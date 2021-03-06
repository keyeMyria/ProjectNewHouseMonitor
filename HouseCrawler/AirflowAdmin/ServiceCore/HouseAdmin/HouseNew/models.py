# encoding = utf-8
import datetime
import uuid
import time

from django_mongoengine import *
from django_mongoengine import fields


# Guiyang City Model
class ProjectBaseGuiyang(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    ProjectRegName = fields.StringField(default='', max_length=1024, null=False)
    ProjectURL = fields.URLField(default=None, null=True, blank=True)
    ProjectURLCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
        ]
    }


class ProjectInfoGuiyang(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectCompany = fields.StringField(default='', max_length=1024, null=False)
    ProjectAddress = fields.StringField(default='', max_length=1024, null=False)
    ProjectUsage = fields.StringField(default='', max_length=1024, null=False)
    ProjectArea = fields.StringField(default='', max_length=1024, null=False)
    ProjectBuildArea = fields.StringField(default='', max_length=1024, null=False)
    ProjectBuildingCompany = fields.StringField(default='', max_length=1024, null=False)
    ProjectDesignCompany = fields.StringField(default='', max_length=1024, null=False)
    ProjectRegName = fields.StringField(default='', max_length=1024, null=False)
    ProjectSalePhone = fields.StringField(default='', max_length=1024, null=False)
    ProjectDescription = fields.StringField(default='', max_length=1024, null=False)
    ProjectBuildingNum = fields.StringField(default='', max_length=1024, null=False)
    ProjectAreaCode = fields.StringField(default='', max_length=1024, null=False)
    ProjectAreaPlanCode = fields.StringField(default='', max_length=1024, null=False)
    ProjectEngPlanCode = fields.StringField(default='', max_length=1024, null=False)
    ProjectBuildingCode = fields.StringField(default='', max_length=1024, null=False)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
        ]
    }


class BuildingInfoGuiyang(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    BuildingName = fields.StringField(default='', max_length=1024, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                    binary=False, null=False)
    BuildingURL = fields.URLField(default=None, null=True, blank=True)
    BuildingURLCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectRegName = fields.StringField(default=str(datetime.datetime.now()), index=True)
    BuildingCode = fields.StringField(default=str(datetime.datetime.now()), index=True)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectName',
            'ProjectUUID',
            'BuildingUUID',
            'BuildingName',
        ]
    }


class HouseInfoGuiyang(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    BuildingName = fields.StringField(default='', max_length=1024, null=False)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                    binary=False, null=False)
    HouseName = fields.StringField(default='', max_length=1024, null=False)
    HouseUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                 binary=False, null=False)
    HouseInfoText = fields.StringField(default='', max_length=1024, null=False)
    HouseUnit = fields.StringField(default='', max_length=1024, null=False)
    HouseFloor = fields.StringField(default='', max_length=1024, null=False)
    HouseNum = fields.StringField(default='', max_length=1024, null=False)
    HouseSaleState = fields.StringField(default='', max_length=1024, null=False)
    HouseSaleStateLatest = fields.StringField(default='', max_length=1024, null=False)
    HouseBuildingArea = fields.StringField(default='', max_length=1024, null=False)
    HouseUsage = fields.StringField(default='', max_length=1024, null=False)
    HouseStructure = fields.StringField(default='', max_length=1024, null=False)
    HouseType = fields.StringField(default='', max_length=1024, null=False)
    HouseReqURL = fields.StringField(default='', max_length=1024, null=False)
    HouseNumCheck = fields.StringField(default='', max_length=1024, null=False)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectName',
            'BuildingName',
            'ProjectUUID',
            'BuildingUUID',
            'HouseUUID',
            'HouseName'
        ]
    }


# Taiyuan City Model
class ProjectBaseTaiyuan(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    ProjectRegName = fields.StringField(default='', max_length=1024, null=False)
    ProjectURL = fields.URLField(default=None, null=True, blank=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectType = fields.StringField(default='', max_length=1024, null=False)
    ProjectDistrict = fields.StringField(default='', max_length=1024, null=False)
    ProjectCompanyId = fields.StringField(default='', max_length=1024, null=False)
    ProjectCompanyName = fields.StringField(default='', max_length=1024, null=False)
    ProjectCompanyCode = fields.StringField(default='', max_length=1024, null=False)
    ProjectCompanyLevel = fields.StringField(default='', max_length=1024, null=False)
    ProjectCompanyLevelCode = fields.StringField(default='', max_length=1024, null=False)
    ProjectCompanyCorporation = fields.StringField(default='', max_length=1024, null=False)
    ProjectCompanyCorporationPhone = fields.StringField(default='', max_length=1024, null=False)
    ProjectURLCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
        ]
    }


class ProjectInfoTaiyuan(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectAddress = fields.StringField(default='', max_length=1024, null=False)
    ProjectSaleRange = fields.StringField(default='', max_length=1024, null=False)
    ProjectBuildArea = fields.StringField(default='', max_length=1024, null=False)
    ProjectSaleArea = fields.StringField(default='', max_length=1024, null=False)
    ProjectSaleBuildingNum = fields.StringField(default='', max_length=1024, null=False)
    ProjectSaleHouseNum = fields.StringField(default='', max_length=1024, null=False)
    ProjectLHRatio = fields.StringField(default='', max_length=1024, null=False)
    ProjectRJRatio = fields.StringField(default='', max_length=1024, null=False)
    ProjectBuildDate = fields.StringField(default='', max_length=1024, null=False)
    ProjectCompleteDate = fields.StringField(default='', max_length=1024, null=False)
    ProjectBuildingCompany = fields.StringField(default='', max_length=1024, null=False)
    ProjectDesignCompany = fields.StringField(default='', max_length=1024, null=False)
    ProjectManageCompany = fields.StringField(default='', max_length=1024, null=False)
    ProjectSaleCompany = fields.StringField(default='', max_length=1024, null=False)
    ProjectUnitPrice = fields.StringField(default='', max_length=1024, null=False)
    ProjectCompanmy = fields.StringField(default='', max_length=1024, null=False)
    ProjectUsage = fields.StringField(default='', max_length=1024, null=False)
    ProjectBuilding = fields.StringField(default='', max_length=1024, null=False)
    ProjectRegId = fields.StringField(default='', max_length=1024, null=False)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
        ]
    }


class BuildingInfoTaiyuan(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    BuildingName = fields.StringField(default='', max_length=1024, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                    binary=False, null=False)
    BuildingURL = fields.URLField(default=None, null=True, blank=True)
    BuildingURLCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    BuildingCode = fields.StringField(default='', max_length=1024, null=False)
    BuildingMCode = fields.StringField(default='', max_length=1024, null=False)
    BuildingBaseArea = fields.StringField(default='', max_length=1024, null=False)
    BuildingShareArea = fields.StringField(default='', max_length=1024, null=False)
    BuildingArea = fields.StringField(default='', max_length=1024, null=False)
    BuildingStructure = fields.StringField(default='', max_length=1024, null=False)
    BuildingYear = fields.StringField(default='', max_length=1024, null=False)
    BuildingFloorNum = fields.StringField(default='', max_length=1024, null=False)
    BuildingFloorAbove = fields.StringField(default='', max_length=1024, null=False)
    BuildingFloorBelow = fields.StringField(default='', max_length=1024, null=False)
    BuildingUnitNum = fields.StringField(default='', max_length=1024, null=False)
    BuildingSaleName = fields.StringField(default='', max_length=1024, null=False)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'BuildingUUID',
            'BuildingName',
        ]
    }


class HouseInfoTaiyuan(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    BuildingName = fields.StringField(default='', max_length=1024, null=False)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                    binary=False, null=False)
    HouseName = fields.StringField(default='', max_length=1024, null=False)
    HouseUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                 binary=False, null=False)
    HouseSaleState = fields.StringField(default='', max_length=1024, null=False)
    HouseSaleStateLatest = fields.StringField(default='', max_length=1024, null=False)
    HouseBuildingArea = fields.StringField(default='', max_length=1024, null=False)
    HouseUsage = fields.StringField(default='', max_length=1024, null=False)
    HouseStructure = fields.StringField(default='', max_length=1024, null=False)
    HouseType = fields.StringField(default='', max_length=1024, null=False)
    HouseSaleSubState = fields.StringField(default='', max_length=1024, null=False)
    HouseSaleSubStateLatest = fields.StringField(default='', max_length=1024, null=False)
    HouseUnitPrice = fields.StringField(default='', max_length=1024, null=False)
    HouseAddress = fields.StringField(default='', max_length=1024, null=False)
    HouseId = fields.StringField(default='', max_length=1024, null=False)
    HouseCode = fields.StringField(default='', max_length=1024, null=False)
    HouseFloorTotal = fields.StringField(default='', max_length=1024, null=False)
    HouseBuildingArea = fields.StringField(default='', max_length=1024, null=False)
    HouseInnerArea = fields.StringField(default='', max_length=1024, null=False)
    HouseShareArea = fields.StringField(default='', max_length=1024, null=False)
    HouseYear = fields.StringField(default='', max_length=1024, null=False)
    HouseGroundCode = fields.StringField(default='', max_length=1024, null=False)
    HouseGroundArea = fields.StringField(default='', max_length=1024, null=False)
    HouseGetGroundType = fields.StringField(default='', max_length=1024, null=False)
    HouseGroundType = fields.StringField(default='', max_length=1024, null=False)
    HouseGroundLimit = fields.StringField(default='', max_length=1024, null=False)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'BuildingName',
            'ProjectUUID',
            'BuildingUUID',
            'HouseUUID',
            'HouseName'
        ]
    }


# 常州 ORM
class ProjectBaseChangzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=255, null=False)
    ProjectPresaleNum = fields.StringField(default='', max_length=255, null=False)
    ProjectPresaleId = fields.StringField(default='', max_length=255, null=False)
    ProjectPresaleDate = fields.StringField(default='', max_length=255, null=False)
    ProjectURL = fields.StringField(default='', max_length=255, null=False)
    ProjectRecordURL = fields.StringField(default='', max_length=255, null=False)
    ProjectBuildingListURL = fields.StringField(default='', max_length=255, null=False)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
            'ProjectURL',
            'ProjectRecordURL',
            'ProjectBuildingListURL',
        ]
    }


class ProjectInfoChangzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=255, null=False)
    ProjectCompany = fields.StringField(default='', max_length=255, null=False)
    ProjectAddress = fields.StringField(default='', max_length=255, null=False)
    ProjectRegion = fields.StringField(default='', max_length=255, null=False)
    # ProjectRegionNum = fields.StringField(default='', max_length=255, null=False)
    ProjectPresaleArea = fields.StringField(default='', max_length=255, null=False)
    ProjectPresaleHouseNum = fields.StringField(default='', max_length=255, null=False)
    ProjectPresaleBuildingRange = fields.StringField(default='', max_length=255, null=False)
    ProjectSalesAgency = fields.StringField(default='', max_length=255, null=False)
    ProjectSupervisorBank = fields.StringField(default='', max_length=255, null=False)
    ProjectSupervisorAccount = fields.StringField(default='', max_length=255, null=False)
    ProjectBankGuarantee = fields.StringField(default='', max_length=255, null=False)
    ProjectRecordsInfo = fields.ListField(default=[], max_length=1024, null=False)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
            'ProjectCompany',
        ]
    }


class BuildingInfoChangzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=255, null=False)
    ProjectPresaleNum = fields.StringField(default='', max_length=255, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                    binary=False, null=False)
    BuildingName = fields.StringField(default='', max_length=255, null=False)
    BuildingURL = fields.StringField(default='', max_length=255, null=False)
    BuildingArea = fields.StringField(default='', max_length=255, null=False)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
            'ProjectPresaleNum',
            'BuildingUUID',
            'BuildingName'
        ]
    }


class HouseInfoChangzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=255, null=False)
    ProjectPresaleNum = fields.StringField(default='', max_length=255, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                    binary=False, null=False)
    BuildingName = fields.StringField(default='', max_length=255, null=False)
    HouseUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                 binary=False, null=False)
    HouseBuildingArea = fields.StringField(default='', max_length=255, null=False)
    HouseContractPrice = fields.StringField(default='', max_length=255, null=False)
    HouseUsage = fields.StringField(default='', max_length=255, null=False)
    HouseLabel = fields.StringField(default='', max_length=255, null=False)
    HouseCurCell = fields.StringField(default='', max_length=255, null=False)
    HouseSaleStatus = fields.StringField(default='', max_length=255, null=False)
    HouseSaleStateLatest = fields.StringField(default='', max_length=255, null=False)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
            'ProjectPresaleNum',
            'BuildingUUID',
            'BuildingName',
            'HouseUUID',
            'HouseUsage',
            'HouseLabel',
            'HouseSaleStatus',
            'HouseSaleStateLatest'
        ]
    }


# Hefei City Model
class ProjectInfoHefei(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    ProjectID = fields.StringField(default='', max_length=1024, null=False)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectAddress = fields.StringField(default='', max_length=1024, null=False)
    ProjectManageCompany = fields.StringField(default='', max_length=1024, null=False)
    ProjectDevelopCompany = fields.StringField(default='', max_length=1024, null=False)
    ProjectBuildingArea = fields.StringField(default='', max_length=1024, null=False)
    ProjectMainStructure = fields.StringField(default='', max_length=1024, null=False)
    ProjectGreenRatio = fields.StringField(default='', max_length=1024, null=False)
    ProjectPlotRatio = fields.StringField(default='', max_length=1024, null=False)
    ProjectTranslateTimes = fields.StringField(default='', max_length=1024, null=False)
    ProjectTranslateRatio = fields.StringField(default='', max_length=1024, null=False)
    ProjectDistrict = fields.StringField(default='', max_length=1024, null=False)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectID',
            'ProjectName',
        ]
    }


class BuildingInfoHefei(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    ProjectID = fields.StringField(default='', max_length=1024, null=False)
    BuildingName = fields.StringField(default='', max_length=1024, null=False)
    BuildingRegName = fields.StringField(default='', max_length=1024, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                    binary=False, null=False)
    BuildingURL = fields.URLField(default=None, null=True, blank=True)
    BuildingURLCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    BuildingStructure = fields.StringField(default='', max_length=1024, null=False)
    BuildingFloorAbove = fields.StringField(default='', max_length=1024, null=False)
    BuildingFloorBelow = fields.StringField(default='', max_length=1024, null=False)
    BuildingHouseNum = fields.StringField(default='', max_length=1024, null=False)
    BuildingBusiness = fields.StringField(default='', max_length=1024, null=False)
    BuildingOfficeNum = fields.StringField(default='', max_length=1024, null=False)
    BuildingOtherNum = fields.StringField(default='', max_length=1024, null=False)
    BuildingAreaCode = fields.StringField(default='', max_length=1024, null=False)
    BuildingPlanCode = fields.StringField(default='', max_length=1024, null=False)
    BuildingUsage = fields.StringField(default='', max_length=1024, null=False)
    BuildingDesignCompany = fields.StringField(default='', max_length=1024, null=False)
    BuildingPreSellArea = fields.StringField(default='', max_length=1024, null=False)
    BuildingOnlineSellArea = fields.StringField(default='', max_length=1024, null=False)
    BuildingOpenDate = fields.StringField(default='', max_length=1024, null=False)
    BuildingCompleteDate = fields.StringField(default='', max_length=1024, null=False)
    BuildingDeliverDate = fields.StringField(default='', max_length=1024, null=False)
    BuildingAgent = fields.StringField(default='', max_length=1024, null=False)
    BuildingSellPhone = fields.StringField(default='', max_length=1024, null=False)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectName',
            'ProjectID',
            'ProjectUUID',
            'BuildingUUID',
            'BuildingName',
        ]
    }


class HouseInfoHefei(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    BuildingName = fields.StringField(default='', max_length=1024, null=False)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                    binary=False, null=False)
    HouseName = fields.StringField(default='', max_length=1024, null=False)
    HouseID = fields.StringField(default='', max_length=1024, null=False)
    HouseUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                 binary=False, null=False)
    HouseSaleState = fields.StringField(default='', max_length=1024, null=False)
    HouseSaleStateLatest = fields.StringField(default='', max_length=1024, null=False)
    HouseStructure = fields.StringField(default='', max_length=1024, null=False)
    HouseType = fields.StringField(default='', max_length=1024, null=False)
    HouseShareArea = fields.StringField(default='', max_length=1024, null=False)
    HouseNum = fields.StringField(default='', max_length=1024, null=False)
    HouseBuildingArea = fields.StringField(default='', max_length=1024, null=False)
    HouseAddress = fields.StringField(default='', max_length=1024, null=False)
    HousePreSellPrice = fields.StringField(default='', max_length=1024, null=False)
    HouseUsage = fields.StringField(default='', max_length=1024, null=False)
    HouseInnerArea = fields.StringField(default='', max_length=1024, null=False)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectName',
            'BuildingName',
            'ProjectUUID',
            'BuildingUUID',
            'HouseUUID',
            'HouseName'
        ]
    }


# Dalian Models
class ProjectBaseDalian(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    ProjectDistrict = fields.StringField(default='', max_length=1024, null=False)
    ProjectAddress = fields.StringField(default='', max_length=1024, null=False)
    ProjectCorporation = fields.StringField(default='', max_length=1024, null=False)
    ProjectURL = fields.URLField(default=None, null=True, blank=True)
    ProjectURLCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
            'ProjectURL',
        ]
    }


class ProjectInfoDalian(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    ProjectAddress = fields.StringField(default='', max_length=1024, null=False)
    ProjectCompany = fields.StringField(default='', max_length=1024, null=False)
    ProjectRegName = fields.StringField(default='', max_length=1024, null=False)
    ProjectAreaPlanLicenseCode = fields.StringField(default='', max_length=1024, null=False)
    ProjectPlanLicenseCode = fields.StringField(default='', max_length=1024, null=False)
    ProjectSaleSum = fields.DictField(default={'code': 0}, null=False)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
        ]
    }


class BuildingInfoDalian(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    BuildingRegName = fields.StringField(default='', max_length=1024, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                    binary=False, null=False)
    BuildingName = fields.StringField(default='', max_length=1024, null=False)
    BuildingAddress = fields.StringField(default='', max_length=1024, null=False)
    BuildingHouseNum = fields.StringField(default='', max_length=1024, null=False)
    BuildingArea = fields.StringField(default='', max_length=1024, null=False)
    BuildingURL = fields.URLField(default=None, null=True, blank=True)
    BuildingURLCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectName',
            'ProjectUUID',
            'BuildingRegName',
            'BuildingUUID',
            'BuildingName',
        ]
    }


class HouseInfoDalian(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    BuildingName = fields.StringField(default='', max_length=1024, null=False)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                    binary=False, null=False)
    HouseUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                 binary=False, null=False)
    HouseName = fields.StringField(default='', max_length=1024, null=False)
    HouseFloor = fields.StringField(default='', max_length=1024, null=False)
    HouseSaleState = fields.StringField(default='', max_length=1024, null=False)
    HouseSaleStateLatest = fields.StringField(default='', max_length=1024, null=False)
    HouseInfoStr = fields.StringField(default='', max_length=1024, null=False)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectName',
            'BuildingName',
            'ProjectUUID',
            'BuildingUUID',
            'HouseUUID',
            'HouseName'
        ]
    }


class ProjectBaseDongguan(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    ProjectDistrict = fields.StringField(default='', max_length=1024, null=False)
    ProjectAddress = fields.StringField(default='', max_length=1024, null=False)
    ProjectSaleSum = fields.StringField(default='', max_length=1024, null=False)
    ProjectURL = fields.URLField(default=None, null=True, blank=True)
    ProjectURLCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
            'ProjectURL',
        ]
    }


class ProjectInfoDongguan(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    ProjectAddress = fields.StringField(default='', max_length=1024, null=False)
    ProjectUsage = fields.StringField(default='', max_length=1024, null=False)
    ProjectArea = fields.StringField(default='', max_length=1024, null=False)
    ProjectHouseNum = fields.StringField(default='', max_length=1024, null=False)
    ProjectCompany = fields.StringField(default='', max_length=1024, null=False)
    ProjectCorporation = fields.StringField(default='', max_length=1024, null=False)
    ProjectRegName = fields.StringField(default='', max_length=1024, null=False)
    ProjectAreaPlanLicenseCode = fields.StringField(default='', max_length=1024, null=False)
    ProjectPlanLicenseCode = fields.StringField(default='', max_length=1024, null=False)
    ProjectConstructionLicenseCode = fields.StringField(default='', max_length=1024, null=False)
    ProjectConstructionCompany = fields.StringField(default='', max_length=1024, null=False)
    ProjectAuthenticFlag = fields.StringField(default='', max_length=1024, null=False)
    ProjectSaleArea = fields.StringField(default='', max_length=1024, null=False)
    ProjectSaleNum = fields.StringField(default='', max_length=1024, null=False)
    ProjectSaledArea = fields.StringField(default='', max_length=1024, null=False)
    ProjectSaledNum = fields.StringField(default='', max_length=1024, null=False)
    ProjectUnavailableArea = fields.StringField(default='', max_length=1024, null=False)
    ProjectUnavailableNum = fields.StringField(default='', max_length=1024, null=False)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
            'ProjectRegName',
        ]
    }


class BuildingInfoDongguan(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectRegName = fields.StringField(default='', max_length=1024, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                    binary=False, null=False)
    BuildingName = fields.StringField(default='', max_length=1024, null=False)
    BuildingFloorNum = fields.StringField(default='', max_length=1024, null=False)
    BuildingHouseNum = fields.StringField(default='', max_length=1024, null=False)
    BuildingUsage = fields.StringField(default='', max_length=1024, null=False)
    BuildingSaleArea = fields.StringField(default='', max_length=1024, null=False)
    BuildingURL = fields.URLField(default=None, null=True, blank=True)
    BuildingURLCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectName',
            'ProjectUUID',
            'ProjectRegName',
            'BuildingUUID',
            'BuildingName',
        ]
    }


