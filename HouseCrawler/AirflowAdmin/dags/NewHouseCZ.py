# -*-coding=utf-8-*-
import datetime
import functools
import os
import sys

import django
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

BASE_DIR = os.path.abspath(os.environ.get('AIRFLOW_HOME'))
HOUSESERVICECORE_DIR = os.path.abspath(os.path.join(BASE_DIR, 'ServiceCore'))
HOUSEADMIN_DIR = os.path.abspath(os.path.join(BASE_DIR, 'ServiceCore/HouseAdmin'))
HOUSECRAWLER_DIR = os.path.abspath(os.path.join(BASE_DIR, 'ServiceCore/HouseCrawler'))
HOUSESERVICE_DIR = os.path.abspath(os.path.join(BASE_DIR, 'ServiceCore/SpiderService'))

sys.path.append(BASE_DIR)
sys.path.append(HOUSEADMIN_DIR)
sys.path.append(HOUSECRAWLER_DIR)
sys.path.append(HOUSESERVICE_DIR)
sys.path.append(HOUSESERVICECORE_DIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'HouseAdmin.settings'
django.setup()

from HouseNew.models import *
from services.spider_service import spider_call


def just_one_instance(func):
    @functools.wraps(func)
    def f(*args, **kwargs):
        import socket
        try:
            global s
            s = socket.socket()
            host = socket.gethostname()
            s.bind((host, 60223))
        except Exception:
            print('already has an instance')
            return None
        return func(*args, **kwargs)

    return f


STARTDATE = datetime.datetime.now() - datetime.timedelta(hours=6)

default_args = {
    'owner': 'airflow',
    'start_date': STARTDATE,
    'email': ['coder.gsy@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=1),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime.datetime(2016, 5, 29, 11, 30),
}

spider_settings = {
    'ITEM_PIPELINES': {
        'HouseCrawler.Pipelines.PipelinesCZ.CZPipeline': 300,
    },
    'SPIDER_MIDDLEWARES': {
        'HouseCrawler.SpiderMiddleWares.SpiderMiddleWaresCZ.ProjectBaseHandleMiddleware': 102,
        'HouseCrawler.SpiderMiddleWares.SpiderMiddleWaresCZ.ProjectInfoHandleMiddleware': 103,
        'HouseCrawler.SpiderMiddleWares.SpiderMiddleWaresCZ.BuildingInfoHandleMiddleware': 104,
    },
    'RETRY_ENABLE': True,
    'CLOSESPIDER_TIMEOUT': 3600 * 3.5
}

dag = DAG('NewHouseCZ', default_args=default_args, schedule_interval="15 */4 * * *")

t1 = PythonOperator(
    task_id='LoadProjectBaseCZ',
    python_callable=spider_call,
    op_kwargs={'spiderName': 'DefaultCrawler',
               'settings': spider_settings,
               'urlList': [{'source_url': 'http://gs.czfdc.com.cn/newxgs/Pages/Code/Xjfas.ashx?'
                                          'kfs=&lpmc=&method=GetYszData&page=1&ysxkz=',
                            'meta': {'PageType': 'ProjectBase'}}]},
    dag=dag
)

project_info_list = []
cur = ProjectBaseChangzhou.objects.all()

for i, item in enumerate(cur):
    project_info = {
        'source_url': item.ProjectURL,
        'meta': {'PageType': 'ProjectInfo', 'ProjectUUID': str(item.ProjectUUID),
                 'ProjectName': item.ProjectName, 'ProjectRecordURL': item.ProjectRecordURL}
    }
    project_info_list.append(project_info)

t2 = PythonOperator(
    task_id='LoadProjectInfoCZ',
    python_callable=spider_call,
    op_kwargs={'spiderName': 'DefaultCrawler',
               'settings': spider_settings,
               'urlList': project_info_list},
    dag=dag
)

building_info_list = []

cur = ProjectBaseChangzhou.objects.aggregate(*[{"$sort": {"CurTimeStamp": 1}},
                                               {'$group':
                                                    {'_id': "$ProjectUUID",
                                                     'ProjectName': {'$first': '$ProjectName'},
                                                     'ProjectUUID': {'$first': '$ProjectUUID'},
                                                     'ProjectPresaleNum': {'$first': '$ProjectPresaleNum'},
                                                     # 'BuildingName': {'$first': '$BuildingName'},
                                                     # 'BuildingUUID': {'$first': '$BuildingUUID'},
                                                     'ProjectBuildingListURL': {'$first': '$ProjectBuildingListURL'}
                                                     }
                                                }])
for item in cur:
    try:
        if item['ProjectBuildingListURL']:
            if item['ProjectBuildingListURL'] != '#':
                building_info = {'source_url': item['ProjectBuildingListURL'],
                                 'meta': {'PageType': 'BuildingInfo',
                                          'ProjectName': item['ProjectName'],
                                          'ProjectPresaleNum': item['ProjectPresaleNum'],
                                          # 'BuildingName': item['BuildingName'],
                                          'ProjectUUID': str(item['ProjectUUID']),
                                          # 'BuildingUUID': str(item['BuildingUUID'])
                                          }}
                building_info_list.append(building_info)
    except Exception as e:
        print(e)

t3 = PythonOperator(
    task_id='LoadBuildingInfoCZ',
    python_callable=spider_call,
    op_kwargs={'spiderName': 'DefaultCrawler',
               'settings': spider_settings,
               'urlList': building_info_list},
    dag=dag)