# -*- coding: utf-8 -*-
import datetime
import os
import sys
import requests
import re
import random

import django
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

BASE_DIR = os.path.abspath(os.environ.get('AIRFLOW_HOME'))
HOUSESERVICECORE_DIR = os.path.abspath(os.path.join(BASE_DIR, 'ServiceCore'))
HOUSEADMIN_DIR = os.path.abspath(
    os.path.join(
        BASE_DIR,
        'ServiceCore/HouseAdmin'))
HOUSECRAWLER_DIR = os.path.abspath(
    os.path.join(BASE_DIR, 'ServiceCore/HouseCrawler'))
HOUSESERVICE_DIR = os.path.abspath(
    os.path.join(BASE_DIR, 'ServiceCore/SpiderService'))

sys.path.append(BASE_DIR)
sys.path.append(HOUSEADMIN_DIR)
sys.path.append(HOUSECRAWLER_DIR)
sys.path.append(HOUSESERVICE_DIR)
sys.path.append(HOUSESERVICECORE_DIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'HouseAdmin.settings'
django.setup()

from HouseNew.models import *
from services.spider_service import spider_call

STARTDATE = datetime.datetime.now() - datetime.timedelta(hours=9)

default_args = {
    'owner': 'sun',
    'start_date': STARTDATE,
    'email': ['jiajia.sun@yunfangdata.com'],
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
        'HouseCrawler.Pipelines.PipelinesShangHai.SHPipeline': 300,
    },
    'SPIDER_MIDDLEWARES': {
        'HouseCrawler.SpiderMiddleWares.SpiderMiddleWaresShangHai.ProjectBaseHandleMiddleware': 102,
        'HouseCrawler.SpiderMiddleWares.SpiderMiddleWaresShangHai.OpenningunitBaseHandleMiddleware': 103,
        'HouseCrawler.SpiderMiddleWares.SpiderMiddleWaresShangHai.BuildingBaseHandleMiddleware': 104,
        'HouseCrawler.SpiderMiddleWares.SpiderMiddleWaresShangHai.HouseBaseHandleMiddleware': 105,
        'HouseCrawler.SpiderMiddleWares.SpiderMiddleWaresShangHai.GetProjectBaseHandleMiddleware': 101,
    },
    'DOWNLOADER_MIDDLEWARES':{
        'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
        'HouseCrawler.DownloadMiddleWares.ProxyMiddleWares.RandomUserAgent': 1,
        'HouseCrawler.DownloadMiddleWares.ProxyMiddleWares.ProxyMiddleware': None,
        'HouseCrawler.DownloadMiddleWares.RetryMiddleWares.RetryMiddleware': 120,
    },
    'RETRY_ENABLE': False,
    'CLOSESPIDER_TIMEOUT': 3600 * 7.5,
    'RETRY_TIMES': 15,
    'CONCURRENT_REQUESTS': 64,
}

dag = DAG(
    'NewHouseShangHai',
    default_args=default_args,
    schedule_interval="30 */5 * * *")


def getData():
    resultdata = []
    headers = {
        'Host': 'www.fangdi.com.cn',
        'Proxy-Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Upgrade-Insecure-Requests': '1',
        'Referer': 'http://www.fangdi.com.cn/moreRegion.asp',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    }
    url = 'http://www.fangdi.com.cn/moreRegion.asp'
    req = requests.get(url, headers=headers)
    req.encoding = req.apparent_encoding
    html = str(req.text).replace('\r', '').replace('\n', '') \
        .replace('\t', '').replace(" ", "")
    tables = re.findall(r'districtID=(\d+)&Region_ID=(\d+)">', html)
    for districtID, Region_ID in tables:
        resultdata.append({
            'county_no': districtID,
            'blank_no': Region_ID
        })
    return resultdata
selcirls = ['1', '2', '3']
selstats = ['1', '2', '4']
datas = getData()
project_info_list = []
for selstat in selstats:
    for data in datas:
        for selcirl in selcirls:
            starurl = 'http://www.fangdi.com.cn/complexpro.asp?page=1&districtID=%s&Region_ID=%s' \
                '&projectAdr=&projectName=&startCod=&buildingType=1' \
                '&houseArea=0&averagePrice=0&selState=%s&selCircle=%s' \
                % (data['county_no'], data['blank_no'], selstat, selcirl)

            project_info = {'source_url': starurl,
                            'meta': {'PageType': 'GetProjectBase'}}
            project_info_list.append(project_info)
t1 = PythonOperator(
    task_id='LoadProjectBaseShanghai',
    python_callable=spider_call,
    op_kwargs={
        'spiderName': 'DefaultCrawler',
        'settings': spider_settings,
        'urlList': project_info_list,
        'spider_count': 10
    },
    dag=dag
)
building_info_list = []
cur = BuildingBaseShanghai.objects.aggregate(
    *[
        {
            "$sort": {
                "CurTimeStamp": 1}}, {
                    '$group': {
                        '_id': "$building_no",
                        'project_name': {'$last': '$project_name'},
                        'project_no': {'$last': '$project_no'},
                        'opening_unit_no': {'$last': '$opening_unit_no'},
                        'building_name': {'$last': '$building_name'},
                        'building_no': {'$last': '$building_no'},
                        'building_url': {'$last': '$building_url'},
                        'building_sts': {'$last': '$building_sts'}
                    }}])
for item in cur:
    if item['building_url'] and item['building_sts']=='在售':
        building_info = {
            'source_url': item['building_url'],
            'meta': {
                'PageType': 'HouseBase',
                'project_no': item['project_no'],
                'project_name': item['project_name'],
                'opening_unit_no': str(item['opening_unit_no']),
                'building_no': str(item['building_no'])}}
        building_info_list.append(building_info)


t2 = PythonOperator(
    task_id='LoadBuildingInfoShanghai',
    python_callable=spider_call,
    op_kwargs={'spiderName': 'DefaultCrawler',
               'settings': spider_settings,
               'urlList': building_info_list,
               'spider_count': 10},
    dag=dag)