class HouseInfoDongguan(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    BuildingName = fields.StringField(default='', max_length=1024, null=False)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                    binary=False, null=False)
    HouseUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                 binary=False, null=False)
    HouseName = fields.StringField(default='', max_length=1024, null=False)
    HouseFloor = fields.StringField(default='', max_length=1024, null=False)
    HouseSaleState = fields.StringField(default='', max_length=1024, null=False)
    HouseSaleStateLatest = fields.StringField(default='', max_length=1024, null=False)
    HouseRecordState = fields.StringField(default='', max_length=1024, null=False)
    HouseRecordStateLatest = fields.StringField(default='', max_length=1024, null=False)
    HousePledgeState = fields.StringField(default='', max_length=1024, null=False)
    HousePledgeStateLatest = fields.StringField(default='', max_length=1024, null=False)
    HouseAttachState = fields.StringField(default='', max_length=1024, null=False)
    HouseAttachStateLatest = fields.StringField(default='', max_length=1024, null=False)
    HouseUsage = fields.StringField(default='', max_length=1024, null=False)
    HouseBuildingArea = fields.StringField(default='0.0', max_length=1024, null=False)
    HouseInnerArea = fields.StringField(default='0.0', max_length=1024, null=False)
    HouseShareArea = fields.StringField(default='0.0', max_length=1024, null=False)
    HouseUnitPrice = fields.StringField(default='0.0', null=False)
    HousePrice = fields.StringField(default='0.0', null=False)
    HousePriceFlag = fields.BooleanField(default=False, null=False)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectName',
            'BuildingName',
            'ProjectUUID',
            'BuildingUUID',
            'HouseUUID',
            'HouseName'
        ]
    }


class ProjectBaseChangsha(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    ProjectRegUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                      binary=False, null=False)
    ProjectRegName = fields.StringField(default='', max_length=1024, null=False)
    ProjectRegDate = fields.StringField(default='', max_length=1024, null=False)
    ProjectAddress = fields.StringField(default='', max_length=1024, null=False)
    ProjectURL = fields.URLField(default=None, null=True, blank=True)
    ProjectURLCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
        ]
    }


class ProjectInfoChangsha(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    ProjectDistrict = fields.StringField(default='', max_length=1024, null=False)
    ProjectBaseLicenseCode = fields.StringField(default='', max_length=1024, null=False)
    ProjectCompany = fields.StringField(default='', max_length=1024, null=False)
    ProjectBuildingNum = fields.StringField(default='', max_length=1024, null=False)
    ProjectAddress = fields.StringField(default='', max_length=1024, null=False)
    ProjectBasePrice = fields.StringField(default='', max_length=1024, null=False)
    ProjectSaleAddress = fields.StringField(default='', max_length=1024, null=False)
    ProjectSalePhone = fields.StringField(default='', max_length=1024, null=False)
    ProjectHouseNum = fields.StringField(default='', max_length=1024, null=False)
    ProjectBusLine = fields.StringField(default='', max_length=1024, null=False)
    ProjectTotalArea = fields.StringField(default='', max_length=1024, null=False)
    ProjectBuildingArea = fields.StringField(default='', max_length=1024, null=False)
    ProjectDesignCompany = fields.StringField(default='', max_length=1024, null=False)
    ProjectSaleAgent = fields.StringField(default='', max_length=1024, null=False)
    ProjectManageCompany = fields.StringField(default='', max_length=1024, null=False)
    ProjectBuildCompany = fields.StringField(default='', max_length=1024, null=False)
    ProjectFinishAt = fields.StringField(default='', max_length=1024, null=False)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
        ]
    }


class BuildingInfoChangsha(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    BuildingRegName = fields.StringField(default='', max_length=1024, null=False)
    BuildingRegDate = fields.StringField(default='', max_length=1024, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                    binary=False, null=False)
    BuildingName = fields.StringField(default='', max_length=1024, null=False)
    BuildingAreaLicenceCode = fields.StringField(default='', max_length=1024, null=False)
    BuildingEngPlanLicenceCode = fields.StringField(default='', max_length=1024, null=False)
    BuildingAreaPlanLicenceCode = fields.StringField(default='', max_length=1024, null=False)
    BuildingBuildLicenceCode = fields.StringField(default='', max_length=1024, null=False)
    BuildingRegArea = fields.StringField(default='', max_length=1024, null=False)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectName',
            'ProjectUUID',
            'BuildingRegName',
            'BuildingUUID',
            'BuildingName',
        ]
    }


class HouseInfoChangsha(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    BuildingName = fields.StringField(default='', max_length=1024, null=False)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                    binary=False, null=False)
    HouseUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                 binary=False, null=False)
    HouseName = fields.StringField(default='', max_length=1024, null=False)
    HouseFloor = fields.StringField(default='', max_length=1024, null=False)
    HouseBuildingArea = fields.StringField(default='', max_length=1024, null=False)
    HouseInnerArea = fields.StringField(default='', max_length=1024, null=False)
    HouseShareArea = fields.StringField(default='', max_length=1024, null=False)
    HouseType = fields.StringField(default='', max_length=1024, null=False)
    HouseUsage = fields.StringField(default='', max_length=1024, null=False)
    HouseSaleState = fields.StringField(default='', max_length=1024, null=False)
    HouseSaleStateLatest = fields.StringField(default='', max_length=1024, null=False)
    HouseDType = fields.StringField(default='', max_length=1024, null=False)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectName',
            'BuildingName',
            'ProjectUUID',
            'BuildingUUID',
            'HouseUUID',
            'HouseName'
        ]
    }


class ProjectBaseHangzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)

    PropertyID = fields.StringField(default='', max_length=100, null=False)  # 楼盘id
    sid = fields.StringField(default='33', max_length=100, null=False)  # sid

    ProjectAllrankvalue = fields.StringField(default='', max_length=100)  # 综合评分
    ProjectName = fields.StringField(default='', max_length=200, null=False)  # 楼盘名称
    PromotionName = fields.StringField(default='', max_length=100)  # 推广名
    DistrictName = fields.StringField(default='', max_length=100)  # 行政区
    RegionName = fields.StringField(default='', max_length=100)  # 街道
    ProjectAddress = fields.StringField(default='', null=False)  # 楼盘地址
    ProjectSellAddress = fields.StringField(default='')  # 售楼地址
    ProjectMainUnitType = fields.StringField(default='', max_length=100)  # 主力户型
    ProjectDecoration = fields.StringField(default='', max_length=100)  # 装修情况
    BuildingType = fields.StringField(default='', max_length=100)  # 建筑类型/建筑形式
    LandUse = fields.StringField(default='', max_length=100)  # 物业类型/土地用途
    FloorAreaRatio = fields.StringField(default='', max_length=100)  # 容积率
    GreeningRate = fields.StringField(default='', max_length=100)  # 绿化率
    FloorArea = fields.StringField(default='', max_length=100)  # 占地面积
    CompletionDate = fields.StringField(default='', max_length=100)  # 竣工时间
    TotalBuidlingArea = fields.StringField(default='', max_length=100)  # 总建筑面积
    HousingCount = fields.StringField(default='', max_length=100)  # 总户数
    LatestDeliversHouseDate = fields.StringField(default='', max_length=100)  # 预计交付时间
    ParkingInfo = fields.StringField(default='', max_length=100)  # 车位信息
    ManagementFees = fields.StringField(default='', max_length=100)  # 物业费
    ManagementCompany = fields.StringField(default='', max_length=100)  # 物业公司

    PropertyRightsDescription = fields.StringField(default='', max_length=100)  # 产权年限
    Developer = fields.StringField(default='', max_length=100)  # 项目公司
    Selltel = fields.StringField(default='', max_length=100)  # 售楼部电话
    OnSaleState = fields.StringField(default='', max_length=100, null=False)  # 楼盘状态/在售状态
    TrafficSituation = fields.StringField(default='')  # 交通情况
    ProjectSupporting = fields.StringField(default='')  # 项目配套
    ProjectIntro = fields.StringField(default='')  # 项目简介
    SourceUrl = fields.URLField(default=None, null=True, blank=True)  # 项目详细URL

    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
        ]
    }


class PresellInfoHangzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(), binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)  # 创建时间
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    PresellUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    PresellID = fields.StringField(default='', max_length=100, null=False)  # 预售证id
    PropertyID = fields.StringField(default='', max_length=100, null=False)  # 预售证id
    sid = fields.StringField(default='', max_length=100, index=True, null=False)  # sid
    PresellNO = fields.StringField(default='')  # 预售证号/预售证编号
    PresellName = fields.StringField(default='')  # 预售证号/预售证编号

    LssueDate = fields.StringField(default='', max_length=100)  # 预售证核发时间
    Applycorp = fields.StringField(default='', max_length=100)  # 预售证申领单位
    LssuingAuthority = fields.StringField(default='', max_length=100)  # 发证机关

    Bank = fields.StringField(default='', max_length=100)  # 资金监管银行
    BankAccount = fields.StringField(default='', max_length=100)  # 资金监管银行账号
    # 接口返回的字段
    num = fields.IntField(default=0, null=True, blank=True)  # 纳入网上预（销）售总套数
    justnum = fields.IntField(default=0, null=True, blank=True)  # 即将解除限制房产套数
    area = fields.FloatField(default=0.00, null=True, blank=True)  # 纳入网上预（销）售总面积
    justarea = fields.FloatField(default=0.00, null=True, blank=True)  # 即将解除限制房产总面积
    avanum = fields.IntField(default=0, null=True, blank=True)  # 可预（销）售总套数
    waitnum = fields.IntField(default=0, null=True, blank=True)  # 待现售房产套数
    avaarea = fields.FloatField(default=0.00, null=True, blank=True)  # 可预（销）售总面积
    waitarea = fields.FloatField(default=0.00, null=True, blank=True)  # 可预（销）售总套数
    resideavanum = fields.IntField(default=0, null=True, blank=True)  # 其中可预（销）售住宅总套数
    limitnum = fields.IntField(default=0, null=True, blank=True)  # 限制房产套数
    resideavaarea = fields.FloatField(default=0.00, null=True, blank=True)  # 可预（销）售住宅总面积
    limitarea = fields.FloatField(default=0.00, null=True, blank=True)  # 限制房产总面积
    dealnum = fields.IntField(default=0, null=True, blank=True)  # 已预（销）售总套数
    notnum = fields.IntField(default=0, null=True, blank=True)  # 未纳入网上销售房产套数
    dealarea = fields.FloatField(default=0.00, null=True, blank=True)  # 已预（销）售总面积
    notarea = fields.IntField(default=0, null=True, blank=True)  # 未纳入网上销售房产总面积
    plannum = fields.IntField(default=0, null=True, blank=True)  # 已预定套数
    planarea = fields.IntField(default=0, null=True, blank=True)  # 已预定总面积

    OpeningDate = fields.StringField(default='', max_length=100)  # 开盘时间
    ApprovalProjectName = fields.StringField(default='', max_length=100)  # 预售审批项目名称
    PresellURL = fields.URLField(default=None, null=True, blank=True)  # 预售价地址
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'PresellUUID',
        ]
    }


class BuildingInfoHangzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    PresellUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    BuildingID = fields.StringField(default='', max_length=100, null=False)  # 楼栋id
    BuildingName = fields.StringField(default='', max_length=100, null=False)  # 楼栋名
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'PresellUUID',
            'BuildingUUID',
        ]
    }


class HouseInfoHangzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    PresellUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    HouseUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    BuildingName = fields.StringField(default='', max_length=100, null=False)  # 楼栋名
    UnitName = fields.StringField(default='', max_length=100, null=True, blank=True)  # 单元
    HouseNO = fields.StringField(default='', max_length=255)  # 户号
    RoughPrice = fields.StringField(default='', null=False)  # 毛坯单价
    HousePrice = fields.StringField(default='', null=False)  # 总价
    HouseBuildingArea = fields.StringField(default='', null=False)  # 建筑面积
    HouseInnerArea = fields.StringField(default='', null=False)  # 套内面积
    HouseState = fields.StringField(default='', max_length=50)  # 当前状态
    HouseStateLatest = fields.StringField(default='', max_length=255, null=False, blank=True)
    HouseType = fields.StringField(default='', max_length=50)  # 户型
    HouseFloor = fields.StringField(default='', null=False)  # 户楼层
    BuildingFloor = fields.StringField(default='', null=False)  # 总楼层
    HouseLocated = fields.StringField(default='', max_length=255)  # 坐落
    HouseUsage = fields.StringField(default='', max_length=50)  # 房屋用途
    HouseStructure = fields.StringField(default='', max_length=50)  # 房屋结构
    RoomRate = fields.StringField(default='', null=False)  # 得房率
    HouseManagementFees = fields.StringField(default='', null=False)  # 物业费
    HouseOrientation = fields.StringField(default='', max_length=50)  # 朝向
    DeclarationTime = fields.StringField(default='', max_length=50)  # 申报时间
    HouseURL = fields.URLField(default=None, null=True, blank=True)  # 户详情地址
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'PresellUUID',
            'BuildingUUID',
            'HouseUUID',
            'HouseState',
            'HouseStateLatest',
        ]
    }


class IndexHouseInfoHangzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    RegionUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    Region = fields.StringField(default='', null=False)
    SignCount = fields.StringField(default='', null=False)
    BookCount = fields.StringField(default='', null=False)
    SaleCount = fields.StringField(default='', null=False)


class IndexInfoHangzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    RegionUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    Region = fields.StringField(default='', null=False)
    SignCount = fields.StringField(default='', null=False)
    SaleArea = fields.StringField(default='', null=False)


# Chongqing Model
class ProjectBaseChongqing(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    ProjectBaseName = fields.StringField(default='', max_length=1024, null=False)
    ProjectDistrict = fields.StringField(default='', max_length=1024, null=False)
    ProjectAddress = fields.StringField(default='', max_length=1024, null=False)
    ProjectCorporation = fields.StringField(default='', max_length=1024, null=False)
    ProjectSoldNum = fields.StringField(default='0', max_length=1024, null=False)
    ProjectSoldArea = fields.StringField(default='0.0', max_length=1024, null=False)
    ProjectURL = fields.URLField(default=None, null=True, blank=True)
    ProjectURLCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
            'ProjectCorporation'
        ]
    }


class BuildingInfoChongqing(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectBaseName = fields.StringField(default='', max_length=1024, null=False)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    ProjectAddress = fields.StringField(default='', max_length=1024, null=False)
    ProjectCorporation = fields.StringField(default='', max_length=1024, null=False)
    BuildingRegName = fields.StringField(default='', max_length=1024, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                    binary=False, null=False)
    BuildingName = fields.StringField(default='', max_length=1024, null=False)
    BuildingZZHouseNum = fields.StringField(default='', max_length=1024, null=False)
    BuildingFZZHouseNum = fields.StringField(default='', max_length=1024, null=False)
    BuildingZZHouseNumSaling = fields.StringField(default='', max_length=1024, null=False)
    BuildingFZZHouseNumSaling = fields.StringField(default='', max_length=1024, null=False)
    BuildingRegHouseNum = fields.StringField(default='', max_length=1024, null=False)
    BuildingRegArea = fields.StringField(default='', max_length=1024, null=False)
    BuildingURL = fields.URLField(default=None, null=True, blank=True)
    BuildingURLCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectBaseName',
            'ProjectName',
            'ProjectUUID',
            'BuildingRegName',
            'BuildingUUID',
            'BuildingName',
        ]
    }


class HouseInfoChongqing(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    BuildingName = fields.StringField(default='', max_length=1024, null=False)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                    binary=False, null=False)
    HouseUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                 binary=False, null=False)
    HouseName = fields.StringField(default='', max_length=1024, null=False)
    HoueseID = fields.StringField(default='', max_length=1024, null=False)
    HoueseRegID = fields.StringField(default='', max_length=1024, null=False)
    HouseFloor = fields.StringField(default='', max_length=1024, null=False)
    HouseRoomNum = fields.StringField(default='', max_length=1024, null=False)
    HouseBuildingArea = fields.StringField(default='', max_length=1024, null=False)
    HouseInnerArea = fields.StringField(default='', max_length=1024, null=False)
    HouseShareArea = fields.StringField(default='', max_length=1024, null=False)
    HouseStructure = fields.StringField(default='', max_length=1024, null=False)
    HouseRoomType = fields.StringField(default='', max_length=1024, null=False)
    HouseUsage = fields.StringField(default='', max_length=1024, null=False)
    HouseSaleStateCode = fields.StringField(default='', max_length=1024, null=False)
    HouseSaleState = fields.StringField(default='', max_length=1024, null=False)
    HouseSaleStateLatest = fields.StringField(default='', max_length=1024, null=False)
    HouseInnerUnitPrice = fields.StringField(default='', max_length=1024, null=False)
    HouseBuildingUnitPrice = fields.StringField(default='', max_length=1024, null=False)
    HouseType = fields.StringField(default='', max_length=1024, null=False)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectName',
            'BuildingName',
            'ProjectUUID',
            'BuildingUUID',
            'HouseUUID',
            'HouseName'
        ]
    }


# Nanchang Model
class ProjectBaseNanchang(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    ProjectHouseSalingNum = fields.StringField(default='', max_length=1024, null=False)
    ProjectOtherSalingNum = fields.StringField(default='', max_length=1024, null=False)
    ProjectSalingArea = fields.StringField(default='', max_length=1024, null=False)
    ProjectAddress = fields.StringField(default='', max_length=1024, null=False)
    ProjectCompany = fields.StringField(default='', max_length=1024, null=False)
    ProjectURL = fields.URLField(default=None, null=True, blank=True)
    ProjectURLCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
        ]
    }


class ProjectInfoNanchang(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectCompany = fields.StringField(default='', max_length=1024, null=False)
    ProjectRegName = fields.StringField(default='', max_length=1024, null=False)
    ProjectSalePhone = fields.StringField(default='', max_length=1024, null=False)
    ProjectAddress = fields.StringField(default='', max_length=1024, null=False)
    ProjectUsage = fields.StringField(default='', max_length=1024, null=False)
    ProjectArea = fields.StringField(default='', max_length=1024, null=False)
    ProjectUseArea = fields.StringField(default='', max_length=1024, null=False)
    ProjectBuildArea = fields.StringField(default='', max_length=1024, null=False)
    ProjectRongjiRatio = fields.StringField(default='', max_length=1024, null=False)
    ProjectLvdiRatio = fields.StringField(default='', max_length=1024, null=False)
    ProjectBuildingRatio = fields.StringField(default='', max_length=1024, null=False)
    ProjectInvestment = fields.StringField(default='', max_length=1024, null=False)
    ProjectBuildDate = fields.StringField(default='', max_length=1024, null=False)
    ProjectCompleteDate = fields.StringField(default='', max_length=1024, null=False)
    ProjectBuildingCompany = fields.StringField(default='', max_length=1024, null=False)
    ProjectMeasureCompany = fields.StringField(default='', max_length=1024, null=False)
    ProjectSaleSum = fields.DictField(default={'null': ''}, null=False)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
        ]
    }


class BuildingInfoNanchang(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                    binary=False, null=False)
    BuildingName = fields.StringField(default='', max_length=1024, null=False)
    BuildingUsage = fields.StringField(default='', max_length=1024, null=False)
    BuildingStructure = fields.StringField(default='', max_length=1024, null=False)
    BuildingTotalFloor = fields.StringField(default='', max_length=1024, null=False)
    BuildingTotalArea = fields.StringField(default='', max_length=1024, null=False)
    BuildingSaleSum = fields.DictField(default={'null': ''}, null=False)
    BuildingURL = fields.URLField(default=None, null=True, blank=True)
    BuildingURLCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectName',
            'ProjectUUID',
            'BuildingUUID',
            'BuildingName',
        ]
    }


class HouseInfoNanchang(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    BuildingName = fields.StringField(default='', max_length=1024, null=False)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                    binary=False, null=False)
    HouseName = fields.StringField(default='', max_length=1024, null=False)
    HouseUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                 binary=False, null=False)
    HouseFloor = fields.StringField(default='', max_length=1024, null=False)
    HouseSaleState = fields.StringField(default='', max_length=1024, null=False)
    HouseSaleStateLatest = fields.StringField(default='', max_length=1024, null=False)
    HouseStructure = fields.StringField(default='', max_length=1024, null=False)
    HouseBuildingArea = fields.StringField(default='', max_length=1024, null=False)
    HouseInnerArea = fields.StringField(default='', max_length=1024, null=False)
    HouseShareArea = fields.StringField(default='', max_length=1024, null=False)
    HouseUsage = fields.StringField(default='', max_length=1024, null=False)
    HouseFloorAt = fields.StringField(default='', max_length=1024, null=False)
    HouseFloorTotal = fields.StringField(default='', max_length=1024, null=False)
    HousePreUnitPrice = fields.StringField(default='', max_length=1024, null=False)
    HouseStructureType = fields.StringField(default='', max_length=1024, null=False)
    HouseContract = fields.StringField(default='', max_length=1024, null=False)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectName',
            'BuildingName',
            'ProjectUUID',
            'BuildingUUID',
            'HouseUUID',
            'HouseName'
        ]
    }


class ProjectBaseNantong(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()))
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=255)  # 项目名称
    ReferencePrice = fields.StringField(default='', max_length=255)  # 参考价格
    OnSaleState = fields.StringField(default='', max_length=100, null=False)  # 楼盘状态/在售状态
    LandUse = fields.StringField(default='', max_length=255)  # 土地用途
    Developer = fields.StringField(default='', max_length=255)  # 开发商
    Selltel = fields.StringField(default='', max_length=100)  # 销售热线
    SourceUrl = fields.URLField(default=None, null=True, blank=True)  # 项目链接


class ProjectInfoNantong(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()))
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=255)  # 项目名称
    OnSaleState = fields.StringField(default='', max_length=100, null=False)  # 楼盘状态/在售状态
    LandUse = fields.StringField(default='', max_length=255)  # 土地用途
    RecordName = fields.StringField(default='', max_length=255)  # 备案名
    Decoration = fields.StringField(default='', max_length=255)  # 装修
    HousingCount = fields.StringField(default='', max_length=255)  # 规划户数
    Developer = fields.StringField(default='', max_length=255)  # 开发商
    DistrictName = fields.StringField(default='', max_length=255)  # 行政区
    ProjectAddress = fields.StringField(default='', max_length=255)  # 项目地址
    ApprovalPresaleAmount = fields.StringField(default='', max_length=255)  # 批准预售总套数
    HousingOnsoldAmount = fields.StringField(default='', max_length=255)  # 住宅可售套数
    ReferencePrice = fields.StringField(default='', max_length=255)  # 参考价格
    EarliestOpeningTime = fields.StringField(default='', max_length=255)  # 开盘时间
    LatestDeliversHouseDate = fields.StringField(default='', max_length=255)  # 交房时间
    FloorArea = fields.StringField(default='', max_length=100)  # 占地面积
    TotalBuidlingArea = fields.StringField(default='', max_length=100)  # 建筑面积
    FloorAreaRatio = fields.StringField(default='', max_length=100)  # 容积率
    GreeningRate = fields.StringField(default='', max_length=100)  # 绿化率
    ManagementFees = fields.StringField(default='', max_length=100)  # 物业费
    ManagementCompany = fields.StringField(default='', max_length=100)  # 物业公司
    BuildingType = fields.StringField(default='', max_length=100)  # 建筑类别
    ProjectSellAddress = fields.StringField(default='')  # 售楼地址
    SalesAgent = fields.StringField(default='')  # 销售代理
    ConstructionUnit = fields.StringField(default='')  # 施工单位
    ProjectIntro = fields.StringField(default='')  # 项目简介
    ProjectAroundSupporting = fields.StringField(default='')  # 周边配套
    TrafficSituation = fields.StringField(default='')  # 交通情况
    DecorationInfo = fields.StringField(default='')  # 装修情况
    DeveloperIntro = fields.StringField(default='')  # 开发商介绍
    AboutInfo = fields.StringField(default='')  # 相关信息
    SourceUrl = fields.URLField(default=None, null=True, blank=True)  # 项目详细URL
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
            'OnSaleState',
            'ApprovalPresaleAmount',
            'HousingOnsoldAmount',
            'ReferencePrice',
            'SourceUrl',
        ]
    }


