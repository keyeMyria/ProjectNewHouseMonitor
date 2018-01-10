#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import logging
import uuid
import datetime
from HouseCrawler.Items.ItemsSZ import *
sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../..'))

logger = logging.getLogger(__name__)


class SZPipeline(object):

    def __init__(self, settings):
        self.settings = settings

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def safe_format_value(self, value):
        try:
            value = '%.05f' % float(value)
            return str(value)
        except Exception:
            pass
        if isinstance(value, dict):
            try:
                value = dict(value)
                return value
            except Exception:
                pass
        if isinstance(value, list):
            try:
                value = value.sort()
                return value
            except Exception:
                pass
        return str(value)

    def check_item_exist(self, item):
        exist_flag = False
        q_object = item.django_model.objects
        if isinstance(item, HouseBaseItem):
            res_object = q_object.filter(house_no=item['house_no']).latest(
                field_name='CurTimeStamp')
            if res_object:
                res_object.NewCurTimeStamp = str(datetime.datetime.now())
                res_object.save()
                exist_flag = True
        elif isinstance(item, BuildingBaseItem):
            res_object = q_object.filter(building_no=item['building_no']).latest(
                field_name='CurTimeStamp')
            if res_object:
                res_object.NewCurTimeStamp = str(datetime.datetime.now())
                res_object.save()
                exist_flag = True
        elif isinstance(item, ApprovalBaseItem):
            res_object = q_object.filter(PresalePermitNumber=item[
                                         'PresalePermitNumber']).latest(field_name='CurTimeStamp')
            if res_object:
                res_object.NewCurTimeStamp = str(datetime.datetime.now())
                res_object.save()
                exist_flag = True

        else:
            pass
        return exist_flag

    def check_item_change(self, item):
        diff_flag = False
        q_object = item.django_model.objects
        monitorkeys = {'house_sts'}
        mainmonitorkeys = {'house_sts', 'HSE_Located', 'HSE_LevelCode', 'Hes_LevelName', 'Hse_URCode',
                           'HSE_CellCode', 'Hse_Type_Room', 'Hse_Type_Hall', 'HSE_Bathroom', 'SHSE_ISPOLICY',
                           'Hse_Class', 'PH_Cdate', 'HSE_Ownership', 'HSE_LDTPermit_SN', 'ddl_ProTypeopt',
                           'hf_name', 'lb_ProStar', 'lb_ProEnd', 'SFLOOR_IN', 'SFLOOR_FH', 'AreaAll', 'Hse_TSUM',
                           'SFLOOR_PRICE', 'Address', 'HSE_IsLevelHeigh', 'LevelHeigh'}
        copymainmonitorkeys = {'HSE_Located', 'HSE_LevelCode', 'Hes_LevelName', 'Hse_URCode',
                               'HSE_CellCode', 'Hse_Type_Room', 'Hse_Type_Hall', 'HSE_Bathroom', 'SHSE_ISPOLICY',
                               'Hse_Class', 'PH_Cdate', 'HSE_Ownership', 'HSE_LDTPermit_SN', 'ddl_ProTypeopt',
                               'hf_name', 'lb_ProStar', 'lb_ProEnd', 'SFLOOR_IN', 'SFLOOR_FH', 'AreaAll', 'Hse_TSUM',
                               'SFLOOR_PRICE', 'Address', 'HSE_IsLevelHeigh', 'LevelHeigh'}
        if isinstance(item, HouseBaseItem):
            res_object = q_object.filter(house_no=item['house_no']).latest(
                field_name='CurTimeStamp')
            changedata = ''
            for key in item:
                if key not in mainmonitorkeys:
                    continue
                if not hasattr(res_object, key):
                    diff_flag = True
                    break
                if self.safe_format_value(item.get(key)) != self.safe_format_value(getattr(res_object, key)):
                    changedata = changedata + 'now' + key + ':' + str(item.get(key)) + ','\
                        + 'last' + key + ':' + \
                        str(getattr(res_object, key)) + ';'
                    diff_flag = True

            item['change_data'] = changedata
            if diff_flag:
                for key in monitorkeys:
                    item[key + 'Latest'] = getattr(res_object, key)
                    if self.safe_format_value(item.get(key)) != self.safe_format_value(
                            getattr(res_object, key)):
                        for nowkey in copymainmonitorkeys:
                            if self.safe_format_value(getattr(res_object, nowkey)) != '':
                                item[nowkey] = getattr(res_object, nowkey)

        elif isinstance(item, BuildingBaseItem):
            res_object = q_object.filter(building_no=item['building_no']).latest(
                field_name='CurTimeStamp')
            changedata = ''
            for key in item:
                if key not in mainmonitorkeys:
                    continue
                if not hasattr(res_object, key):
                    diff_flag = True
                    break

                if self.safe_format_value(item.get(key)) != self.safe_format_value(getattr(res_object, key)):
                    changedata = changedata + 'now' + key + ':' + str(item.get(key)) + ','\
                        + 'last' + key + ':' + \
                        str(getattr(res_object, key)) + ';'
                    diff_flag = True
            item['change_data'] = changedata
            if diff_flag:
                for key in monitorkeys:
                    item[key + 'Latest'] = getattr(res_object, key)
        elif isinstance(item, ApprovalBaseItem):
            res_object = q_object.filter(PresalePermitNumber=item[
                                         'PresalePermitNumber']).latest(field_name='CurTimeStamp')
            changedata = ''
            for key in item:
                if key not in mainmonitorkeys:
                    continue
                if not hasattr(res_object, key):
                    diff_flag = True
                    break
                if self.safe_format_value(item.get(key)) != self.safe_format_value(getattr(res_object, key)):
                    changedata = changedata + 'now' + key + ':' + str(item.get(key)) + ','\
                        + 'last' + key + ':' + \
                        str(getattr(res_object, key)) + ';'
                    diff_flag = True
            item['change_data'] = changedata
            if diff_flag:
                for key in monitorkeys:
                    item[key + 'Latest'] = getattr(res_object, key)
        return diff_flag, item

    def storage_item(self, item):
        if hasattr(item, 'save') and hasattr(item, 'django_model'):
            item['RecordID'] = uuid.uuid1()
            item['CurTimeStamp'] = str(datetime.datetime.now())
            item.save()
            logger.debug("storage item: %(item)s",
                         {'item': item})

    def process_item(self, item, spider):
        if item:

            if self.check_item_exist(item):
                logger.debug("item: %(item)s UUID existed",
                             {'item': item})
                diff_result, diff_item = self.check_item_change(item)
                if diff_result:
                    diff_item['NewCurTimeStamp'] = str(datetime.datetime.now())
                    self.storage_item(diff_item)
            else:
                logger.debug("item: %(item)s met first",
                             {'item': item})
                self.storage_item(item)
            return item