class PresellInfoNantong(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()))
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    PresellUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=255)  # 项目名称
    PresalePermitNumber = fields.StringField(default='', max_length=255)  # 预售证编号
    ApprovalPresaleArea = fields.StringField(default='', max_length=255)  # 批准预售面积
    ApprovalPresaleBuildingName = fields.StringField(default='')  # 批准销售房层幢号
    Price = fields.StringField(default='')  # 房层价格
    LssueDate = fields.StringField(default='', max_length=255)  # 批准日期
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'PresellUUID',
            'ProjectName',
            'PresalePermitNumber',
        ]
    }


class BuildingInfoNantong(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(), binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()))
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=255)  # 项目名称
    PresalePermitNumber = fields.StringField(default='', max_length=255)  # 预售证编号
    BuildingName = fields.StringField(default='', max_length=255)  # 楼栋名
    SourceUrl = fields.URLField(default=None, null=True, blank=True)  # 楼栋销控表链接
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'BuildingUUID',
            'SourceUrl',
        ]
    }


class HouseInfoNantong(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(), binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()))
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    HouseUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=255)  # 项目名称
    BuildingName = fields.StringField(default='', max_length=255)  # 楼栋名称
    FloorName = fields.StringField(default='', max_length=255)  # 层名
    HouseNumber = fields.StringField(default='', max_length=255)  # 房号
    HouseState = fields.StringField(default='', max_length=255)  # 当前状态
    HouseStateLatest = fields.StringField(default='', max_length=255)  # 上次状态
    MeasuredBuildingArea = fields.StringField(default='', max_length=255)  # 建筑面积
    MeasuredInsideOfBuildingArea = fields.StringField(default='', max_length=255)  # 套内面积
    MeasuredSharedPublicArea = fields.StringField(default='', max_length=255)  # 公摊面积
    HouseUseType = fields.StringField(default='', max_length=255)  # 房屋功能/用途
    UnitShape = fields.StringField(default='', max_length=255)  # 户型
    TotalPrice = fields.StringField(default='', max_length=255)  # 总价
    SourceUrl = fields.URLField(default=None, null=True, blank=True)  # 户详细URL
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
            'BuildingUUID',
            'HouseUUID',
            'HouseState',
            'HouseStateLatest',
            'SourceUrl',
        ]
    }


class ProjectBaseQuanzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    ProjectURL = fields.StringField(default='', max_length=1024, null=False)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
        ]
    }


class ProjectInfoQuanzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectCompany = fields.StringField(default='', max_length=1024, null=False)
    ProjectAddress = fields.StringField(default='', max_length=1024, null=False)
    ProjectArea = fields.StringField(default='', max_length=1024, null=False)
    ProjectDistrict = fields.StringField(default='', max_length=1024, null=False)
    ProjectPhone = fields.StringField(default='', max_length=1024, null=False)
    ProjectPhoneConn = fields.StringField(default='', max_length=1024, null=False)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
        ]
    }


class BuildingInfoQuanzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    BuildingName = fields.StringField(default='', max_length=1024, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                    binary=False, null=False)
    BuildingRegName = fields.StringField(default='', max_length=1024, null=False)
    BuildingArea = fields.StringField(default='', max_length=1024, null=False)
    BuildingNum = fields.StringField(default='', max_length=1024, null=False)
    BuildingDistrict = fields.StringField(default='', max_length=1024, null=False)
    BuildingAddress = fields.StringField(default='', max_length=1024, null=False)
    BuildingBuildDate = fields.StringField(default='', max_length=1024, null=False)
    BuildingCompleteDate = fields.StringField(default='', max_length=1024, null=False)
    BuildingURL = fields.URLField(default=None, null=True, blank=True)
    BuildingURLCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectName',
            'ProjectUUID',
            'BuildingUUID',
            'BuildingName',
        ]
    }


class HouseInfoQuanzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    BuildingName = fields.StringField(default='', max_length=1024, null=False)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                    binary=False, null=False)
    HouseName = fields.StringField(default='', max_length=1024, null=False)
    HouseUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                 binary=False, null=False)
    HouseFloor = fields.StringField(default='', max_length=1024, null=False)
    HouseNum = fields.StringField(default='', max_length=1024, null=False)
    HouseStructure = fields.StringField(default='', max_length=1024, null=False)
    HouseUsage = fields.StringField(default='', max_length=1024, null=False)
    HouseBuildingArea = fields.StringField(default='', max_length=1024, null=False)
    HouseInnerArea = fields.StringField(default='', max_length=1024, null=False)
    HouseShareArea = fields.StringField(default='', max_length=1024, null=False)
    HouseSaleState = fields.StringField(default='', max_length=1024, null=False)
    HouseSaleStateLatest = fields.StringField(default='', max_length=1024, null=False)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectName',
            'BuildingName',
            'ProjectUUID',
            'BuildingUUID',
            'HouseUUID',
            'HouseName'
        ]
    }


class ProjectBaseJiujiang(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    ProjectDescription = fields.DynamicField(default='', null=False)
    ProjectURL = fields.URLField(default=None, null=True, blank=True)
    ProjectURLCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
        ]
    }


class ProjectInfoJiujiang(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectCompany = fields.StringField(default='', max_length=1024, null=False)
    ProjectAddress = fields.StringField(default='', max_length=1024, null=False)
    ProjectUsage = fields.StringField(default='', max_length=1024, null=False)
    ProjectArea = fields.StringField(default='', max_length=1024, null=False)
    ProjectBuildArea = fields.StringField(default='', max_length=1024, null=False)
    ProjectRongjiRatio = fields.StringField(default='', max_length=1024, null=False)
    ProjectLvdiRatio = fields.StringField(default='', max_length=1024, null=False)
    ProjectInvestment = fields.StringField(default='', max_length=1024, null=False)
    ProjectBuildDate = fields.StringField(default='', max_length=1024, null=False)
    ProjectBuildingCompany = fields.StringField(default='', max_length=1024, null=False)
    ProjectManageCompany = fields.StringField(default='', max_length=1024, null=False)
    ProjectDesignCompany = fields.StringField(default='', max_length=1024, null=False)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
        ]
    }


class BuildingInfoJiujiang(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    BuildingName = fields.StringField(default='', max_length=1024, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                    binary=False, null=False)
    BuildingRegName = fields.StringField(default='', max_length=1024, null=False)
    BuildingArea = fields.StringField(default='', max_length=1024, null=False)
    BuildingRegDate = fields.StringField(default='', max_length=1024, null=False)
    BuildingRegPrice = fields.StringField(default='', max_length=1024, null=False)
    BuildingSalingNum = fields.StringField(default='', max_length=1024, null=False)
    BuildingType = fields.StringField(default='', max_length=1024, null=False)
    BuildingSaleState = fields.StringField(default='', max_length=1024, null=False)
    BuildingSaleStateLatest = fields.StringField(default='', max_length=1024, null=False)
    BuildingPlanAreaCode = fields.StringField(default='', max_length=1024, null=False)
    BuildingPlanEngCode = fields.StringField(default='', max_length=1024, null=False)
    BuildingBuildEngCode = fields.StringField(default='', max_length=1024, null=False)
    BuildingAreaCode = fields.StringField(default='', max_length=1024, null=False)
    BuildingZZHouseNum = fields.StringField(default='', max_length=1024, null=False)
    BuildingFZZHouseNum = fields.StringField(default='', max_length=1024, null=False)
    BuildingSoldNum = fields.StringField(default='', max_length=1024, null=False)
    BuildingZZUnitPrice = fields.StringField(default='', max_length=1024, null=False)
    BuildingFZZUnitPrice = fields.StringField(default='', max_length=1024, null=False)
    BuildingURL = fields.URLField(default=None, null=True, blank=True)
    BuildingURLCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectName',
            'ProjectUUID',
            'BuildingUUID',
            'BuildingName',
        ]
    }


class HouseInfoJiujiang(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectName = fields.StringField(default='', max_length=1024, null=False)
    BuildingName = fields.StringField(default='', max_length=1024, null=False)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                    binary=False, null=False)
    HouseName = fields.StringField(default='', max_length=1024, null=False)
    HouseUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                 binary=False, null=False)
    HouseOSEQ = fields.StringField(default='', max_length=1024, null=False)
    HouseFloor = fields.StringField(default='', max_length=1024, null=False)
    HouseKey = fields.StringField(default='', max_length=1024, null=False)
    HouseSTR_2 = fields.StringField(default='', max_length=1024, null=False)
    HouseSTR_3 = fields.StringField(default='', max_length=1024, null=False)
    HouseSTR_5 = fields.StringField(default='', max_length=1024, null=False)
    HouseSattribute = fields.StringField(default='', max_length=1024, null=False)
    HouseBuildingArea = fields.StringField(default='', max_length=1024, null=False)
    HouseInnerArea = fields.StringField(default='', max_length=1024, null=False)
    HouseSaleState = fields.StringField(default='', max_length=1024, null=False)
    HouseSaleStateLatest = fields.StringField(default='', max_length=1024, null=False)
    HouseUnitPrice = fields.StringField(default='', max_length=1024, null=False)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectName',
            'BuildingName',
            'ProjectUUID',
            'BuildingUUID',
            'HouseUUID',
            'HouseName'
        ]
    }


# class ProjectCountInfoJiujiang(Document):
#     RecordID = fields.UUIDField(default=uuid.uuid1(),
#                                     binary=True, primary_key=True, null=False)
#     CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
#     ProjectSalingNum = fields.IntField(default=0, index=True)
#     ProjectSaledNum = fields.IntField(default=0, index=True)
#     meta = {
#         'indexes': [
#             'RecordID',
#             'CurTimeStamp',
#         ]
#     }
#
#
# class BuildingCountInfoJiujiang(Document):
#     RecordID = fields.UUIDField(default=uuid.uuid1(),
#                                     binary=True, primary_key=True, null=False)
#     CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
#     BuildingSalingNum = fields.IntField(default=0, index=True)
#     BuildingSaledNum = fields.IntField(default=0, index=True)
#     meta = {
#         'indexes': [
#             'RecordID',
#             'CurTimeStamp',
#         ]
#     }
#
#
# class HouseCountInfoJiujiang(Document):
#     RecordID = fields.UUIDField(default=uuid.uuid1(),
#                                     binary=True, primary_key=True, null=False)
#     CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
#     HouseUnavailableNum = fields.DictField(default={'dafault': 0, 'pledged': 0}, index=True)
#     HouseAvailableNum = fields.DictField(default={'dafault': 0, 'pledged': 0}, index=True)
#     HouseReserveNum = fields.DictField(default={'dafault': 0, 'pledged': 0}, index=True)
#     HouseContractNum = fields.DictField(default={'dafault': 0, 'pledged': 0}, index=True)
#     HouseRecordNum = fields.DictField(default={'dafault': 0, 'pledged': 0}, index=True)
#     HouseAuditNum = fields.DictField(default={'dafault': 0, 'pledged': 0}, index=True)
#     meta = {
#         'indexes': [
#             'RecordID',
#             'CurTimeStamp',
#         ]
#     }

class ProjectInfoGuangzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()))
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    ProjectID = fields.StringField(default='', null=False, max_length=255)
    ProjectName = fields.StringField(default='', max_length=255)  # 项目名称
    PresalePermitNumber = fields.StringField(default='', max_length=255)  # 预售证
    ProjectAddress = fields.StringField(default='', max_length=255)
    Developer = fields.StringField(default='', max_length=255)
    DistrictName = fields.StringField(default='', max_length=255)  # 行政区
    RegionName = fields.StringField(default='', max_length=255)  # 片区
    FloorArea = fields.StringField(default='', max_length=255)  # 占地面积
    TotalBuildingArea = fields.StringField(default='', max_length=255)  # 建筑面积
    QualificationNumber = fields.StringField(default='', max_length=255)
    HouseUseType = fields.StringField(default='', max_length=255)
    CertificateOfUseOfStateOwnedLand = fields.StringField(default='')  # 国土证
    ConstructionPermitNumber = fields.StringField(default='')  # 施工许可证
    BuildingPermit = fields.StringField(default='')  # 规划许可证
    ApprovalPresaleAmount = fields.StringField(default='', max_length=255)
    ApprovalPresaleArea = fields.StringField(default='', max_length=255)
    TotalSoldAmount = fields.StringField(default='', max_length=255)  # 已售总套数
    TotalSoldArea = fields.StringField(default='', max_length=255)  # 已售总套数
    TotalUnsoldAmount = fields.StringField(default='', max_length=255)  # 未售总套数
    TotalUnsoldArea = fields.StringField(default='', max_length=255)  # 未售总面积
    HousingTotalSoldAmount = fields.StringField(default='', max_length=255)  # 住宅累计已售套数
    HousingTotalSoldArea = fields.StringField(default='', max_length=255)  # 住宅累计已售面积
    HousingTotalSoldPrice = fields.StringField(default='', max_length=255)  # 住宅累计已售均价
    HousingUnsoldAmount = fields.StringField(default='', max_length=255)  # 住宅未售套数
    HousinglUnsoldArea = fields.StringField(default='', max_length=255)  # 住宅未售面积
    ShopTotalSoldAmount = fields.StringField(default='', max_length=255)  # 商业累计已售套数
    ShopTotalSoldArea = fields.StringField(default='', max_length=255)  # 商业累计已售面积
    ShopTotalSoldPrice = fields.StringField(default='', max_length=255)  # 商业累计已售均价
    ShopUnsoldAmount = fields.StringField(default='', max_length=255)  # 商业未售套数
    ShoplUnsoldArea = fields.StringField(default='', max_length=255)  # 商业未售面积
    OfficeTotalSoldAmount = fields.StringField(default='', max_length=255)  # 办公累计已售套数
    OfficeTotalSoldArea = fields.StringField(default='', max_length=255)  # 办公累计已售面积
    OfficeTotalSoldPrice = fields.StringField(default='', max_length=255)  # 办公累计已售均价
    OfficeUnsoldAmount = fields.StringField(default='', max_length=255)  # 办公未售套数
    OfficelUnsoldArea = fields.StringField(default='', max_length=255)  # 办公未售面积
    ParkingTotalSoldAmount = fields.StringField(default='', max_length=255)  # 车位累计已售套数
    ParkingTotalSoldArea = fields.StringField(default='', max_length=255)  # 车位累计已售面积
    ParkingTotalSoldPrice = fields.StringField(default='', max_length=255)  # 车位累计已售均价
    ParkingUnsoldAmount = fields.StringField(default='', max_length=255)  # 车位未售套数
    ParkinglUnsoldArea = fields.StringField(default='', max_length=255)  # 车位未售面积
    OtherTotalSoldAmount = fields.StringField(default='', max_length=255)  # 其他累计已售套数
    OtherTotalSoldArea = fields.StringField(default='', max_length=255)  # 其他累计已售面积
    OtherTotalSoldPrice = fields.StringField(default='', max_length=255)  # 其他累计已售均价
    OtherUnsoldAmount = fields.StringField(default='', max_length=255)  # 其他未售套数
    OtherlUnsoldArea = fields.StringField(default='', max_length=255)  # 其他未售面积
    HousingSoldAmount = fields.StringField(default='', max_length=255)  # 住宅当日已售套数
    HousingSoldArea = fields.StringField(default='', max_length=255)  # 住宅当日已售面积
    HousingCheckoutAmount = fields.StringField(default='', max_length=255)  # 住宅当日退房套数
    ShopSoldAmount = fields.StringField(default='', max_length=255)  # 商业当日已售套数
    ShopSoldArea = fields.StringField(default='', max_length=255)  # 商业当日已售面积
    ShopCheckoutAmount = fields.StringField(default='', max_length=255)  # 商业当日退房套数
    OfficeSoldAmount = fields.StringField(default='', max_length=255)  # 办公当日已售套数
    OfficeSoldArea = fields.StringField(default='', max_length=255)  # 办公当日已售面积
    OfficeCheckoutAmount = fields.StringField(default='', max_length=255)  # 办公当日退房套数
    ParkingSoldAmount = fields.StringField(default='', max_length=255)  # 车位当日已售套数
    ParkingSoldArea = fields.StringField(default='', max_length=255)  # 车位当日已售面积
    ParkingCheckoutAmount = fields.StringField(default='', max_length=255)  # 车位当日退房套数
    OtherSoldAmount = fields.StringField(default='', max_length=255)  # 其他当日已售套数
    OtherSoldArea = fields.StringField(default='', max_length=255)  # 其他当日已售面积
    OtherCheckoutAmount = fields.StringField(default='', max_length=255)  # 其他当日退房套数
    SourceUrl = fields.URLField(default=None, null=True, blank=True)  # 项目详细URL
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectID',
            'ProjectName',
            'PresalePermitNumber',
            'DistrictName',
            'RegionName',
            'ProjectAddress',
            'TotalSoldAmount',
            'TotalUnsoldAmount',
            'SourceUrl',
        ]
    }


class PresellInfoGuangzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(), binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()))
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    PresellUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    PresellID = fields.StringField(default='', null=False, max_length=255)
    ProjectID = fields.StringField(default='', null=False, max_length=255)
    ProjectName = fields.StringField(default='', max_length=255)
    PresalePermitNumber = fields.StringField(default='', max_length=255)
    PresaleBuildingAmount = fields.StringField(default='', max_length=255)
    ConstructionFloorCount = fields.StringField(default='', max_length=255)
    BuiltFloorCount = fields.StringField(default='', max_length=255)
    PeriodsCount = fields.StringField(default='', max_length=255)
    ConstructionTotalArea = fields.StringField(default='', max_length=255)
    GroundArea = fields.StringField(default='', max_length=255)
    UnderGroundArea = fields.StringField(default='', max_length=255)
    PresaleUnitCount = fields.StringField(default='', max_length=255)
    PresaleTotalBuildingArea = fields.StringField(default='', max_length=255)
    PresaleHousingLandIsMortgage = fields.StringField(default='', max_length=255)
    PresaleBuildingSupportingAreaInfo = fields.StringField(default='', max_length=255)
    LssueDate = fields.StringField(default='', max_length=255)
    LssuingAuthority = fields.StringField(default='', max_length=255)
    HouseSpread = fields.DictField(default={'null': True})  # 房屋分布
    Contacts = fields.StringField(default='', max_length=255)  # 联系人
    ValidityDateStartDate = fields.StringField(default='', max_length=255)  # 有效期自
    ValidityDateClosingDate = fields.StringField(default='', max_length=255)  # 有效期至
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'PresellUUID',
            'PresellID',
            'PresalePermitNumber',
        ]
    }


class BuildingInfoGuangzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(), binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()))
    ProjectID = fields.StringField(default='', null=False, max_length=255)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=255)
    BuildingID = fields.StringField(default='', max_length=255)  # 楼栋id
    BuildingName = fields.StringField(default='', max_length=255)  # 楼栋名
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectID',
            'ProjectUUID',
            'BuildingUUID',
            'BuildingID',
            'BuildingName',
        ]
    }


class HouseInfoGuangzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(), binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()))
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    HouseUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    HouseID = fields.StringField(default='', max_length=255)  # 户id
    ProjectName = fields.StringField(default='', max_length=255)  # 项目名称
    BuildingName = fields.StringField(default='', max_length=255)  # 楼栋名称
    HouseNumber = fields.StringField(default='', max_length=255)  # 房号
    HouseName = fields.StringField(default='', max_length=255)  # 名义房号
    HouseUseType = fields.StringField(default='', max_length=255)  # 房屋功能/用途
    ActualFloor = fields.StringField(default='', max_length=255)  # 实际层
    FloorName = fields.StringField(default='', max_length=255)  # 名义层
    FloorHight = fields.StringField(default='', max_length=255)  # 层高
    FloorCount = fields.StringField(default='', max_length=255)  # 层数/最高层?
    UnitShape = fields.StringField(default='', max_length=255)  # 户型
    IsPrivateUse = fields.StringField(default='', max_length=255)  # 是否自用
    IsSharedPublicMatching = fields.StringField(default='', max_length=255)  # 是否公建配套
    IsMoveBack = fields.StringField(default='', max_length=255)  # 是否回迁
    BuildingStructure = fields.StringField(default='', max_length=255)
    Balconys = fields.StringField(default='', max_length=255)
    UnenclosedBalconys = fields.StringField(default='', max_length=255)
    Kitchens = fields.StringField(default='', max_length=255)  # 阳台数量
    Toilets = fields.StringField(default='', max_length=255)  # 卫生间数量
    ForecastBuildingArea = fields.StringField(default='', max_length=255)  # 预测建筑面积
    ForecastInsideOfBuildingArea = fields.StringField(default='', max_length=255)  # 预测套内面积
    ForecastPublicArea = fields.StringField(default='', max_length=255)  # 预测公摊面积
    MeasuredBuildingArea = fields.StringField(default='', max_length=255)  # 实测建筑面积
    MeasuredInsideOfBuildingArea = fields.StringField(default='', max_length=255)  # 实测套内面积
    MeasuredSharedPublicArea = fields.StringField(default='', max_length=255)  # 实测公摊面积
    IsMortgage = fields.StringField(default='', max_length=255)  # 是否抵押
    IsAttachment = fields.StringField(default='', max_length=255)  # 是否查封
    HouseState = fields.StringField(default='', max_length=255)  # 当前状态
    HouseStateLatest = fields.StringField(default='', max_length=255)  # 上次状态
    HouseLabel = fields.StringField(default='', max_length=255)  # 当前标签
    HouseLabelLatest = fields.StringField(default='', max_length=255)  # 上次标签
    SourceUrl = fields.URLField(default=None, null=True, blank=True)  # 户详细URL
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
            'BuildingUUID',
            'BuildingName',
            'HouseUUID',
            'HouseID',
            'HouseNumber',
            'HouseUseType',
            'ForecastBuildingArea',
            'ForecastInsideOfBuildingArea',
            'ForecastPublicArea',
            'MeasuredBuildingArea',
            'MeasuredInsideOfBuildingArea',
            'MeasuredSharedPublicArea',
            'HouseState',
            'HouseStateLatest',
            'HouseLabel',
            'HouseLabelLatest',
            'SourceUrl',
        ]
    }


class PermitInfoGuangzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(), binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()))
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    ProjectID = fields.StringField(default='', null=False, max_length=255)
    PermitUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=255)
    PermitType = fields.StringField(null=False, max_length=255)
    Content = fields.DictField(default={'null': True}, null=False)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectID',
            'PermitUUID',
            'ProjectName',
            'PermitType',
        ]
    }


class ProjectBaseQingdao(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    ProjectID = fields.StringField(default='', max_length=100, index=True, null=False)  # 项目id
    DistrictName = fields.StringField(default='', max_length=50, null=False)  # 行政区
    ProjectName = fields.StringField(default='', max_length=100, null=False)  # 楼盘名称
    ProjectAddress = fields.StringField(default='', max_length=100, null=False)  # 楼盘地址
    Developer = fields.StringField(default='', max_length=100, null=False)  # 开发商
    OnSaleState = fields.StringField(default='', max_length=20, null=False)  # 销售状态
    HousingAmount = fields.StringField(default='', max_length=100, null=False)  # 住宅套数
    HousingArea = fields.StringField(default='', max_length=100, null=False)  # 住宅面积
    TotalAmount = fields.StringField(default='', max_length=100, null=False)  # 总套数
    TotalArea = fields.StringField(default='', max_length=100, null=False)  # 总面积
    HousingOnsoldAmount = fields.StringField(default='', max_length=100, null=False)  # 可售住宅套数
    HousingOnsoldArea = fields.StringField(default='', max_length=100, null=False)  # 可售住宅面积
    TotalOnsoldAmount = fields.StringField(default='', max_length=100, null=False)  # 可售总套数
    TotalOnsoldArea = fields.StringField(default='', max_length=100, null=False)  # 可售总面积
    BookingHousingAmount = fields.StringField(default='', max_length=100, null=False)  # 预定住宅套数
    BookingHousingArea = fields.StringField(default='', max_length=100, null=False)  # 预定住宅面积
    TotalBookingAmount = fields.StringField(default='', max_length=100, null=False)  # 预定总套数
    TotalBookingArea = fields.StringField(default='', max_length=100, null=False)  # 预定总面积
    HousingSoldAmount = fields.StringField(default='', max_length=100, null=False)  # 已售住宅套数
    HousingSoldArea = fields.StringField(default='', max_length=100, null=False)  # 已售住宅面积
    TotalSoldAmount = fields.StringField(default='', max_length=100, null=False)  # 已售总套数
    TotalSoldArea = fields.StringField(default='', max_length=100, null=False)  # 已售总面积
    RegisterHousingAmount = fields.StringField(default='', max_length=100, null=False)  # 已登记住宅套数
    RegisterHousingArea = fields.StringField(default='', max_length=100, null=False)  # 已登记住宅面积
    TotalRegisterAmount = fields.StringField(default='', max_length=100, null=False)  # 已登记总套数
    TotalRegisterArea = fields.StringField(default='', max_length=100, null=False)  # 已登记总面积
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectID',
            'DistrictName',
            'ProjectName',
            'OnSaleState',
            'HousingAmount',
            'HousingArea',
            'TotalAmount',
            'TotalArea',
        ]
    }


class PresellInfoQingdao(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(), binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    PresellUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    PresellID = fields.StringField(default='', index=True, max_length=100, null=False)  # 预售证id
    ProjectName = fields.StringField(default='', max_length=100, null=False)  # 楼盘名称
    PresalePermitNumber = fields.StringField(default='', max_length=100, null=False)  # 预售证编号
    PresalePermitName = fields.StringField(default='', max_length=100, null=False)  # 预售许可证
    EarliestOpeningDate = fields.StringField(default='', max_length=100, null=False)  # 开盘日期
    SellAddress = fields.StringField(default='', max_length=200, null=False)  # 售楼地址
    SellTel = fields.StringField(default='', max_length=100, null=False)  # 售楼电话
    TotalAmount = fields.StringField(default='', max_length=100, null=False)  # 总套数
    TotalArea = fields.StringField(default='', max_length=100, null=False)  # 总面积
    OnsoldAmount = fields.StringField(default='', max_length=100, null=False)  # 可售总套数
    OnsoldArea = fields.StringField(default='', max_length=100, null=False)  # 可售总面积
    SoldAmount = fields.StringField(default='', max_length=100, null=False)  # 已售总套数
    SoldArea = fields.StringField(default='', max_length=100, null=False)  # 已售总面积
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'PresellUUID',
            'PresellID',
            'ProjectName',
            'PresalePermitNumber',
            'PresalePermitName',
            'TotalAmount',
            'TotalArea',
            'OnsoldAmount',
            'OnsoldArea',
            'SoldAmount',
            'SoldArea',
        ]
    }


class BuildingInfoQingdao(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(), binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    PresellUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=100, null=False)  # 楼盘名称
    PresalePermitName = fields.StringField(default='', max_length=100, null=False)  # 预售许可证
    BuildingID = fields.StringField(default='', max_length=100, index=True, null=False)  # 楼栋id
    BuildingName = fields.StringField(default='', max_length=100)  # 楼栋名
    BuildingReferencePrice = fields.StringField(default='', max_length=100)  # 参考价格
    BuildingFloatingRange = fields.StringField(default='', max_length=100)  # 可浮动幅度
    OnsoldAmount = fields.StringField(default='', max_length=100)  # 可售套数
    BookingAmount = fields.StringField(default='', max_length=100)  # 预定套数
    TotalAmount = fields.StringField(default='', max_length=100)  # 总套数
    BuildingURL = fields.URLField(default=None, null=True, blank=True)  # 一房一价地址
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'PresellUUID',
            'BuildingUUID',
            'BuildingID',
            'BuildingURL',
            'ProjectName',
            'PresalePermitName',
            'BuildingName',
        ]
    }


class HouseInfoQingdao(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    PresellUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    HouseUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False,
                                 null=False)  # BuildingUUID+实际层+在页面上的列数 生成唯一id
    ProjectName = fields.StringField(default='', max_length=100, null=False)  # 楼盘名称
    PresalePermitName = fields.StringField(default='', max_length=100, null=False)  # 预售许可证
    BuildingName = fields.StringField(default='', max_length=100)  # 楼栋名
    HouseID = fields.StringField(default='', max_length=100, index=True, null=False)  # 房间id
    FloorName = fields.StringField(default='', max_length=100, null=False)  # 名义层
    ActualFloor = fields.StringField(default='', max_length=100, null=False)  # 实际层
    HouseName = fields.StringField(default='', max_length=100, index=True)  # 房间号
    HouseUseType = fields.StringField(default='', max_length=100)  # 房屋类型
    HouseUnitShape = fields.StringField(default='', max_length=100)  # 房型
    ForecastBuildingArea = fields.StringField(default='')  # 预测面积
    MeasuredBuildingArea = fields.StringField(default='')  # 实测面积
    ForecastInsideOfBuildingArea = fields.StringField(default='')  # 预测套内面积
    MeasuredInsideOfBuildingArea = fields.StringField(default='')  # 实测套内面积
    ForecastPublicArea = fields.StringField(default='')  # 预测分摊面积
    MeasuredSharedPublicArea = fields.StringField(default='')  # 实测分摊面积
    ForecastUndergroundArea = fields.StringField(default='')  # 预测地下面积
    MeasuredUndergroundArea = fields.StringField(default='')  # 实测地下面积
    HouseReferencePrice = fields.StringField(default='')  # 参考价格
    HouseState = fields.StringField(default='', max_length=100, null=False)  # 状态
    HouseStateLatest = fields.StringField(default='', max_length=255)  # 上次状态
    SourceUrl = fields.URLField(default=None, null=True, blank=True)  # 户详情地址
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'PresellUUID',
            'BuildingUUID',
            'HouseUUID',
            'SourceUrl',
            'ProjectName',
            'PresalePermitName',
            'BuildingName',
            'HouseName',
            'HouseUseType',
            'HouseState',
            'HouseStateLatest',
            'HouseUnitShape',
        ]
    }


def set_field(kind, empty=False, key=False, choice=False):
    '''
    primary_key#zhujian;   choices#kexuanshuxing; binary#erjinzhi;  null#feikong; index#suoyin
    '''
    if kind == "string":

        return fields.StringField(default='', null=empty, primary_key=key, choices=choice)

    elif kind == "int":

        return fields.IntField(default=0, null=True, primary_key=key, choices=choice)

    elif kind == 'url':

        return fields.URLField(default=None, null=True, blank=True, primary_key=key, choices=choice)

    elif kind == 'uuid1':

        return fields.UUIDField(default=uuid.uuid1(), binary=True, primary_key=key, null=empty, choices=choice)

    elif kind == 'uuid3':

        return fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=empty, primary_key=key,
                                choices=choice)

    elif kind == 'time':

        return fields.StringField(default=str(datetime.datetime.now()), index=True)

    elif kind == 'day':

        return fields.StringField(default=time.strftime("%Y-%m-%d", time.localtime()), index=True)

    elif kind == 'string':

        return fields.TextField(default='', null=empty, primary_key=key, choices=choice)


class ProjectDetailFoshan(Document):
    RecordID = set_field(kind='uuid1', key=True)
    RecordTime = set_field(kind='time')
    CheackTimeLatest = set_field(kind='time')
    ProjectUUID = set_field(kind='uuid3')
    RealEstateProjectID = set_field(kind='string')
    ProjectUrl = set_field(kind='url')
    SourceUrl = set_field(kind='url')

    AveragePrice = set_field(kind='string')  # 均价
    ProjectName = set_field(kind='string')
    ProjectAddress = set_field(kind='string')  # 惠州市惠城区金山大道与三环南路交汇处
    Developer = set_field(kind='string')  # 发展商

    FloorAreaRatio = set_field(kind='string')  # 容积率
    DistrictName = set_field(kind='string')  # 行政区
    ManagementFees = set_field(kind='string')  # 物业费
    ManagementCompany = set_field(kind='string')  # 物业公司
    TotalBuidlingArea = set_field(kind='string')  # 总建筑面积

    HouseSoldAmount = set_field(kind='string')  # 已售套数
    HouseUnsoldAmount = set_field(kind='string')  # 未售套数
    DeveloperLevel = set_field(kind='string')  # 资质等级
    DeveloperPermitNumber = set_field(kind='string')  # 开发商资质证书

    SaleTelphoneNumber = set_field(kind='string')  # 销售电话

    meta = {
        'indexes': [
            'RecordTime',
            'ProjectUUID',
            'ProjectName',

        ]
    }


class BuildingDetailFoshan(Document):
    RecordID = set_field(kind='uuid1', key=True)
    RecordTime = set_field(kind='time')
    CheackTimeLatest = set_field(kind='time')
    RecordDay = set_field(kind='day')
    BuildingUrl = set_field(kind='string')
    SourceUrl = set_field(kind='string')

    ProjectName = set_field(kind='string')
    RealEstateProjectID = set_field(kind='string')
    ProjectUUID = set_field(kind='uuid3')

    RegionName = set_field(kind='string')

    BuildingID = set_field(kind='string')
    BuildingUUID = set_field(kind='uuid3')
    BuildingName = set_field(kind='string')

    meta = {
        'indexes': [
            'RecordTime',
            'ProjectUUID',
            'BuildingUUID',
            'RecordTime'
        ]
    }


class HouseDetailFoshan(Document):
    RecordID = set_field(kind='uuid1', key=True)
    RecordTime = set_field(kind='time')
    RecordDay = set_field(kind='day')
    CheackTimeLatest = set_field(kind='time')

    ProjectUUID = set_field(kind='uuid3')
    BuildingUUID = set_field(kind='uuid3')
    HouseUUID = set_field(kind='uuid3')

    ProjectName = set_field(kind='string')
    BuildingName = set_field(kind='string')
    UnitName = set_field(kind='string')

    HouseUseType = set_field(kind='string')  # 用途
    HouseID = set_field(kind='string')
    HouseUrl = set_field(kind='string')
    SourceUrl = set_field(kind='string')

    RegionName = set_field(kind='string')  # 区域
    FloorName = set_field(kind='string')  # 层名
    HouseName = set_field(kind='string')
    HouseSaleState = set_field(kind='string')  # 销售状态
    HouseNature = set_field(kind='string')  # 房屋性质
    HouseType = set_field(kind='string')  # 房屋类型

    BalconyType = set_field(kind='string')  #
    MeasuredBuildingArea = set_field(kind='string')  # 实测建筑面积
    MeasuredInsideOfBuildingArea = set_field(kind='string')  # 实测套内面积
    MeasuredSharedPublicArea = set_field(kind='string')  # 实测公摊面积
    ForecastBuildingArea = set_field(kind='string')  # 预测建筑面积
    ForecastInsideOfBuildingArea = set_field(kind='string')  # 预测套内面积
    ForecastPublicArea = set_field(kind='string')  # 预测公摊面积
    IsMortgage = set_field(kind='string')  # 是否抵押
    IsAttachment = set_field(kind='string')  # 是否查封
    Adress = set_field(kind='string')  # 地址
    TotalPrice = set_field(kind='string')  # 总价
    HouseSaleStateLatest = set_field(kind='string')
    ComplateTag = set_field(kind='int')

    meta = {
        'indexes': [
            "ProjectUUID",
            'ComplateTag',
            'RecordTime',
            'HouseSaleStateLatest',
            'CheackTimeLatest',
            # "BuildingUUID",
            'RecordTime',
            'HouseUUID',
            'HouseSaleState'
        ]
    }


class CertificateDetailFoshan(Document):
    RecordID = set_field(kind='uuid1', key=True)
    RecordTime = set_field(kind='time')
    PresalePermitUrl = set_field(kind='string')
    SourceUrl = set_field(kind='string')
    CheackTimeLatest = set_field(kind='time')
    ProjectUUID = set_field(kind='uuid3')
    ProjectName = set_field(kind='string')
    RealEstateProjectID = set_field(kind='string')

    PresalePermitNumber = set_field(kind='string')  # 预售证编号
    PresalePermitNumberID = set_field(kind='string')  # 预售证编号
    PresalePermitNumberUUID = set_field(kind='uuid3')

    LssuingAuthority = set_field(kind='string')  # 发证机关
    PresaleTotalBuidlingArea = set_field(kind='string')  # 预售总建筑面积
    ValidityDateStartDate = set_field(kind='string')  # 有效期起始日期
    ValidityDateClosingDate = set_field(kind='string')  # 有效期截止日期
    LssueDate = set_field(kind='string')  # 发证日期
    Bank_Account = set_field(kind='string')  # 预售款专用帐户
    Bank = set_field(kind='string')  # 开户银行
    LivingArea = set_field(kind='string')  # 住宅面积
    BusinessArea = set_field(kind='string')  # 商业用房面积
    OtherArea = set_field(kind='string')  # 其它面积
    LivingCount = set_field(kind='string')  # 住宅套数
    BusinessCount = set_field(kind='string')  # 商业套数
    OtherCount = set_field(kind='string')  # 其它套数

    PresaleHouseCount = set_field(kind='string')  # 本期总单元套数
    PresaleBuildingNo = set_field(kind='string')  # 预售房屋栋号及层数

    meta = {
        'indexes': [
            'RecordTime',
            'PresalePermitNumberUUID',
            'ProjectUUID',
            'PresalePermitNumber',

        ]
    }


class WebCountFoshan(Document):
    RecordID = set_field(kind='uuid1', key=True)  # 记录id
    RecordTime = set_field(kind='time')  # 记录时间
    CheackTimeLatest = set_field(kind='time')  # 时间

    riqi = set_field(kind='string')
    quanshi_zhuzhai_taoshu = set_field(kind='string')
    quanshi_zhuzhai_mianji = set_field(kind='string')
    quanshi_shangye_taoshu = set_field(kind='string')
    quanshi_shangye_mianji = set_field(kind='string')
    quanshi_qita_taoshu = set_field(kind='string')
    quanshi_qita_mianji = set_field(kind='string')

    chancheng_zhuzhai_taoshu = set_field(kind='string')
    chancheng_zhuzhai_mianji = set_field(kind='string')
    chancheng_shangye_taoshu = set_field(kind='string')
    chancheng_shangye_mianji = set_field(kind='string')
    chancheng_qita_taoshu = set_field(kind='string')
    chancheng_qita_mianji = set_field(kind='string')

    nanhan_zhuzhai_taoshu = set_field(kind='string')
    nanhan_zhuzhai_mianji = set_field(kind='string')
    nanhan_shangye_taoshu = set_field(kind='string')
    nanhan_shangye_mianji = set_field(kind='string')
    nanhan_qita_taoshu = set_field(kind='string')
    nanhan_qita_mianji = set_field(kind='string')

    shunde_zhuzhai_taoshu = set_field(kind='string')
    shunde_zhuzhai_mianji = set_field(kind='string')
    shunde_shangye_taoshu = set_field(kind='string')
    shunde_shangye_mianji = set_field(kind='string')
    shunde_qita_taoshu = set_field(kind='string')
    shunde_qita_mianji = set_field(kind='string')

    gaoming_zhuzhai_taoshu = set_field(kind='string')
    gaoming_zhuzhai_mianji = set_field(kind='string')
    gaoming_shangye_taoshu = set_field(kind='string')
    gaoming_shangye_mianji = set_field(kind='string')
    gaoming_qita_taoshu = set_field(kind='string')
    gaoming_qita_mianji = set_field(kind='string')

    sanshui_zhuzhai_taoshu = set_field(kind='string')
    sanshui_zhuzhai_mianji = set_field(kind='string')
    sanshui_shangye_taoshu = set_field(kind='string')
    sanshui_shangye_mianji = set_field(kind='string')
    sanshui_qita_taoshu = set_field(kind='string')
    sanshui_qita_mianji = set_field(kind='string')


class ProjectBaseShanghai(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    project_id = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                  binary=False, null=False)
    project_sts = fields.StringField(default='', max_length=255, null=False)

    project_addr = fields.StringField(default='', max_length=255, null=False)
    project_house_num = fields.StringField(default='', max_length=255, null=False)
    project_house_area = fields.StringField(default='', max_length=255, null=False)
    project_no = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                  binary=False, null=False)
    project_name = fields.StringField(default='', max_length=255, null=False)
    project_county = fields.StringField(default='', max_length=255, null=False)
    project_blank = fields.StringField(default='', max_length=255, null=False)
    project_com_name = fields.StringField(default='', max_length=255, null=False)

    project_price = fields.StringField(default='', max_length=255, null=False)
    project_price_house = fields.StringField(default='', max_length=255, null=False)
    project_price_back = fields.StringField(default='', max_length=255, null=False)
    project_price_house_back = fields.StringField(default='', max_length=255, null=False)
    project_detail_link = fields.StringField(default='', max_length=510, null=False)
    change_data = fields.StringField(default='', max_length=1024, null=False)

    NewCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'NewCurTimeStamp',
            'project_detail_link',
            'change_data',
            'project_id',
            'project_no',

        ]
    }


class OpeningunitBaseShanghai(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    project_no = fields.StringField(default='', max_length=255, null=False)
    project_name = fields.StringField(default='', max_length=255, null=False)
    opening_unit_no = fields.StringField(default='', max_length=255, null=False)
    opening_building_detail_link = fields.StringField(default='', max_length=510, null=False)
    opening_unit_licence = fields.StringField(default='', max_length=255, null=False)
    opening_unit_opendate = fields.StringField(default='', max_length=255, null=False)
    opening_unit_num = fields.StringField(default='', max_length=255, null=False)
    opening_unit_housenum = fields.StringField(default='', max_length=255, null=False)
    opening_unit_area = fields.StringField(default='', max_length=255, null=False)
    opening_unit_housearea = fields.StringField(default='', max_length=255, null=False)
    opening_unit_sts = fields.StringField(default='', max_length=255, null=False)
    change_data = fields.StringField(default='', max_length=1024, null=False)
    NewCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'NewCurTimeStamp',
            'opening_unit_sts',
            'change_data',
            'project_no',
            'opening_unit_no',
        ]
    }


class BuildingBaseShanghai(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    project_no = fields.StringField(default='', max_length=255, null=False)
    project_name = fields.StringField(default='', max_length=255, null=False)
    opening_unit_no = fields.StringField(default='', max_length=255, null=False)
    building_name = fields.StringField(default='', max_length=255, null=False)
    building_no = fields.StringField(default='', max_length=255, null=False)
    building_price = fields.StringField(default='', max_length=255, null=False)
    building_fluctuation = fields.StringField(default='', max_length=255, null=False)
    building_num = fields.StringField(default='', max_length=255, null=False)
    building_area = fields.StringField(default='', max_length=255, null=False)
    building_sts = fields.StringField(default='', max_length=255, null=False)
    change_data = fields.StringField(default='', max_length=1023, null=False)
    building_url = fields.URLField(default=None, null=True, blank=True)
    NewCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'NewCurTimeStamp',
            'change_data',
            'project_no',
            'building_sts',
            'opening_unit_no',
            'building_no',

        ]
    }


class HouseBaseShanghai(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    project_name = fields.StringField(default='', max_length=255, null=False)
    project_no = fields.StringField(default='', max_length=255, null=False)
    opening_unit_no = fields.StringField(default='', max_length=255, null=False)
    building_no = fields.StringField(default='', max_length=255, null=False)
    house_no = fields.StringField(default='', max_length=255, null=False)
    house_floor = fields.StringField(default='', max_length=255, null=False)
    house_num = fields.StringField(default='', max_length=255, null=False)
    house_class = fields.StringField(default='', max_length=255, null=False)
    house_use_type = fields.StringField(default='', max_length=255, null=False)
    house_layout = fields.StringField(default='', max_length=255, null=False)
    house_area_pr_yc = fields.StringField(default='', max_length=510, null=False)
    house_area_pr_tn = fields.StringField(default='', max_length=255, null=False)
    house_area_pr_ft = fields.StringField(default='', max_length=255, null=False)
    house_area_pr_dx = fields.StringField(default='', max_length=255, null=False)
    house_area_real_yc = fields.StringField(default='', max_length=255, null=False)
    house_area_real_tn = fields.StringField(default='', max_length=255, null=False)
    house_area_real_ft = fields.StringField(default='', max_length=255, null=False)
    house_area_real_dx = fields.StringField(default='', max_length=255, null=False)
    house_sts = fields.StringField(default='', max_length=255, null=False)
    change_data = fields.StringField(default='', max_length=1023, null=False)
    house_stsLatest = fields.StringField(default='', max_length=255, null=False)
    NewCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'NewCurTimeStamp',
            'house_stsLatest',
            'house_sts',
            'change_data',
            'project_no',
            'opening_unit_no',
            'building_no',
            'house_no',
        ]
    }


class SearchProjectBaseFuzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)

    SearchProjectuuid = fields.StringField(default='', max_length=255, null=False)

    Presalelicensenumber = fields.StringField(default='', max_length=255, null=False)
    Projectname = fields.StringField(default='', max_length=255, null=False)
    Permittedarea = fields.StringField(default='', max_length=255, null=False)
    Presalebuildingno = fields.StringField(default='', max_length=255, null=False)
    Approvaldate = fields.StringField(default='', max_length=255, null=False)
    Planenddate = fields.StringField(default='', max_length=255, null=False)
    NewCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    change_data = fields.StringField(default='', max_length=1023, null=False)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'SearchProjectuuid',
            'change_data',

        ]
    }


class ProjectinfoBaseFuzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)

    projectuuid = fields.StringField(default='', max_length=255, null=False)
    Projectname = fields.StringField(default='', max_length=255, null=False)

    projectcounty = fields.StringField(default='', max_length=255, null=False)
    projectcomname = fields.StringField(default='', max_length=255, null=False)
    projectaddr = fields.StringField(default='', max_length=255, null=False)
    totalnum = fields.IntField(default=0, null=False)
    totalareas = fields.IntField(default=0, null=False)
    totalhousenum = fields.IntField(default=0, null=False)
    totalhouseareas = fields.IntField(default=0, null=False)
    cansalenum = fields.IntField(default=0, null=False)
    cansaleareas = fields.IntField(default=0, null=False)
    cansalehousenum = fields.IntField(default=0, null=False)
    cansalehouseareas = fields.IntField(default=0, null=False)
    prebuynum = fields.IntField(default=0, null=False)
    prebuyareas = fields.IntField(default=0, null=False)
    prebuyhousenum = fields.IntField(default=0, null=False)
    prebuyhouseareas = fields.IntField(default=0, null=False)
    salednum = fields.IntField(default=0, null=False)
    saledareas = fields.IntField(default=0, null=False)
    saledhousenum = fields.IntField(default=0, null=False)
    saledhouseareas = fields.IntField(default=0, null=False)
    registerednum = fields.IntField(default=0, null=False)
    registeredareas = fields.IntField(default=0, null=False)
    registeredhousenum = fields.IntField(default=0, null=False)
    registeredhouseareas = fields.IntField(default=0, null=False)

    projectprice = fields.StringField(default='', max_length=255, null=False)
    projectpricehouse = fields.StringField(default='', max_length=255, null=False)
    projectpriceback = fields.StringField(default='', max_length=255, null=False)
    projectpricehouseback = fields.StringField(default='', max_length=255, null=False)
    change_data = fields.StringField(default='', max_length=1023, null=False)
    NewCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ApprovalUrl = fields.StringField(default='', max_length=1023, null=False)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'Projectname',
            'change_data',
            'projectuuid',
        ]
    }


class ApprovalBaseFuzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    projectno = fields.StringField(default='', max_length=255, null=False)
    projectname = fields.StringField(default='', max_length=255, null=False)
    Approvalno = fields.StringField(default='', max_length=255, null=False)
    Supervisionno = fields.StringField(default='', max_length=255, null=False)
    Supervisionbank = fields.StringField(default='', max_length=255, null=False)
    Approvaldate = fields.StringField(default='', max_length=255, null=False)
    Totalnum = fields.IntField(default=0, null=False)
    Totalhousenum = fields.IntField(default=0, null=False)
    Totalareas = fields.FloatField(default=0.00, max_digits=10, decimal_places=2)
    Totalhouseareas = fields.FloatField(default=0.00, max_digits=10, decimal_places=2)

    change_data = fields.StringField(default='', max_length=1023, null=False)
    NewCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'Approvalno',
        ]
    }


class BuildingBaseFuzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    projectno = fields.StringField(default='', max_length=255, null=False)
    projectname = fields.StringField(default='', max_length=255, null=False)

    Approvalno = fields.StringField(default='', max_length=255, null=False)
    buildingname = fields.StringField(default='', max_length=255, null=False)
    buildingno = fields.StringField(default='', max_length=255, null=False)
    buildingtotalnum = fields.IntField(default=0, null=False)
    buildingtotalareas = fields.FloatField(default=0.00, max_digits=10, decimal_places=2)
    buildinghousenum = fields.IntField(default=0, null=False)
    buildinghouseareas = fields.FloatField(default=0.00, max_digits=10, decimal_places=2)
    NewCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    change_data = fields.StringField(default='', max_length=1023, null=False)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'projectno',
            'Approvalno',
            'buildingno',
        ]
    }


class HouseBaseFuzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    project_no = fields.StringField(default='', max_length=255, null=False)
    project_name = fields.StringField(default='', max_length=1020, null=False)
    Approvalno = fields.StringField(default='', max_length=255, null=False)
    building_no = fields.StringField(default='', max_length=255, null=False)
    building_name = fields.StringField(default='', max_length=255, null=False)
    house_no = fields.StringField(default='', max_length=255, null=False)
    house_floor = fields.StringField(default='', max_length=255, null=False)
    house_num = fields.StringField(default='', max_length=255, null=False)
    house_class = fields.StringField(default='', max_length=255, null=False)
    house_use_type = fields.StringField(default='', max_length=255, null=False)
    house_layout = fields.StringField(default='', max_length=255, null=False)
    house_area_pr_yc = fields.StringField(default='', max_length=510, null=False)
    house_area_pr_tn = fields.StringField(default='', max_length=255, null=False)
    house_area_pr_ft = fields.StringField(default='', max_length=255, null=False)
    house_area_pr_dx = fields.StringField(default='', max_length=255, null=False)
    house_area_real_yc = fields.StringField(default='', max_length=255, null=False)
    house_area_real_tn = fields.StringField(default='', max_length=255, null=False)
    house_area_real_ft = fields.StringField(default='', max_length=255, null=False)
    house_area_real_dx = fields.StringField(default='', max_length=255, null=False)
    house_sts = fields.StringField(default='', max_length=255, null=False)
    change_data = fields.StringField(default='', max_length=1023, null=False)

    house_stsLatest = fields.StringField(default='', max_length=255, null=False)
    NewCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'project_no',  # 项目编号
            'Approvalno',  # 开盘单元编号
            'building_no',  # 楼栋编号
            'house_no',  # 房间编号
        ]
    }


class MonitorProjectBaseWuxi(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    NewCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    change_data = fields.StringField(default='', max_length=10240, null=False)
    ProjectNo = fields.StringField(default='', max_length=255, null=False)
    ProjectName = fields.StringField(default='', max_length=255, null=False)
    TotalHouseNumber = fields.StringField(default='', max_length=255, )
    OnSoldNumber = fields.StringField(default='', max_length=255, )
    PresalePermitNumber = fields.StringField(default='', max_length=255, )
    ProjectCode = fields.StringField(default='', max_length=255, )
    projectDetailUrl = fields.URLField(default=None, blank=True)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'change_data',
            'ProjectNo',
            'ProjectCode'
        ]
    }


class ProjectBaseWuxi(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    NewCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    change_data = fields.StringField(default='', max_length=10240, null=False)
    ProjectNo = fields.StringField(default='', max_length=255, null=False)
    TotalHouseNumber = fields.StringField(default='', max_length=255, )
    OnSoldNumber = fields.StringField(default='', max_length=255, )
    SoldNumber = fields.StringField(default='', max_length=255, )
    LimitSoldNumber = fields.StringField(default='', max_length=255, )
    ProjectName = fields.StringField(default='', max_length=255, )
    PresalePermitNumber = fields.StringField(default='', max_length=255, )
    ProjectTemporaryName = fields.StringField(default='', max_length=255, )
    ApprovalPresaleDepartment = fields.StringField(default='', max_length=255, )
    Developer = fields.StringField(default='', max_length=255, )
    DeveloperUrl = fields.StringField(default='', max_length=255, )
    Cooperator = fields.StringField(default='', max_length=255, )
    ProjectAddress = fields.StringField(default='', max_length=255, )
    DistrictName = fields.StringField(default='', max_length=255, )
    ApprovalForApproval = fields.StringField(default='', max_length=255, )
    UsePermitNumber = fields.StringField(default='', max_length=255, )
    OwnedLand = fields.StringField(default='', max_length=255, )
    ConstructionPermitNumber = fields.StringField(default='', max_length=255, )
    CertificateOfUseOfStateOwnedLand = fields.StringField(default='', max_length=255, )
    PreSaleAreas = fields.StringField(default='', max_length=255, )
    SaleCom = fields.StringField(default='', max_length=255, )
    SaleComPhone = fields.StringField(default='', max_length=255, )
    SaleAddress = fields.StringField(default='', max_length=255, )
    SalePhone = fields.StringField(default='', max_length=255, )
    ManagementCompany = fields.StringField(default='', max_length=255, )
    SoldStatusInfo = fields.DictField(default={'0': '0'})
    GetSoldStatusUrl = fields.URLField(default=None, blank=True)
    BuildingBaseUrl = fields.URLField(default=None, blank=True)
    SourceUrl = fields.URLField(default=None, blank=True)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectNo',
            'OnSoldNumber',
            'SoldNumber'
        ]
    }


class MonitorHouseBaseWuxi(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    NewCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    change_data = fields.StringField(default='', max_length=10240, null=False)
    ProjectName = fields.StringField(default='', max_length=255, null=False)
    BuildingNum = fields.StringField(default='', max_length=255, null=False)
    HouseTitle = fields.StringField(default='', max_length=255, null=False)
    HouseNo = fields.StringField(default='', max_length=255, null=False)
    HouseFwid = fields.StringField(default='', max_length=255, null=False)
    HouseLpid = fields.StringField(default='', max_length=255, null=False)
    HouseSts = fields.StringField(default='', max_length=255, null=False)
    HouseStsLatest = fields.StringField(default='', max_length=255, null=False)
    HouseInfoUrl = fields.URLField(default=None, blank=True)
    SourceUrl = fields.URLField(default=None, blank=True)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'change_data',
            'HouseNo',
            'HouseSts',
        ]
    }


class DeveloperBaseWuxi(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    NewCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    change_data = fields.StringField(default='', max_length=10240, null=False)
    DeveloperNo = fields.StringField(default='', max_length=255, null=False)
    DeveloperName = fields.StringField(default='', max_length=255, )
    DeveloperAddress = fields.StringField(default='', max_length=255, )
    DeveloperFullName = fields.StringField(default='', max_length=255, )
    DeveloperLevel = fields.StringField(default='', max_length=255, )
    LegalPerson = fields.StringField(default='', max_length=255, )
    SalesManager = fields.StringField(default='', max_length=255, )
    ZipCode = fields.StringField(default='', max_length=255, )
    Fax = fields.StringField(default='', max_length=255, )
    Web = fields.StringField(default='', max_length=255, )
    EMail = fields.StringField(default='', max_length=255, )
    ProjectName = fields.StringField(default='', max_length=255, )
    SourceUrl = fields.URLField(default=None, blank=True)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'DeveloperNo',
            'DeveloperAddress',
        ]
    }


class HouseBaseWuxi(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    NewCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    change_data = fields.StringField(default='', max_length=10240, null=False)
    HouseNo = fields.StringField(default='', max_length=255, null=False)
    ProjectName = fields.StringField(default='', max_length=255, null=False)
    BuildingNum = fields.StringField(default='', max_length=255, null=False)
    HouseAddress = fields.StringField(default='', max_length=255, null=False)
    HouseCode = fields.StringField(default='', max_length=255, null=False)
    HouseSts = fields.StringField(default='', max_length=255, null=False)
    HouseStsLatest = fields.StringField(default='', max_length=255, null=False)
    BuildingNumber = fields.StringField(default='', max_length=255, null=False)
    UnitNumber = fields.StringField(default='', max_length=255, null=False)
    HouseNumber = fields.StringField(default='', max_length=255, null=False)
    ActualFloor = fields.StringField(default='', max_length=255, null=False)
    TotalFloor = fields.StringField(default='', max_length=255, null=False)
    BuildingStructure = fields.StringField(default='', max_length=255, null=False)
    HouseUseType = fields.StringField(default='', max_length=255, null=False)
    AreasType = fields.StringField(default='', max_length=255, null=False)
    TotalArea = fields.StringField(default='', max_length=255, null=False)
    InsideOfBuildingArea = fields.StringField(default='', max_length=255, null=False)
    MeasuredSharedPublicArea = fields.StringField(default='', max_length=255, null=False)
    hightArea = fields.StringField(default='', max_length=255, null=False)
    Remarks = fields.StringField(default='', max_length=255, null=False)
    Price = fields.StringField(default='', max_length=255, null=False)
    SourceUrl = fields.URLField(default=None, blank=True)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'HouseNo',
            'HouseSts',
            'HouseStsLatest'
        ]
    }


class ProjectBaseWulumuqi(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    PropertyID = fields.StringField(default='', max_length=100, null=False)  # 楼盘id
    sid = fields.StringField(default='33', max_length=100, null=False)  # sid
    ProjectAllrankvalue = fields.StringField(default='', max_length=100)  # 综合评分
    ProjectName = fields.StringField(default='', max_length=100, null=False)  # 楼盘名称
    PromotionName = fields.StringField(default=None, null=True, blank=True, max_length=50)  # 推广名
    DistrictName = fields.StringField(default='', max_length=50)  # 行政区
    RegionName = fields.StringField(default='', max_length=50)  # 街道
    ProjectAddress = fields.StringField(default='', max_length=100, null=False)  # 楼盘地址
    ProjectSellAddress = fields.StringField(default='', max_length=100)  # 售楼地址
    ProjectMainUnitType = fields.StringField(default='', max_length=100)  # 主力户型
    ProjectDecoration = fields.StringField(default='', max_length=100)  # 装修情况
    BuildingType = fields.StringField(default='', max_length=100)  # 建筑类型/建筑形式
    LandUse = fields.StringField(default='', max_length=100)  # 物业类型/土地用途
    FloorAreaRatio = fields.StringField(default='', max_length=100)  # 容积率
    GreeningRate = fields.StringField(default='', max_length=100)  # 绿化率
    FloorArea = fields.StringField(default='', max_length=100)  # 占地面积
    CompletionDate = fields.StringField(default='', max_length=100)  # 竣工时间
    TotalBuidlingArea = fields.StringField(default='', max_length=100)  # 总建筑面积
    HousingCount = fields.StringField(default='', max_length=100)  # 总户数
    LatestDeliversHouseDate = fields.StringField(default='', max_length=100)  # 预计交付时间
    ParkingInfo = fields.StringField(default='', max_length=100)  # 车位信息
    ManagementFees = fields.StringField(default='', max_length=100)  # 物业费
    ManagementCompany = fields.StringField(default='', max_length=100)  # 物业公司
    PropertyRightsDescription = fields.StringField(default='', max_length=100)  # 产权年限
    Developer = fields.StringField(default='', max_length=100)  # 项目公司
    Selltel = fields.StringField(default='', max_length=100)  # 售楼部电话
    OnSaleState = fields.StringField(default='', max_length=100, null=False)  # 楼盘状态/在售状态
    TrafficSituation = fields.StringField(default='')  # 交通情况
    ProjectSupporting = fields.StringField(default='')  # 项目配套
    ProjectIntro = fields.StringField(default='')  # 项目简介
    SourceUrl = fields.URLField(default=None, null=True, blank=True)  # 项目详细URL
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
        ]
    }


class PresellInfoWulumuqi(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(), binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)  # 创建时间
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    PresellUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    PresellID = fields.StringField(default='', max_length=100, null=False)  # 预售证id
    PropertyID = fields.StringField(default='', max_length=100, null=False)  # 预售证id
    sid = fields.StringField(default='', max_length=100, index=True, null=False)  # sid
    PresellNO = fields.StringField(default='')  # 预售证号/预售证编号
    PresellName = fields.StringField(default='', null=True)  # 预售证号/预售证编号
    LandUse = fields.StringField(default='', max_length=100)  # 物业类型/土地用途
    LssueDate = fields.StringField(default='', max_length=100, null=True)  # 预售证核发时间
    Applycorp = fields.StringField(default='', max_length=100, null=True)  # 预售证申领单位
    LssuingAuthority = fields.StringField(default='', max_length=100, null=True, blank=True)  # 发证机关
    ApprovalPresalePosition = fields.StringField(default='', max_length=100, null=True, blank=True)  # 批准预售位置

    Bank = fields.StringField(default='', max_length=100, null=True, blank=True)  # 资金监管银行
    BankAccount = fields.StringField(default='', max_length=100, null=True)  # 资金监管银行账号
    # 接口返回的字段
    num = fields.IntField(default=0, null=True, blank=True)  # 纳入网上预（销）售总套数
    justnum = fields.IntField(default=0, null=True, blank=True)  # 即将解除限制房产套数
    area = fields.FloatField(default=0.00, null=True, blank=True)  # 纳入网上预（销）售总面积
    justarea = fields.FloatField(default=0.00, null=True, blank=True)  # 即将解除限制房产总面积
    avanum = fields.IntField(default=0, null=True, blank=True)  # 可预（销）售总套数
    waitnum = fields.IntField(default=0, null=True, blank=True)  # 待现售房产套数
    avaarea = fields.FloatField(default=0.00, null=True, blank=True)  # 可预（销）售总面积
    waitarea = fields.FloatField(default=0.00, null=True, blank=True)  # 可预（销）售总套数
    resideavanum = fields.IntField(default=0, null=True, blank=True)  # 其中可预（销）售住宅总套数
    limitnum = fields.IntField(default=0, null=True, blank=True)  # 限制房产套数
    resideavaarea = fields.FloatField(default=0.00, null=True, blank=True)  # 可预（销）售住宅总面积
    limitarea = fields.FloatField(default=0.00, null=True, blank=True)  # 限制房产总面积
    dealnum = fields.IntField(default=0, null=True, blank=True)  # 已预（销）售总套数
    notnum = fields.IntField(default=0, null=True, blank=True)  # 未纳入网上销售房产套数
    dealarea = fields.FloatField(default=0.00, null=True, blank=True)  # 已预（销）售总面积
    notarea = fields.IntField(default=0, null=True, blank=True)  # 未纳入网上销售房产总面积
    plannum = fields.IntField(default=0, null=True, blank=True)  # 已预定套数
    planarea = fields.IntField(default=0, null=True, blank=True)  # 已预定总面积

    OpeningDate = fields.StringField(default='', max_length=100, null=True, blank=True)  # 开盘时间
    OpeningPrice = fields.FloatField(default=0.00, null=True, blank=True)  # 开盘价格
    ApprovalProjectName = fields.StringField(default='', max_length=100, null=True, blank=True)  # 预售审批项目名称
    PresellURL = fields.URLField(default=None, null=True, blank=True)  # 预售价地址
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'PresellUUID',
        ]
    }


class BuildingInfoWulumuqi(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    PresellUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    BuildingID = fields.StringField(default='', max_length=100, null=False)  # 楼栋id
    BuildingName = fields.StringField(default='', max_length=100, null=False)  # 楼栋名
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'PresellUUID',
            'BuildingUUID',
        ]
    }


class HouseInfoWulumuqi(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    PresellUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    HouseUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    BuildingName = fields.StringField(default='', max_length=100, null=False)  # 楼栋名
    UnitName = fields.StringField(default='', max_length=100, null=True, blank=True)  # 单元
    HouseNO = fields.StringField(default='', max_length=50)  # 户号
    RoughPrice = fields.StringField(default='', null=False)  # 毛坯单价
    HousePrice = fields.StringField(default='', null=False)  # 总价
    HouseBuildingArea = fields.StringField(default='', null=False)  # 建筑面积
    HouseInnerArea = fields.StringField(default='', null=False)  # 套内面积
    HouseState = fields.StringField(default='', max_length=50)  # 当前状态
    HouseStateLatest = fields.StringField(default='', max_length=255, null=False, blank=True)
    HouseType = fields.StringField(default='', max_length=50)  # 户型
    HouseFloor = fields.StringField(default='', null=False)  # 户楼层
    BuildingFloor = fields.StringField(default='', null=False)  # 总楼层
    HouseLocated = fields.StringField(default='', max_length=255)  # 坐落
    HouseUsage = fields.StringField(default='', max_length=50)  # 房屋用途
    HouseStructure = fields.StringField(default='', max_length=50)  # 房屋结构
    RoomRate = fields.StringField(default='', null=False)  # 得房率
    HouseManagementFees = fields.StringField(default='', null=False)  # 物业费
    HouseOrientation = fields.StringField(default='', max_length=50)  # 朝向
    DeclarationTime = fields.StringField(default='', max_length=50)  # 申报时间
    HouseURL = fields.URLField(default=None, null=True, blank=True)  # 户详情地址
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'PresellUUID',
            'BuildingUUID',
            'HouseUUID',
        ]
    }


class ProjectBaseTaizhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)

    PropertyID = fields.StringField(default='', max_length=100, null=False)  # 楼盘id
    sid = fields.StringField(default='33', max_length=100, null=False)  # sid

    ProjectAllrankvalue = fields.StringField(default='', max_length=100)  # 综合评分
    ProjectName = fields.StringField(default='', max_length=100, null=False)  # 楼盘名称
    PromotionName = fields.StringField(default=None, null=True, blank=True, max_length=50)  # 推广名
    DistrictName = fields.StringField(default='', max_length=50)  # 行政区
    RegionName = fields.StringField(default='', max_length=50)  # 街道
    ProjectAddress = fields.StringField(default='', max_length=100, null=False)  # 项目地址
    OnSaleState = fields.StringField(default='', max_length=100, null=False)  # 楼盘状态/在售状态
    LandUse = fields.StringField(default='', max_length=100)  # 物业类型/土地用途
    HousingCount = fields.StringField(default='', max_length=100)  # 总户数

    ProjectSellAddress = fields.StringField(default='', max_length=100)  # 售楼地址
    ProjectMainUnitType = fields.StringField(default='', max_length=100)  # 主力户型
    ProjectDecoration = fields.StringField(default='', max_length=100)  # 装修情况
    BuildingType = fields.StringField(default='', max_length=100)  # 建筑类型/建筑形式
    FloorAreaRatio = fields.StringField(default='', max_length=100)  # 容积率
    GreeningRate = fields.StringField(default='', max_length=100)  # 绿化率
    FloorArea = fields.StringField(default='', max_length=100)  # 占地面积
    CompletionDate = fields.StringField(default='', max_length=100)  # 竣工时间
    TotalBuidlingArea = fields.StringField(default='', max_length=100)  # 总建筑面积
    HousingCount = fields.StringField(default='', max_length=100)  # 总户数
    LatestDeliversHouseDate = fields.StringField(default='', max_length=100)  # 预计交付时间
    ParkingInfo = fields.StringField(default='', max_length=100)  # 车位信息
    ManagementFees = fields.StringField(default='', max_length=100)  # 物业费
    ManagementCompany = fields.StringField(default='', max_length=100)  # 物业公司

    PropertyRightsDescription = fields.StringField(default='', max_length=100)  # 产权年限
    Developer = fields.StringField(default='', max_length=100)  # 项目公司
    Selltel = fields.StringField(default='', max_length=100)  # 售楼部电话

    TrafficSituation = fields.StringField(default='')  # 交通情况
    ProjectSupporting = fields.StringField(default='')  # 项目配套
    ProjectIntro = fields.StringField(default='')  # 项目简介
    SourceUrl = fields.URLField(default=None, null=True, blank=True)  # 项目详细URL

    OnsoldAmount = fields.StringField(default='', max_length=100)  # 可售套数
    ApprovalPresaleAmount = fields.StringField(default='', max_length=100)  # 可售套数/批准预售套数
    AveragePrice = fields.StringField(default='', max_length=100)  # 非住宅均价

    CumulativeSoldAveragePrice = fields.StringField(default='', max_length=100)  # 累计均价
    LatelyAveragePrice = fields.StringField(default='', max_length=100)  # 近日成交均价
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
        ]
    }


class PresellInfoTaizhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(), binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)  # 创建时间
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    PresellUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    PresellID = fields.StringField(default='', max_length=100, null=False)  # 预售证id
    sid = fields.StringField(default='', max_length=100, index=True, null=False)  # sid
    ProjectName = fields.StringField(default='', max_length=100, null=False)  # 楼盘名称
    PresalePermitNumber = fields.StringField(default='', null=True)  # 预售证号/预售证编号
    PresellName = fields.StringField(default='')  # 预售证号/预售证编号
    LssueDate = fields.StringField(default='', max_length=100)  # 预售证核发时间
    Applycorp = fields.StringField(default='', max_length=100)  # 预售证申领单位
    LssuingAuthority = fields.StringField(default='', max_length=100, null=True, blank=True)  # 发证机关

    Bank = fields.StringField(default='', max_length=100, null=True, blank=True)  # 资金监管银行
    BankAccount = fields.StringField(default='', max_length=100, null=True)  # 资金监管银行账号
    # 接口返回的字段
    num = fields.IntField(default=0, null=True, blank=True)  # 纳入网上预（销）售总套数
    justnum = fields.IntField(default=0, null=True, blank=True)  # 即将解除限制房产套数
    area = fields.FloatField(default=0.00, null=True, blank=True)  # 纳入网上预（销）售总面积
    justarea = fields.FloatField(default=0.00, null=True, blank=True)  # 即将解除限制房产总面积
    avanum = fields.IntField(default=0, null=True, blank=True)  # 可预（销）售总套数
    waitnum = fields.IntField(default=0, null=True, blank=True)  # 待现售房产套数
    avaarea = fields.FloatField(default=0.00, null=True, blank=True)  # 可预（销）售总面积
    waitarea = fields.FloatField(default=0.00, null=True, blank=True)  # 可预（销）售总套数
    resideavanum = fields.IntField(default=0, null=True, blank=True)  # 其中可预（销）售住宅总套数
    limitnum = fields.IntField(default=0, null=True, blank=True)  # 限制房产套数
    resideavaarea = fields.FloatField(default=0.00, null=True, blank=True)  # 可预（销）售住宅总面积
    limitarea = fields.FloatField(default=0.00, null=True, blank=True)  # 限制房产总面积
    dealnum = fields.IntField(default=0, null=True, blank=True)  # 已预（销）售总套数
    notnum = fields.IntField(default=0, null=True, blank=True)  # 未纳入网上销售房产套数
    dealarea = fields.FloatField(default=0.00, null=True, blank=True)  # 已预（销）售总面积
    notarea = fields.IntField(default=0, null=True, blank=True)  # 未纳入网上销售房产总面积
    plannum = fields.IntField(default=0, null=True, blank=True)  # 已预定套数
    planarea = fields.IntField(default=0, null=True, blank=True)  # 已预定总面积

    OpeningDate = fields.StringField(default='', max_length=100)  # 开盘时间
    OpeningPrice = fields.StringField(default='', max_length=100)  # 开盘价格
    LandUse = fields.StringField(default='', max_length=100)  # 土地用途
    ApprovalPresalePosition = fields.StringField(default='', max_length=200)  # 批准预售位置
    ApprovalProjectName = fields.StringField(default='')  # 预售审批项目名称
    PresellURL = fields.URLField(default=None, null=True, blank=True)  # 预售价地址
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'PresellUUID',
        ]
    }


class BuildingInfoTaizhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    PresellUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    BuildingID = fields.StringField(default='', max_length=100, null=False)  # 楼栋id
    ProjectName = fields.StringField(default='', max_length=100, null=False)  # 楼盘名称
    PresalePermitNumber = fields.StringField(default='', null=True)  # 预售证号/预售证编号
    BuildingName = fields.StringField(default='', max_length=100, null=False)  # 楼栋名
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'PresellUUID',
            'BuildingUUID',
            'ProjectName',
            'PresalePermitNumber',
            'BuildingName',
        ]
    }


class HouseInfoTaizhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    PresellUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    HouseUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=100, null=False)  # 楼盘名称
    PresalePermitNumber = fields.StringField(default='', null=True)  # 预售证号/预售证编号
    BuildingName = fields.StringField(default='', max_length=100, null=False)  # 楼栋名
    UnitName = fields.StringField(default='', max_length=100, null=True, blank=True)  # 单元
    HouseNO = fields.StringField(default='', max_length=50)  # 户号
    RoughPrice = fields.StringField(default='', null=False)  # 毛坯单价
    TotalPrice = fields.StringField(default='', max_length=100)  # 总价
    HouseBuildingArea = fields.StringField(default='', null=False)  # 建筑面积
    HouseInnerArea = fields.StringField(default='', null=False)  # 套内面积
    HouseState = fields.StringField(default='', max_length=50)  # 当前状态
    HouseStateLatest = fields.StringField(default='', max_length=255, null=False, blank=True)
    HouseType = fields.StringField(default='', max_length=50)  # 户型
    FloorCount = fields.StringField(default='', null=False)  # 户楼层
    BuildingFloor = fields.StringField(default='', null=False)  # 总楼层
    HouseLocated = fields.StringField(default='', max_length=255)  # 坐落
    HouseUsage = fields.StringField(default='', max_length=50)  # 房屋用途
    HouseStructure = fields.StringField(default='', max_length=50)  # 房屋结构
    RoomRate = fields.StringField(default='', null=False)  # 得房率
    HouseManagementFees = fields.StringField(default='', null=False)  # 物业费
    Toward = fields.StringField(default='', max_length=50)  # 朝向
    DeclarationTime = fields.StringField(default='', max_length=50)  # 申报时间
    SourceUrl = fields.URLField(default=None, null=True, blank=True)  # 户详情地址
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'PresellUUID',
            'BuildingUUID',
            'HouseUUID',
            'ProjectName',
            'PresalePermitNumber',
            'BuildingName',
            'HouseState',
            'HouseStateLatest',
            'SourceUrl',
        ]
    }


class ProjectBaseYantai(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)  # 创建时间
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=200, null=False)  # 楼盘名称
    Developer = fields.StringField(default='', max_length=200)  # 开发商
    ProjectAddress = fields.StringField(default='', max_length=255)  # 项目地址
    PresalePermitNumber = fields.StringField(default='', max_length=200)  # 预售证
    SoldAmount = fields.StringField(default='', max_length=100, null=False)  # 已售套数
    UnsoldAmount = fields.StringField(default='', max_length=200)  # 未售套数
    SourceUrl = fields.URLField(default=None, null=True, blank=True)  # 项目详细URL
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
            'UnsoldAmount',
            'SourceUrl',
        ]
    }


class ProjectInfoYantai(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(), binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)  # 创建时间
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    ProjectNO = fields.StringField(default='', max_length=100)  # 项目编号
    ProjectName = fields.StringField(default='', max_length=100, null=False)  # 项目名称
    Developer = fields.StringField(default='', max_length=200)  # 开发商
    ProjectAddress = fields.StringField(default='', max_length=255)  # 项目地址
    DistrictName = fields.StringField(default='', max_length=50)  # 行政区
    FloorAreaRatio = fields.StringField(default='', max_length=100)  # 容积率
    TotalBuidlingArea = fields.StringField(default='', max_length=100)  # 总建筑面积
    PlanningAcceptanceDate = fields.StringField(default='', max_length=100)  # 规划验收日期
    ComprehensiveAcceptanceDate = fields.StringField(default='', max_length=100)  # 综合验收日期
    PlanInvest = fields.StringField(default='', max_length=100)  # 计划总投资(万元)
    PresalePermitNumber = fields.StringField(default='', max_length=200)  # 预售证
    SoldAmount = fields.StringField(default='', max_length=100, null=False)  # 已售套数
    UnsoldAmount = fields.StringField(default='', max_length=200)  # 未售套数
    SoldArea = fields.StringField(default='', max_length=200)  # 已售总面积
    UnsoldArea = fields.StringField(default='', max_length=200)  # 未售总面积
    CheckOutAmount = fields.StringField(default='', max_length=200)  # 退房次数
    CheckOutRatio = fields.StringField(default='', max_length=200)  # 退房率(%)
    SellAddress = fields.StringField(default='', max_length=200)  # 售楼地址
    Selltel = fields.StringField(default='', max_length=100)  # 售楼部电话
    DesignUnit = fields.StringField(default='', max_length=100)  # 设计单位
    ConstructionUnit = fields.StringField(default='', max_length=100)  # 施工单位
    SupervisionUnit = fields.StringField(default='', max_length=100)  # 监理单位
    ManagementCompany = fields.StringField(default='', max_length=100)  # 物业管理公司
    ProjectSupporting = fields.StringField(default='')  # 项目配套
    AroundSupporting = fields.StringField(default='')  # 周边配套
    ProjectIntro = fields.StringField(default='')  # 项目简介

    TodayHousingSoldAmount = fields.StringField(default='')  # 今日住宅已售套数
    TodayHousingSoldArea = fields.StringField(default='')  # 今日住宅已售面积
    HousingSoldAmount = fields.StringField(default='')  # 住宅已售套数
    HousingSoldArea = fields.StringField(default='')  # 住宅已售面积
    HousingUnsoldAmount = fields.StringField(default='')  # 住宅未售套数
    HousingUnsoldArea = fields.StringField(default='')  # 住宅未售面积

    TodayShopSoldAmount = fields.StringField(default='')  # 今日商业已售套数
    TodayShopSoldArea = fields.StringField(default='')  # 今日商业已售面积
    ShopSoldAmount = fields.StringField(default='')  # 商业已售套数
    ShopSoldArea = fields.StringField(default='')  # 商业已售面积
    ShopUnsoldAmount = fields.StringField(default='')  # 商业未售套数
    ShopUnsoldArea = fields.StringField(default='')  # 商业未售面积

    TodayOfficeSoldAmount = fields.StringField(default='')  # 今日办公已售套数
    TodayOfficeSoldArea = fields.StringField(default='')  # 今日办公已售面积
    OfficeSoldAmount = fields.StringField(default='')  # 办公已售套数
    OfficeSoldArea = fields.StringField(default='')  # 办公已售面积
    OfficeUnsoldAmount = fields.StringField(default='')  # 办公未售套数
    OfficeUnsoldArea = fields.StringField(default='')  # 办公未售面积

    TodayOtherSoldAmount = fields.StringField(default='')  # 今日其他已售套数
    TodayOtherSoldArea = fields.StringField(default='')  # 今日其他已售面积
    OtherSoldAmount = fields.StringField(default='')  # 其他已售套数
    OtherSoldArea = fields.StringField(default='')  # 其他已售面积
    OtherUnsoldAmount = fields.StringField(default='')  # 其他未售套数
    OtherUnsoldArea = fields.StringField(default='')  # 其他未售面积

    CertificateOfUseOfStateOwnedLand = fields.StringField(default='', null=True, blank=True)  # 土地使用证
    ConstructionPermitNumber = fields.StringField(default='', null=True, blank=True)  # 施工许可证号
    LandUsePermit = fields.StringField(default='', null=True, blank=True)  # 建设用地规划许可证号
    BuildingPermit = fields.StringField(default='', null=True, blank=True)  # 建设工程规划许可证号

    SourceUrl = fields.URLField(default=None, null=True, blank=True)  # 项目详细URL
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectNO',
            'ProjectName',
            'Developer',
            'ProjectAddress',
            'DistrictName',
            'FloorAreaRatio',
            'TotalBuidlingArea',
            'SoldAmount',
            'UnsoldAmount',
            'SoldArea',
            'UnsoldArea',
            'CertificateOfUseOfStateOwnedLand',
            'ConstructionPermitNumber',
            'LandUsePermit',
            'BuildingPermit',
            'SourceUrl',
        ]
    }


class PresellInfoYantai(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=100, null=False)  # 项目名称
    PresellUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    PresalePermitNumber = fields.StringField(default='', max_length=100)  # 许可证号
    LssueDate = fields.StringField(default='', max_length=100)  # 发证日期
    ValidityDateStartDate = fields.StringField(default='', max_length=100)  # 有效期起始日期
    ValidityDateClosingDate = fields.StringField(default='', max_length=100)  # 有效期截止日期
    PresaleBuildingName = fields.StringField(default='', max_length=255)  # 预售幢名称
    LssuingAuthority = fields.StringField(default='', max_length=100)  # 发证机关
    Bank = fields.StringField(default='', max_length=100)  # 预售资金开户银行
    BankAccount = fields.StringField(default='', max_length=100)  # 预售资金监管帐号
    ApprovalPresaleHouseAmount = fields.StringField(default='', max_length=100)  # 批准预售住宅套数
    ApprovalPresaleHouseArea = fields.StringField(default='', max_length=100)  # 批准预售住宅面积
    ApprovalPresaleShopAmount = fields.StringField(default='', max_length=100)  # 批准预售商业套数
    ApprovalPresaleShopArea = fields.StringField(default='', max_length=100)  # 批准预售商业面积
    ApprovalPresaleOfficeAmount = fields.StringField(default='', max_length=100)  # 批准预售办公套数
    ApprovalPresaleOfficeArea = fields.StringField(default='', max_length=100)  # 批准预售办公面积
    ApprovalPresaleOtherAmount = fields.StringField(default='', max_length=100)  # 批准预售其他套数
    ApprovalPresaleOtherArea = fields.StringField(default='', max_length=100)  # 批准预售其他面积
    SourceUrl = fields.URLField(default=None, null=True, blank=True)  # 预售证url
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
            'PresellUUID',
            'PresalePermitNumber',
            'LssueDate',
            'SourceUrl',
        ]
    }


class BuildingInfoYantai(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=100, null=False)  # 项目名称
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    BuildingID = fields.StringField(default='', max_length=100, null=False)  # 楼栋ID
    BuildingName = fields.StringField(default='', max_length=100, null=False)  # 楼栋名
    SourceUrl = fields.URLField(default=None, null=True, blank=True)  # 楼栋销控表列表页url
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'BuildingUUID',
            'ProjectName',
            'BuildingName',
            'SourceUrl',
        ]
    }


class HouseInfoYantai(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=100)  # 楼栋名
    BuildingName = fields.StringField(default='', max_length=100)  # 楼栋名
    HouseUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    HouseNumber = fields.StringField(default='', max_length=255)  # 户号
    UnitName = fields.StringField(default='', max_length=255)  # 单元
    ActualFloor = fields.StringField(default='', max_length=255)  # 楼层
    HouseState = fields.StringField(default='', max_length=255)  # 当前状态
    HouseStateLatest = fields.StringField(default='', max_length=255, null=False, blank=True)  # 上次状态

    UnitShape = fields.StringField(default='', max_length=255)  # 户型
    Dwelling = fields.StringField(default='', max_length=255)  # 房屋类型
    NatureOfPropertyRight = fields.StringField(default='', max_length=255)  # 房屋性质
    HouseUseType = fields.StringField(default='', max_length=255)  # 房屋用途
    OwnershipStatus = fields.StringField(default='', max_length=255)  # 权属状态
    BalconyType = fields.StringField(default='', max_length=255)  # 阳台类型

    ForecastBuildingArea = fields.StringField(default='', max_length=255)  # 预测建筑面积
    ForecastInsideOfBuildingArea = fields.StringField(default='', max_length=255)  # 预测套内面积
    ForecastPublicArea = fields.StringField(default='', max_length=255)  # 预测公摊面积
    MeasuredBuildingArea = fields.StringField(default='', max_length=255)  # 实测建筑面积
    MeasuredInsideOfBuildingArea = fields.StringField(default='', max_length=255)  # 实测套内面积
    MeasuredSharedPublicArea = fields.StringField(default='', max_length=255)  # 实测公摊面积

    Decoration = fields.StringField(default='', max_length=255)  # 装饰标准
    EquipmentStandard = fields.StringField(default='', max_length=255)  # 设备标准
    HouseMatching = fields.StringField(default='', max_length=255)  # 户室配套
    IsMortgage = fields.StringField(default='', max_length=255)  # 是否抵押
    IsAttachment = fields.StringField(default='', max_length=255)  # 是否查封
    IsSold = fields.StringField(default='', max_length=255)  # 是否可售
    Price = fields.StringField(default='', max_length=255)  # 申报价格
    SourceUrl = fields.URLField(default=None, null=True, blank=True)  # 户详情地址
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'BuildingUUID',
            'ProjectName',
            'BuildingName',
            'HouseUUID',
            'HouseNumber',
            'UnitName',
            'HouseState',
            'HouseStateLatest',
            'UnitShape',
            'Dwelling',
            'NatureOfPropertyRight',
            'HouseUseType',
            'ForecastBuildingArea',
            'ForecastInsideOfBuildingArea',
            'ForecastPublicArea',
            'MeasuredBuildingArea',
            'MeasuredInsideOfBuildingArea',
            'MeasuredSharedPublicArea',
            'Price',
            'SourceUrl',
        ]
    }


class ProjectInfoXuzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()))
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    ProjectID = fields.StringField(default='', null=False, max_length=255)
    DistrictName = fields.StringField(default='', max_length=255)  # 行政区
    ProjectName = fields.StringField(default='', max_length=255)  # 从列表带过来的项目名称
    PageProjectName = fields.StringField(default='', max_length=255)  # 项目信息页的项目名称
    RegionName = fields.StringField(default='', max_length=255)  # 片区
    PromotionName = fields.StringField(default='', max_length=255)  # 推广名
    Developer = fields.StringField(default='', max_length=255)  # 开发商
    SellAddress = fields.StringField(default='', max_length=255)  # 售楼地址
    ProjectAddress = fields.StringField(default='', max_length=255)  # 项目地址
    EarliestStartDate = fields.StringField(default='', max_length=255)  # 开工时间
    CompletionDate = fields.StringField(default='', max_length=255)  # 竣工时间
    PropertyRightsDescription = fields.StringField(default='', max_length=255)  # 使用年限
    GreeningRate = fields.StringField(default='', max_length=255)  # 绿化率
    Decoration = fields.StringField(default='', max_length=255)  # 装修情况
    FloorAreaRatio = fields.StringField(default='', max_length=255)  # 容积率
    AveragePrice = fields.StringField(default='', max_length=255)  # 均价
    TotalBuidlingArea = fields.StringField(default='', max_length=255)  # 建筑面积
    ManagementFees = fields.StringField(default='', max_length=255)  # 物业费
    ParkingSpaceAmount = fields.StringField(default='', max_length=255)  # 车位
    ProjectIntro = fields.StringField(default='')  # 项目介绍
    ProjectSupporting = fields.StringField(default='')  # 项目配套
    SourceUrl = fields.URLField(default=None, null=True, blank=True)  # 项目详细URL
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectID',
            'DistrictName',
            'ProjectName',
            'RegionName',
            'PromotionName',
            'Developer',
            'ProjectAddress',
            'AveragePrice',
            'SourceUrl',
        ]
    }


class PresellInfoXuzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(), binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()))
    PresellUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=255)  # 项目名称
    LssueDate = fields.StringField(default='', max_length=255)  # 发证日期
    DistrictName = fields.StringField(default='', max_length=255)  # 行政区
    ProjectAddress = fields.StringField(default='', max_length=255)  # 项目地址
    RegionName = fields.StringField(default='', max_length=255)  # 区位
    Developer = fields.StringField(default='', max_length=255)  # 开发商
    LandUse = fields.StringField(default='', max_length=255)  # 规划用途
    BuildingPermit = fields.StringField(default='')  # 工程规划许可证
    CertificateOfUseOfStateOwnedLand = fields.StringField(default='')  # 用地许可证
    ConstructionPermitNumber = fields.StringField(default='')  # 施工许可证
    LandCertificate = fields.StringField(default='')  # 土地证
    FloorArea = fields.StringField(default='')  # 土地面积
    PresalePermitNumber = fields.StringField(default='')  # 预售证号
    EarliestStartDate = fields.StringField(default='', max_length=255)  # 开工时间
    CompletionDate = fields.StringField(default='', max_length=255)  # 预计竣工时间
    ApprovalPresaleAmount = fields.StringField(default='', max_length=255)  # 总入网套数
    SoldAmount = fields.StringField(default='', max_length=255)  # 已销售套数
    UnsoldAmount = fields.StringField(default='', max_length=255)  # 可售套数
    ApprovalPresaleArea = fields.StringField(default='', max_length=255)  # 总入网面积
    SoldArea = fields.StringField(default='', max_length=255)  # 已销售面积
    UnsoldArea = fields.StringField(default='', max_length=255)  # 可售面积
    SoldRatio = fields.StringField(default='', max_length=255)  # 销售比例
    SourceUrl = fields.URLField(default=None, null=True, blank=True)  # 预售证URL
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'PresellUUID',
            'ProjectName',
            'DistrictName',
            'ProjectAddress',
            'RegionName',
            'UnsoldAmount',
            'SourceUrl',
        ]
    }


class BuildingInfoXuzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(), binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()))
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    PresellUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=255)  # 项目名称
    PresalePermitNumber = fields.StringField(default='', max_length=255)  # 预售证号
    BuildingName = fields.StringField(default='', max_length=255)  # 楼栋名称
    ApprovalPresaleAmount = fields.StringField(default='', max_length=255)  # 总入网套数
    SoldAmount = fields.StringField(default='', max_length=255)  # 已销售套数
    UnsoldAmount = fields.StringField(default='', max_length=255)  # 可售套数
    ApprovalPresaleArea = fields.StringField(default='', max_length=255)  # 总入网面积
    SoldArea = fields.StringField(default='', max_length=255)  # 已销售面积
    UnsoldArea = fields.StringField(default='', max_length=255)  # 可售面积
    SourceUrl = fields.URLField(default=None, null=True, blank=True)  # 楼栋销控表URL
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'PresellUUID',
            'BuildingUUID',
            'ProjectName',
            'PresalePermitNumber',
            'BuildingName',
            'UnsoldAmount',
            'SourceUrl',
        ]
    }


class HouseInfoXuzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(), binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()))
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    PresellUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    HouseUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=255)  # 项目名称
    PresalePermitNumber = fields.StringField(default='', max_length=255)  # 预售证号
    BuildingName = fields.StringField(default='', max_length=255)  # 楼栋名称
    UnitName = fields.StringField(default='', max_length=255)  # 单元号
    HouseNumber = fields.StringField(default='', max_length=255)  # 房号
    HouseUseType = fields.StringField(default='', max_length=255)  # 房屋功能/用途
    BuildingStructure = fields.StringField(default='', max_length=255)  # 房屋结构
    MeasuredBuildingArea = fields.StringField(default='', max_length=255)  # 实测建筑面积
    MeasuredInsideOfBuildingArea = fields.StringField(default='', max_length=255)  # 实测套内面积
    MeasuredSharedPublicArea = fields.StringField(default='', max_length=255)  # 实测公摊面积
    HouseState = fields.StringField(default='', max_length=255)  # 当前状态
    HouseStateLatest = fields.StringField(default='', max_length=255)  # 上次状态
    ContractRecordNumber = fields.StringField(default='', max_length=255)  # 合同备案号
    ContractRecordDate = fields.StringField(default='', max_length=255)  # 备案日期
    SourceUrl = fields.URLField(default=None, null=True, blank=True)  # 户详细URL
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
            'PresellUUID',
            'PresalePermitNumber',
            'BuildingUUID',
            'BuildingName',
            'HouseUUID',
            'HouseState',
            'HouseStateLatest',
            'SourceUrl',
        ]
    }


class UnitshapeImageInfoXuzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(), binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()))
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    PresellUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    HouseUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    SourceUrl = fields.URLField(default=None, null=True, blank=True)  # 户详细URL
    ImageUrls = fields.ListField(default=[], null=False)  # 图片下载地址
    ImageFiles = fields.ListField(default=[], null=False)  # 图片文件,base64
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'PresellUUID',
            'BuildingUUID',
            'HouseUUID',
            'SourceUrl',
        ]
    }


class ProjectBaseShaoxing(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=200, null=False)  # 楼盘名称
    OnSaleState = fields.StringField(default='', max_length=100, null=False)  # 楼盘状态/在售状态
    AveragePrice = fields.StringField(default='', max_length=200)  # 均价
    OnsoldAmount = fields.StringField(default='', max_length=100)  # 可售套数
    ApprovalPresaleAmount = fields.StringField(default='', max_length=100)  # 总套数/批准预售套数?
    SourceUrl = fields.URLField(default=None, null=True, blank=True)  # 项目详细URL
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
            'OnSaleState',
            'OnsoldAmount',
            'SourceUrl',
        ]
    }


class ProjectInfoShaoxing(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(), binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)  # 创建时间
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=100, null=False)  # 楼盘名称
    Developer = fields.StringField(default='', max_length=200)  # 开发商
    DistrictName = fields.StringField(default='', max_length=50)  # 行政区
    AreaRange = fields.StringField(default='', max_length=100)  # 面积范围
    FloorArea = fields.StringField(default='', max_length=100)  # 占地面积
    TotalBuidlingArea = fields.StringField(default='', max_length=100)  # 总建筑面积
    PriceStart = fields.StringField(default='', max_length=100)  # 起价
    EarliestOpeningTime = fields.StringField(default='', max_length=100)  # 开盘时间
    AveragePrice = fields.StringField(default='', max_length=100)  # 均价
    GreeningRate = fields.StringField(default='', max_length=100)  # 绿化率
    OnSaleState = fields.StringField(default='', max_length=100, null=False)  # 在售状态
    FloorAreaRatio = fields.StringField(default='', max_length=100)  # 容积率
    LandUse = fields.StringField(default='', max_length=100)  # 物业类型/土地用途
    ParkingSpaceAmount = fields.StringField(default='', max_length=100)  # 车位套数
    FloorCondition = fields.StringField(default='', max_length=100)  # 楼层状况
    PresalePermitNumber = fields.StringField(default='')  # 预售证号
    Contacts = fields.StringField(default='', max_length=100)  # 联系人
    Selltel = fields.StringField(default='', max_length=100)  # 售楼部电话
    ManagementCompany = fields.StringField(default='', max_length=100)  # 物业公司
    SellAddress = fields.StringField(default='', max_length=200)  # 售楼地址
    DecorationCondition = fields.StringField(default='', max_length=200)  # 装修状况
    ProjectAddress = fields.StringField(default='', max_length=200)  # 项目地址
    ProjectIntro = fields.StringField(default='')  # 项目简介
    TrafficSituation = fields.StringField(default='')  # 交通情况
    ProjectSupporting = fields.StringField(default='')  # 项目配套
    SourceUrl = fields.URLField(default=None, null=True, blank=True)  # 项目详细URL
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
            'DistrictName',
            'AreaRange',
            'FloorArea',
            'TotalBuidlingArea',
            'AveragePrice',
            'GreeningRate',
            'OnSaleState',
            'FloorAreaRatio',
            'LandUse',
            'PresalePermitNumber',
            'ProjectAddress',
            'SourceUrl',
        ]
    }


class BuildingInfoShaoxing(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=255)  # 项目名称
    BuildingName = fields.StringField(default='', max_length=100, null=False)  # 楼栋名
    ApprovalPresaleAmount = fields.StringField(default='', max_length=100, null=False)  # 总套数
    SoldAmount = fields.StringField(default='', max_length=100)  # 已售套数
    OnsoldAmount = fields.StringField(default='', max_length=100)  # 可售套数
    LimitAmount = fields.StringField(default='', max_length=100)  # 限制套数
    BuildingURL = fields.URLField(default=None, null=True, blank=True)  # 楼栋销控表url
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'BuildingUUID',
            'ProjectName',
            'BuildingName',
            'ApprovalPresaleAmount',
            'SoldAmount',
            'OnsoldAmount',
            'BuildingURL',
        ]
    }


class HouseInfoShaoxing(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    HouseUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=255)  # 项目名称
    BuildingName = fields.StringField(default='', max_length=255)  # 楼栋名称
    HouseNO = fields.StringField(default='', max_length=50)  # 户号
    HouseState = fields.StringField(default='', max_length=50)  # 当前状态
    HouseStateLatest = fields.StringField(default='', max_length=255, null=False, blank=True)  # 上次状态
    MeasuredBuildingArea = fields.StringField(default='', null=False)  # 建筑面积
    MeasuredInsideOfBuildingArea = fields.StringField(default='', null=False)  # 套内面积
    MeasuredSharedPublicArea = fields.StringField(default='', null=False)  # 分摊面积
    BuildingStructure = fields.StringField(default='', max_length=50)  # 建筑结构
    FloorName = fields.StringField(default='')  # 名义层/层名
    ActualFloor = fields.StringField(default='')  # 实际层
    HouseUseType = fields.StringField(default='', max_length=50)  # 房屋用途
    HouseSalePrice = fields.StringField(default='', max_length=50)  # 参考价格
    HouseSalePriceUpdateTime = fields.StringField(default='', max_length=50)  # 参考价格更新时间
    SourceUrl = fields.URLField(default=None, null=True, blank=True)  # 户详情地址
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'BuildingUUID',
            'HouseUUID',
            'ProjectName',
            'BuildingName',
            'HouseNO',
            'HouseState',
            'HouseStateLatest',
            'MeasuredBuildingArea',
            'MeasuredInsideOfBuildingArea',
            'MeasuredSharedPublicArea',
            'BuildingStructure',
            'FloorName',
            'ActualFloor',
            'HouseUseType',
            'HouseSalePrice',
            'SourceUrl',
        ]
    }


class ProjectBaseWenzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)

    ProjectNo = fields.StringField(default='', max_length=255, )
    ProjectUrl = fields.URLField(default=None, blank=True)
    PresalePermitNumber = fields.StringField(default='', max_length=255, )
    ProjectName = fields.StringField(default='', max_length=255, )

    ProjectAddress = fields.StringField(default='', max_length=255, )
    OpeningDate = fields.StringField(default='', max_length=255, )
    RegionName = fields.StringField(default='', max_length=255, )
    DeveloperInfoUrl = fields.URLField(default=None, blank=True)
    DeveloperName = fields.StringField(default='', max_length=255, )

    LssueDate = fields.StringField(default='', max_length=255, )

    Samplearea = fields.StringField(default='', max_length=255, )
    TotalBuidlingArea = fields.StringField(default='', max_length=255)

    StartDate = fields.StringField(default='', max_length=255, )
    ProjectSaleAddress = fields.StringField(default='', max_length=255, )
    ProjectSalePhone = fields.StringField(default='', max_length=255, )
    typePriceInfo = fields.DictField(default={'0': '0'})
    TotalHouseNum = fields.StringField(default='', max_length=255)
    TotalHouseAreas = fields.StringField(default='', max_length=255, )
    SalingHouseNum = fields.StringField(default='', max_length=255, )
    SalingHouseAreas = fields.StringField(default='', max_length=255, )
    SalingDwellingNum = fields.StringField(default='', max_length=255, )
    SalingDwellingAreas = fields.StringField(default='', max_length=255, )
    SubscribedNum = fields.StringField(default='', max_length=255, )
    SubscribedAreas = fields.StringField(default='', max_length=255, )
    SoldNum = fields.StringField(default='', max_length=255, )
    SoldAreas = fields.StringField(default='', max_length=255, )
    RegisteredNum = fields.StringField(default='', max_length=255, )
    RegisteredAreas = fields.StringField(default='', max_length=255, )
    PlacementofhousingNum = fields.StringField(default='', max_length=255, )
    PlacementofhousingAreas = fields.StringField(default='', max_length=255, )
    RestrictedpropertyNum = fields.StringField(default='', max_length=255, )
    RestrictedpropertyAreas = fields.StringField(default='', max_length=255, )
    NonsalesNum = fields.StringField(default='', max_length=255, )
    NonsalesAreas = fields.StringField(default='', max_length=255, )
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectNo',
        ]
    }


class DeveloperBaseWenzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)

    DeveloperNo = fields.StringField(default='', max_length=255, )
    DeveloperName = fields.StringField(default='', max_length=255, )
    ProjectName = fields.StringField(default='', max_length=255, )
    ProjectNo = fields.StringField(default='', max_length=255, )
    LegalRepresentative = fields.StringField(default='', max_length=255, )
    BusinessLicenseNumber = fields.StringField(default='', max_length=255, )
    DeveloperComAddress = fields.StringField(default='', max_length=255, )
    RegisteredCapital = fields.StringField(default='', max_length=255, )
    DeveloperPhoneNumber = fields.StringField(default='', max_length=255, )
    QualificationGrade = fields.StringField(default='', max_length=255, )
    CertificateNumber = fields.StringField(default='', max_length=255, )
    Fax = fields.StringField(default='', max_length=255, )
    ZipCode = fields.StringField(default='', max_length=255, )
    Email = fields.StringField(default='', max_length=255, )
    Web = fields.StringField(default='', max_length=255, )
    Remarks = fields.StringField(default='', max_length=255, )
    Registrar = fields.StringField(default='', max_length=255, )
    DeveloperUrl = fields.URLField(default=None, blank=True)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'DeveloperNo',
        ]
    }


class BuildingBaseWenzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectNo = fields.StringField(default='', max_length=255, )
    BuildingNo = fields.StringField(default='', max_length=255, )
    BuildingId = fields.StringField(default='', max_length=255, )
    ProjectName = fields.StringField(default='', max_length=255, )
    BuildingName = fields.StringField(default='', max_length=255, )

    BuildingInfo = fields.StringField(default='', max_length=255, )
    BuildingAddress = fields.StringField(default='', max_length=255, )
    BuildingTotalFloor = fields.StringField(default='', max_length=255, )
    BuildingHouseNum = fields.StringField(default='', max_length=255, )
    BuildingAreas = fields.StringField(default='', max_length=255, )
    BuildingStructure = fields.StringField(default='', max_length=255, )
    BuildingPreAreas = fields.StringField(default='', max_length=255, )

    meta = {
        'indexes': [
            'CurTimeStamp',
            'BuildingNo',
        ]
    }


class HouseBaseWenzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectNo = fields.StringField(default='', max_length=255, )
    BuildingNo = fields.StringField(default='', max_length=255, )
    HouseNo = fields.StringField(default='', max_length=255, )
    ProjectName = fields.StringField(default='', max_length=255, )
    BuildingName = fields.StringField(default='', max_length=255, )
    HouseRealFloor = fields.StringField(default='', max_length=255, )
    HouseId = fields.StringField(default='', max_length=255, )
    HouseAreas = fields.StringField(default='', max_length=255, )
    HouseNum = fields.StringField(default='', max_length=255, )
    HouseClass = fields.StringField(default='', max_length=255, )
    HouseSts = fields.StringField(default='', max_length=255, )
    HouseStsLatest = fields.StringField(default='', max_length=255, )

    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectNo',
            'BuildingNo',
            'HouseNo',
            'ProjectName',
            'BuildingName',
            'HouseId',
            'HouseSts',
            'HouseStsLatest',
        ]
    }


class ProjectBaseCangzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    NewCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    change_data = fields.StringField(default='', null=False)
    ProjectNo = fields.StringField(default='', max_length=255, null=False)

    ProjectName = fields.StringField(default='', max_length=255, )
    ProjectUrl = fields.StringField(default='', max_length=255, )
    PresaleNo = fields.StringField(default='', max_length=255, )
    DeveloperName = fields.StringField(default='', max_length=255, )
    BUildingNumber = fields.StringField(default='', max_length=255, )
    ProjectAddress = fields.StringField(default='', max_length=255, )
    BuildingAres = fields.StringField(default='', max_length=255, )
    DistrictName = fields.StringField(default='', max_length=255, )
    QualificationNumber = fields.StringField(default='', max_length=255, )
    QualificationLevel = fields.StringField(default='', max_length=255, )
    soldAmount = fields.IntField(default=0, index=True)
    UnsoldAmount = fields.IntField(default=0, index=True)
    soldAreas = fields.StringField(default='', max_length=255, )
    UnsoldAreas = fields.StringField(default='', max_length=255, )
    soldAddress = fields.StringField(default='', max_length=255, )
    soldPhonNumber = fields.StringField(default='', max_length=255, )
    CurrentMonthHouseSoldNumber = fields.IntField(default=0, index=True)
    CurrentMonthHouseSoldAreas = fields.StringField(default='', max_length=255, )
    CurrentMonthBusinessSoldNumber = fields.IntField(default=0, index=True)
    CurrentMonthBusinessSoldAres = fields.StringField(default='', max_length=255, )
    CurrentMonthOtherSoldNumber = fields.IntField(default=0, index=True)
    TotalHouseSoldNumber = fields.IntField(default=0, index=True)
    TotalHouseSoldAreas = fields.StringField(default='', max_length=255, )
    TotalBusinessSoldNumber = fields.IntField(default=0, index=True)
    TotalBusinessSoldAres = fields.StringField(default='', max_length=255, )
    TotalOtherSoldNumber = fields.IntField(default=0, index=True)
    HouseUnSoldNumber = fields.IntField(default=0, index=True)
    HouseUnSoldAreas = fields.StringField(default='', max_length=255, )
    BusinessUnSoldNumber = fields.IntField(default=0, index=True)
    BusinessUnSoldAres = fields.StringField(default='', max_length=255, )
    OtherUnSoldNumber = fields.IntField(default=0, index=True)
    ProjectCode = fields.StringField(default='', )
    presellInfoCode = fields.StringField(default='', )
    buildInfoCode = fields.StringField(default='', )
    tdzInfoCode = fields.StringField(default='', )
    sgxkzInfoCode = fields.StringField(default='', )
    ghxkzInfo = fields.StringField(default='', )
    jsydghxkzInfoCode = fields.StringField(default='', )
    SourceUrl = fields.URLField(default=None, blank=True)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectNo',
        ]
    }


class LandBaseCangzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    NewCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    change_data = fields.StringField(default='', null=False)
    LandNo = fields.StringField(default='', max_length=255, null=False)
    ProjectName = fields.StringField(default='', max_length=255, )
    ProjectNo = fields.StringField(default='', max_length=255, null=False)

    LandCertificateNumber = fields.StringField(default='', max_length=255, )
    LandNumber = fields.StringField(default='', max_length=255, )
    PictureNumber = fields.StringField(default='', max_length=255, )
    LandUseType = fields.StringField(default='', max_length=255, )
    LandUser = fields.StringField(default='', max_length=255, )
    LandAddress = fields.StringField(default='', max_length=255, )
    LssueDate = fields.StringField(default='', max_length=255, )
    EndDate = fields.StringField(default='', max_length=255, )
    RightAreaOfUse = fields.StringField(default='', max_length=255, )
    AcquireWay = fields.StringField(default='', max_length=255, )
    SourceUrl = fields.URLField(default=None, blank=True)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'LandNo',
        ]
    }


class PlanningBaseCangzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    NewCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    change_data = fields.StringField(default='', null=False)
    PlanningNo = fields.StringField(default='', max_length=255, null=False)
    ProjectName = fields.StringField(default='', max_length=255, )
    ProjectNo = fields.StringField(default='', max_length=255, null=False)

    LssuingAuthority = fields.StringField(default='', max_length=255, )
    PlanningPermitNumber = fields.StringField(default='', max_length=255, )
    LssueDate = fields.StringField(default='', max_length=255, )

    BuildAddress = fields.StringField(default='', max_length=255, )
    BuildOrganization = fields.StringField(default='', max_length=255, )
    BuildArea = fields.StringField(default='', max_length=255, )
    Remark = fields.StringField(default='', )
    SourceUrl = fields.URLField(default=None, blank=True)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'PlanningNo',
        ]
    }


class ConstructionBaseCangzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    NewCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    change_data = fields.StringField(default='', null=False)
    ConstructionNo = fields.StringField(default='', max_length=255, null=False)
    ProjectName = fields.StringField(default='', max_length=255, )
    ProjectNo = fields.StringField(default='', max_length=255, null=False)

    LssuingAuthority = fields.StringField(default='', max_length=255, )
    ConstructionPermitNumber = fields.StringField(default='', max_length=255, )
    LssueDate = fields.StringField(default='', max_length=255, )
    BuildProjectName = fields.StringField(default='', max_length=255, )
    BuildAddress = fields.StringField(default='', max_length=255, )
    BuildOrganization = fields.StringField(default='', max_length=255, )
    BuildArea = fields.StringField(default='', max_length=255, )
    DesignOrganization = fields.StringField(default='', max_length=255, )
    SuperviseOrganization = fields.StringField(default='', max_length=255, )
    ContractStartDate = fields.StringField(default='', max_length=255, )
    ContractEndDate = fields.StringField(default='', max_length=255, )
    ContractPrice = fields.StringField(default='', max_length=255, )
    Remark = fields.StringField(default='', )
    SourceUrl = fields.URLField(default=None, blank=True)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ConstructionNo',
        ]
    }


class ConstructionLandPlanningBaseCangzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    NewCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    change_data = fields.StringField(default='', null=False)
    ConstructionLandPlanningNo = fields.StringField(default='', max_length=255, null=False)
    ProjectName = fields.StringField(default='', max_length=255, )
    ProjectNo = fields.StringField(default='', max_length=255, null=False)

    LssuingAuthority = fields.StringField(default='', max_length=255, )
    ConstructionPermitNumber = fields.StringField(default='', max_length=255, )
    LssueDate = fields.StringField(default='', max_length=255, )
    BuildProjectName = fields.StringField(default='', max_length=255, )
    BuildAddress = fields.StringField(default='', max_length=255, )
    BuildOrganization = fields.StringField(default='', max_length=255, )
    BuildArea = fields.StringField(default='', max_length=255, )
    DesignOrganization = fields.StringField(default='', max_length=255, )
    SuperviseOrganization = fields.StringField(default='', max_length=255, )
    ContractStartDate = fields.StringField(default='', max_length=255, )
    ContractEndDate = fields.StringField(default='', max_length=255, )
    ContractPrice = fields.StringField(default='', max_length=255, )
    Remark = fields.StringField(default='', )
    SourceUrl = fields.URLField(default=None, blank=True)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'ConstructionLandPlanningNo',
        ]
    }


class DeveloperBaseCangzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    NewCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    change_data = fields.StringField(default='', null=False)
    DeveloperNo = fields.StringField(default='', max_length=255, null=False)

    QualificationNumber = fields.StringField(default='', max_length=255, )
    QualificationLevel = fields.StringField(default='', max_length=255, )
    DeveloperName = fields.StringField(default='', max_length=255, )
    DeveloperDetailUrl = fields.StringField(default='', max_length=255, )
    LegalPersonName = fields.StringField(default='', max_length=255, )
    LssueDate = fields.StringField(default='', max_length=255, )
    BusinessLicenseRegistrationNumber = fields.StringField(default='', max_length=255, )
    Territorial = fields.StringField(default='', max_length=255, )
    Email = fields.StringField(default='', max_length=255, )
    ContactsName = fields.StringField(default='', max_length=255, )
    ContactsPhone = fields.StringField(default='', max_length=255, )
    PostalCode = fields.StringField(default='', max_length=255, )
    RegisteredCapital = fields.StringField(default='', max_length=255, )
    EnterpriseIntroduction = fields.StringField(default='', )
    ScopeOperation = fields.StringField(default='', max_length=255, )
    TypeCompany = fields.StringField(default='', max_length=255, )
    QualificationEndDate = fields.StringField(default='', max_length=255, )
    DateOfApproval = fields.StringField(default='', max_length=255, )
    SourceUrl = fields.URLField(default=None, blank=True)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'DeveloperNo',
        ]
    }


class PresaleBaseCangzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(), binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    NewCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    change_data = fields.StringField(default='', null=False)
    PresaleNo = fields.StringField(default='', max_length=255, null=False)
    ProjectName = fields.StringField(default='', max_length=255, null=False)
    ProjectNo = fields.StringField(default='', max_length=255, null=False)

    PresalePermitNumber = fields.StringField(default='', max_length=255, )
    LssueDate = fields.StringField(default='', max_length=255, )
    ValidityDateStartDate = fields.StringField(default='', max_length=255, )
    ValidityDateClosingDate = fields.StringField(default='', max_length=255, )
    PresalePermitBuildingName = fields.StringField(default='', max_length=255, )
    LssuingAuthority = fields.StringField(default='', max_length=255, )
    PresaleCapitalOpenAccountBank = fields.StringField(default='', max_length=255, )
    PresaleCapitalManageAccount = fields.StringField(default='', max_length=255, )
    HouseApprovalPresaleAmount = fields.IntField(default=0, index=True)
    HouseApprovalPresaleArea = fields.StringField(default='', max_length=255, )
    BussinessApprovalPresaleAmount = fields.IntField(default=0, index=True)
    BussinessApprovalPresaleArea = fields.StringField(default='', max_length=255, )
    OtherApprovalPresaleAmount = fields.IntField(default=0, index=True)
    OtherApprovalPresaleArea = fields.StringField(default='', max_length=255, )
    SourceUrl = fields.URLField(default=None, blank=True)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'PresaleNo',
        ]
    }


class HouseBaseCangzhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    NewCurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    change_data = fields.StringField(default='', null=False)
    HouseNo = fields.StringField(default='', max_length=255, null=False)

    BuildName = fields.StringField(default='', max_length=255, null=False)
    ProjectCode = fields.StringField(default='', max_length=255, null=False)
    BuildCode = fields.StringField(default='', max_length=255, null=False)

    ProjectName = fields.StringField(default='', max_length=255, null=False)
    ProjectNo = fields.StringField(default='', max_length=255, null=False)

    HouseNum = fields.StringField(default='', max_length=255, )
    HouseDetailUrl = fields.StringField(default='', max_length=255, )
    UnitNum = fields.StringField(default='', max_length=255, )
    HouseType = fields.StringField(default='', max_length=255, )
    TotalAreas = fields.StringField(default='', max_length=255, )
    SellSchedule = fields.StringField(default='', max_length=255, )
    HouseSts = fields.StringField(default='', max_length=255, )
    HouseStsLatest = fields.StringField(default='', max_length=255, )
    HouseFloor = fields.StringField(default='', max_length=255, )
    HouseBelongSts = fields.StringField(default='', max_length=255, )
    HouseBelongStsLatest = fields.StringField(default='', max_length=255, )
    HouseNature = fields.StringField(default='', max_length=255, )
    HouseUseType = fields.StringField(default='', max_length=255, )
    UnitShape = fields.StringField(default='', max_length=255, )
    BuildingStructure = fields.StringField(default='', max_length=255, )
    ForecastBuildingArea = fields.StringField(default='', max_length=255, )
    MeasuredBuildingArea = fields.StringField(default='', max_length=255, )
    ForecastInsideOfBuildingArea = fields.StringField(default='', max_length=255, )
    MeasuredInsideOfBuildingArea = fields.StringField(default='', max_length=255, )
    ForecastPublicArea = fields.StringField(default='', max_length=255, )
    MeasuredSharedPublicArea = fields.StringField(default='', max_length=255, )
    Address = fields.StringField(default='', max_length=255, )
    SourceUrl = fields.URLField(default=None, blank=True)
    meta = {
        'indexes': [
            'CurTimeStamp',
            'HouseNo',
            'HouseSts'
        ]
    }


class Project_DetailHuizhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(), binary=True, primary_key=True, null=False,
                                choices=False)  # 记录id
    RecordTime = fields.StringField(default=str(datetime.datetime.now()), index=True)  # 记录时间
    CheackTimeLatest = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False,
                                   primary_key=False, choices=False)  # 项目uuid
    RealEstateProjectID = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 项目id
    ProjectUrl = fields.URLField(default=None, null=True, blank=True, primary_key=False,
                                 choices=False)  # 项目url
    SourceUrl = fields.URLField(default=None, null=True, blank=True, primary_key=False,
                                choices=False)  # 来源url
    AveragePrice = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 均价
    PresalePermitNumber = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 预售证编号
    ProjectName = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 项目名称
    RegionName = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 所在区域
    ProjectAddress = fields.StringField(default='', null=False, primary_key=False,
                                        choices=False)  # 惠州市惠城区金山大道与三环南路交汇处
    Developer = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 发展商
    EarliestOpeningTime = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 最早开盘时间
    GreeningRate = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 绿化率
    FloorAreaRatio = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 容积率
    DistrictName = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 行政区
    ManagementFees = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 物业费
    ManagementCompany = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 物业公司
    TotalBuidlingArea = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 总建筑面积
    FloorArea = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 占地面积
    ParkingSpaceAmount = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 车位套数
    ProjectInformation = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 项目信息
    HouseBuildingCount = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 楼幢总数
    HousingCount = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 总户数
    PropertyRightsDescription = fields.StringField(default='', null=False, primary_key=False,
                                                   choices=False)  # 产权年限描述
    Decoration = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 装修
    Project_LivingTime = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 入住时间
    BuildingType = fields.StringField(default='', null=False, primary_key=False,
                                      choices=False)  # 建筑类型 低层/多层/中高层/高层/超高层
    Project_Traffic = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 项目交通
    Project_Introduce = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 项目介绍
    Project_Surround = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 项目周边
    ProjectLandNumber = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 国土证号
    Project_Feature = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 项目特色
    ProjectBlock = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 版块
    ProjectHouseType = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 物业类别
    ProjectMainShape = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 主力户型
    ParkingSpaceMatching = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 车位配比
    HouseSoldAmount = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 已售套数
    HouseUnsoldAmount = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 未售套数
    DeveloperLevel = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 资质等级
    DeveloperPermitNumber = fields.StringField(default='', null=False, primary_key=False,
                                               choices=False)  # 开发商资质证书
    SaleTelphoneNumber = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 销售电话
    meta = {
        'indexes': [
            'RecordTime',
            'ProjectUUID',
            'ProjectUrl',
            'ProjectName',
            'ProjectBlock'

        ]
    }


class Certificate_DetailHuizhou(Document):
    RecordID = fields.UUIDField(default = uuid.uuid1(), binary = True, primary_key = True, null = False,
                                choices = False)  # 记录id
    RecordTime = fields.StringField(default = str(datetime.datetime.now()), index = True)  # 记录时间
    CheackTimeLatest = fields.StringField(default = str(datetime.datetime.now()), index = True)
    ProjectUUID = fields.UUIDField(default = uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary = False, null = False,
                                   primary_key = False, choices = False)  # 项目uuid
    PresalePermitNumberUUID = fields.UUIDField(default = uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary = False,
                                               null = False, primary_key = False, choices = False)  # 预售证uuid
    RealEstateProjectID = fields.StringField(default = '', null = False, primary_key = False, choices = False)  # 项目id
    PresalePermitUrl = fields.StringField(default = '', null = False, primary_key = False, choices = False)  # 预售证url
    SourceUrl = fields.StringField(default = '', null = False, primary_key = False, choices = False)  # 来源url
    ProjectName = fields.StringField(default = '', null = False, primary_key = False, choices = False)
    PresalePermitNumber = fields.StringField(default = '', null = False, primary_key = False, choices = False)  # 预售证编号
    LssuingAuthority = fields.StringField(default = '', null = False, primary_key = False, choices = False)  # 发证机关
    PresaleTotalBuidlingArea = fields.StringField(default = '', null = False, primary_key = False,
                                                  choices = False)  # 预售总建筑面积
    ValidityDateStartDate = fields.StringField(default = '', null = False, primary_key = False,
                                               choices = False)  # 有效期起始日期
    ValidityDateClosingDate = fields.StringField(default = '', null = False, primary_key = False,
                                                 choices = False)  # 有效期截止日期
    LssueDate = fields.StringField(default = '', null = False, primary_key = False, choices = False)  # 发证日期
    Bank_Account = fields.StringField(default = '', null = False, primary_key = False, choices = False)  # 预售款专用帐户
    Remarks = fields.StringField(default = '', null = False, primary_key = False, choices = False)  # 备注
    BuiltFloorCount = fields.StringField(default = '', null = False, primary_key = False, choices = False)  # 发证时各栋已建层数
    PresaleHousingLandIsMortgage = fields.StringField(default = '', null = False, primary_key = False,
                                                      choices = False)  # 土地是否抵押
    LivingArea = fields.StringField(default = '', null = False, primary_key = False, choices = False)  # 住宅面积
    BusinessArea = fields.StringField(default = '', null = False, primary_key = False, choices = False)  # 商业用房面积
    OtherArea = fields.StringField(default = '', null = False, primary_key = False, choices = False)  # 其它面积
    PresaleBuildingNo = fields.StringField(default = '', null = False, primary_key = False,
                                           choices = False)  # 预售房屋栋号及层数                                #预售房屋栋号及层数
    PresaleHouseCount = fields.StringField(default = '', null = False, primary_key = False,
                                           choices = False)  # 本期总单元套数
    DeveloperPermitNumber = fields.StringField(default = '', null = False, primary_key = False,
                                               choices = False)  # 开发商资质证书
    LandNumberAndUse = fields.StringField(default = '', null = False, primary_key = False,
                                          choices = False)  # 土地使用权证号及用途
    meta = {
        'indexes': [
            'RecordTime',
            'PresalePermitNumberUUID',
            'ProjectUUID',
            'PresalePermitNumber',

        ]
    }


class Building_DetailHuizhou(Document):
    RecordID = fields.UUIDField(default = uuid.uuid1(), binary = True, primary_key = True, null = False,
                                choices = False)  # 记录id
    RecordTime = fields.StringField(default = str(datetime.datetime.now()), index = True)  # 记录时间
    CheackTimeLatest = fields.StringField(default = str(datetime.datetime.now()), index = True)
    ProjectUUID = fields.UUIDField(default = uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary = False, null = False,
                                   primary_key = False, choices = False)  # 项目uuid
    PresalePermitNumberUUID = fields.StringField(default = '') # 预售证uuid
    BuildingUUID = fields.UUIDField(default = uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary = False, null = False,
                                    primary_key = False, choices = False)  # 楼栋uuid
    BuildingID = fields.StringField(default = '', null = False, primary_key = False, choices = False)  # 楼栋id
    PresalePermitNumber = fields.StringField(default = '', null = False, primary_key = False, choices = False)  # 预售证编号
    BuildingUrl = fields.URLField(default = None, null = True, blank = True, primary_key = False,
                                  choices = False)  # 楼栋url
    SourceUrl = fields.URLField(default = None, null = True, blank = True, primary_key = False,
                                choices = False)  # 来源url
    ProjectName = fields.StringField(default = '', null = False, primary_key = False, choices = False)  # 项目名称
    BuildingName = fields.StringField(default = '', null = False, primary_key = False, choices = False)  # 楼栋名称
    BuildingNumber = fields.StringField(default = '', null = False, primary_key = False, choices = False)  # 楼栋号码
    meta = {
        'indexes': [
            'RecordTime',
            'ProjectUUID',
            'BuildingUUID',
            'PresalePermitNumberUUID',
        ]
    }


class House_DetailHuizhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(), binary=True, primary_key=True, null=False,
                                choices=False)  # 记录id
    RecordTime = fields.StringField(default=str(datetime.datetime.now()), index=True)  # 记录时间
    CheackTimeLatest = fields.StringField(default=str(datetime.datetime.now()), index=True)  # 最新爬取时间

    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False,
                                   primary_key=False, choices=False)  # 项目uuid
    PresalePermitNumberUUID = fields.StringField(default='')  # 预售证uuid
    BuildingUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False,
                                    primary_key=False, choices=False)  # 楼栋uuid
    HouseUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''), binary=False, null=False,
                                 primary_key=False, choices=False)  # 户uuid

    HouseID = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 户id

    HouseUrl = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 户url
    SourceUrl = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 来源url

    BuildingNumber = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 楼栋号码
    ProjectName = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 项目名称
    BuildingName = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 楼栋名称
    FloorName = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 层名
    HouseName = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 用途类型
    HouseUseType = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 用途
    UnitShape = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 户型
    Toward = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 朝向
    HouseUse = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 房屋功能
    FloorHight = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 层高
    BuildingStructure = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 建筑结构
    SalePriceList = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 商品房销售价目表
    HouseSaleState = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 销售状态

    ForecastBuildingArea = fields.StringField(default='', null=False, primary_key=False,
                                              choices=False)  # 预测建筑面积
    ForecastInsideOfBuildingArea = fields.StringField(default='', null=False, primary_key=False,
                                                      choices=False)  # 预测套内面积
    ForecastPublicArea = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 预测公摊面积
    MeasuredBuildingArea = fields.StringField(default='', null=False, primary_key=False,
                                              choices=False)  # 实测建筑面积
    MeasuredInsideOfBuildingArea = fields.StringField(default='', null=False, primary_key=False,
                                                      choices=False)  # 实测套内面积
    MeasuredSharedPublicArea = fields.StringField(default='', null=False, primary_key=False,
                                                  choices=False)  # 实测公摊面积
    SalePriceByBuildingArea = fields.StringField(default='', null=False, primary_key=False,
                                                 choices=False)  # 按建筑面积拟售单价
    SalePriceByQuantiy = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 备案价(元/套

    IsMortgage = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 是否抵押
    IsAttachment = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 是否查封
    IsMoveBack = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 是否回迁
    IsPrivateUse = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 是否自用
    IsPublicMating = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 是否公建配套
    IsPermitSale = fields.StringField(default='', null=False, primary_key=False, choices=False)

    Balconys = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 封闭阳台数量
    UnenclosedBalconys = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 非封闭阳台
    Kitchens = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 厨房
    Toilets = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 卫生间数量
    Address = fields.StringField(default='', null=False, primary_key=False, choices=False)  # 地址
    HouseSaleStateLatest = fields.StringField(default='', null=False, primary_key=False,
                                              choices=False)  # 上一次销售状态
    ComplateTag = fields.IntField(default=0, null=True, primary_key=False, choices=False)
    meta = {
        'indexes': [
            "ProjectUUID",
            "PresalePermitNumberUUID",
            "BuildingUUID",
            "HouseUUID",
            "HouseID",
            'HouseUrl',
            'RecordTime',
            'CheackTimeLatest',
            'HouseSaleStateLatest',
            'HouseSaleState'
        ]
    }


class web_countHuizhou(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(), binary=True, primary_key=True, null=False)  # 记录id
    RecordTime = fields.StringField(default=str(datetime.datetime.now()), index=True)  # 记录时间
    riqi = fields.StringField(default='')
    wangshangqianyue_taoshu = fields.StringField(default='')
    wangshangqianyue_mianji = fields.StringField(default='')
    wangshangqianyue_zhuzhaitaoshu = fields.StringField(default='')
    wangshangqianyue_zhuzhaimianji = fields.StringField(default='')
    wangshangqianyuedengji_taoshu = fields.StringField(default='')
    wangshangqianyuedengji_mianji = fields.StringField(default='')
    wangshangqianyuedengji_zhuzhaitaoshu = fields.StringField(default='')
    wangshangqianyuedengji_zhuzhaimianji = fields.StringField(default='')


class ProjectBaseXian(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=255, null=False)
    ProjectRoomType = fields.StringField(default='', max_length=255, null=False)
    ProjectHotSales = fields.StringField(default='', max_length=255, null=False)
    ProjectAddress = fields.StringField(default='', max_length=255, null=False)
    ProjectCompany = fields.StringField(default='', max_length=255, null=False)
    ProjectPhoneNum = fields.StringField(default='', max_length=255, null=False)
    ProjectPrice = fields.StringField(default='', max_length=255, null=False)
    ProjectBaseSubURL = fields.StringField(default='', max_length=255, null=False)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
            'ProjectBaseSubURL',
        ]
    }


class ProjectInfoXian(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectName = fields.StringField(default='', max_length=255, null=False)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectCompany = fields.StringField(default='', max_length=255, null=False)
    ProjectDueDate = fields.StringField(default='', max_length=255, null=False)
    ProjectInfoURL = fields.StringField(default='', max_length=255, null=False)
    ProjectCompanyURL = fields.StringField(default='', max_length=255, null=False)
    ProjectPresaleURL = fields.StringField(default='', max_length=255, null=False)

    ProjectAddress = fields.StringField(default='', max_length=255, null=False)
    ProjectSalesAddress = fields.StringField(default='', max_length=255, null=False)
    ProjectCityArea = fields.StringField(default='', max_length=255, null=False)
    ProjectTradeCircle = fields.StringField(default='', max_length=255, null=False)
    PropertyType = fields.StringField(default='', max_length=255, null=False)
    ProjectFirstDueDate = fields.StringField(default='', max_length=255, null=False)
    ProjectMainRoomType = fields.StringField(default='', max_length=255, null=False)
    ProjectDekoration = fields.StringField(default='', max_length=255, null=False)
    ProjectBuildType = fields.StringField(default='', max_length=255, null=False)
    ProjectBrief = fields.StringField(default='', max_length=255, null=False)
    ProjectTotalFlat = fields.StringField(default='', max_length=255, null=False)
    PropertyCost = fields.StringField(default='', max_length=255, null=False)
    ProjectSupplyType = fields.StringField(default='', max_length=255, null=False)
    ProjectContainRoomType = fields.StringField(default='', max_length=255, null=False)
    ProjectLoopLine = fields.StringField(default='', max_length=255, null=False)
    ProjectParkingSpace = fields.StringField(default='', max_length=255, null=False)
    LandUseLife = fields.StringField(default='', max_length=255, null=False)
    PeripheryEducation = fields.StringField(default='', max_length=255, null=False)
    PeripheryCommerce = fields.StringField(default='', max_length=255, null=False)
    PeripheryBank = fields.StringField(default='', max_length=255, null=False)
    PeripheryHospital = fields.StringField(default='', max_length=255, null=False)
    PeripheryTraffic = fields.StringField(default='', max_length=255, null=False)
    PeripheryRestaurant = fields.StringField(default='', max_length=255, null=False)
    PeripheryOthers = fields.StringField(default='', max_length=255, null=False)
    BuildingStructure = fields.StringField(default='', max_length=255, null=False)
    BuildingArea = fields.StringField(default='', max_length=255, null=False)
    BuildingFloorSpace = fields.StringField(default='', max_length=255, null=False)
    MaxBuildingFlats = fields.StringField(default='', max_length=255, null=False)
    MinBuildingFlats = fields.StringField(default='', max_length=255, null=False)
    ProjectDevCompany = fields.StringField(default='', max_length=255, null=False)
    PropertyCompany = fields.StringField(default='', max_length=255, null=False)
    IsCompletion = fields.StringField(default='', max_length=16, null=False)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
            'ProjectPresaleURL',
        ]
    }


class PresaleInfoXian(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=255, null=False)
    PresaleCode = fields.StringField(default='', max_length=255, null=False)
    PresaleUUID = fields.StringField(default='', max_length=255, null=False)
    BuildingRecordName = fields.StringField(default='', max_length=255, null=False)
    DevCompany = fields.StringField(default='', max_length=255, null=False)
    LicenseDate = fields.StringField(default='', max_length=255, null=False)
    SuperviseBank = fields.StringField(default='', max_length=255, null=False)
    SuperviseBankAccount = fields.StringField(default='', max_length=255, null=False)
    BuildingList = fields.StringField(default='', max_length=255, null=False)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
            'PresaleUUID',
            'PresaleCode',
            # 'BuildingList'
        ]
    }


class BuildingInfoXian(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=255, null=False)
    PresaleUUID = fields.StringField(default='', max_length=255, null=False)
    PresaleCode = fields.StringField(default='', max_length=255, null=False)
    BuildingUUID = fields.StringField(default='', max_length=255, null=False)
    BuildingName = fields.StringField(default='', max_length=255, null=False)
    BuildingURL = fields.StringField(default='', max_length=255, null=False)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
            'PresaleUUID',
            'PresaleCode',
            'BuildingName',
            'BuildingUUID',
            'BuildingURL',
            # 'BuildingList'
        ]
    }


class HouseInfoXian(Document):
    RecordID = fields.UUIDField(default=uuid.uuid1(),
                                binary=True, primary_key=True, null=False)
    CurTimeStamp = fields.StringField(default=str(datetime.datetime.now()), index=True)
    ProjectUUID = fields.UUIDField(default=uuid.uuid3(uuid.NAMESPACE_DNS, ''),
                                   binary=False, null=False)
    ProjectName = fields.StringField(default='', max_length=255, null=False)
    BuildingUUID = fields.StringField(default='', max_length=255, null=False)
    BuildingName = fields.StringField(default='', max_length=255, null=False)
    BuildingNum = fields.StringField(default='', max_length=255, null=False)
    HouseUUID = fields.StringField(default='', max_length=255, null=False)
    HouseUnit = fields.StringField(default='', max_length=255, null=False)
    HouseRoomNum = fields.StringField(default='', max_length=255, null=False)
    HouseFloor = fields.StringField(default='', max_length=255, null=False)
    HouseRoomType = fields.StringField(default='', max_length=255, null=False)
    HouseUsage = fields.StringField(default='', max_length=255, null=False)
    HouseType = fields.StringField(default='', max_length=255, null=False)
    HouseBuildingArea = fields.StringField(default='', max_length=255, null=False)
    HouseSaleState = fields.StringField(default='', max_length=255, null=False)
    HouseSaleStateLatest = fields.StringField(default='', max_length=255, null=False)

    meta = {
        'indexes': [
            'CurTimeStamp',
            'ProjectUUID',
            'ProjectName',
            'BuildingUUID',
            'BuildingName',
            'HouseUUID',
            'HouseUnit',
            'HouseRoomNum',
            'HouseSaleState',
            'HouseSaleStateLatest',
        ]
    }
