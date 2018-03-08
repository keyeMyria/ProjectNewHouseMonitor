# coding = utf-8
from scrapy_djangoitem import DjangoItem
from HouseNew.models import *


class ProjectInfoItem(DjangoItem):
    django_model = ProjectInfoXuzhou
    fields_map = {'RecordTime': '',
                  'ProjectName': 'ProjectName',
                  'PromotionName': 'PromotionName',
                  'RealEstateProjectID': '',
                  'ProjectUUID': 'ProjectUUID',
                  'DistrictName': 'DistrictName',
                  'RegionName': '',
                  'ProjectAddress': 'ProjectAddress',
                  'ProjectType': '',
                  'OnSaleState': 'OnSaleState',
                  'LandUse': '',
                  'HousingCount': '',
                  'Developer': 'Developer',
                  'FloorArea': '',
                  'TotalBuidlingArea': 'TotalBuidlingArea',
                  'BuildingType': '',
                  'HouseUseType': 'HouseUseType',
                  'PropertyRightsDescription': 'PropertyRightsDescription',
                  'ProjectApproveData': '',
                  'ProjectBookingData': '',
                  'LssueDate': '',
                  'PresalePermitNumber': '',
                  'HouseBuildingCount': '',
                  'ApprovalPresaleAmount': 'ApprovalPresaleAmount',
                  'ApprovalPresaleArea': 'ApprovalPresaleArea',
                  'AveragePrice': 'AveragePrice',
                  'EarliestStartDate': '',
                  'CompletionDate': '',
                  'EarliestOpeningTime': 'EarliestOpeningDate',
                  'LatestDeliversHouseDate': '',
                  'PresaleRegistrationManagementDepartment': '',
                  'LandLevel': '',
                  'GreeningRate': 'GreeningRate',
                  'FloorAreaRatio': 'FloorAreaRatio',
                  'ManagementFees': 'ManagementFees',
                  'ManagementCompany': '',
                  'OtheRights': '',
                  'CertificateOfUseOfStateOwnedLand': '',
                  'ConstructionPermitNumber': '',
                  'QualificationNumber': '',
                  'LandUsePermit': '',
                  'BuildingPermit': '',
                  'LegalPersonNumber': '',
                  'LegalPerson': '',
                  'SourceUrl': 'SourceUrl',
                  'Decoration': '',
                  'ParkingSpaceAmount': 'ParkingSpaceAmount',
                  'Remarks': '',
                  'ExtraJson': '',
                  }


class PresellInfoItem(DjangoItem):
    django_model = PresellInfoXuzhou
    fields_map = {'RecordTime': '',
                  'ProjectName': 'ProjectName',
                  'RealEstateProjectID': '',
                  'ProjectUUID': 'ProjectUUID',
                  'PresalePermitNumber': 'PresalePermitNumber',
                  'TotalBuidlingArea': '',
                  'ApprovalPresaleAmount': 'ApprovalPresaleAmount',
                  'ApprovalPresaleArea': 'TotalArea',
                  'ApprovalPresaleHouseAmount': '',
                  'ApprovalPresaleHouseArea': '',
                  'PresaleBuildingAmount': 'SaleScope',
                  'ConstructionFloorCount': '',
                  'BuiltFloorCount': '',
                  'PeriodsCount': '',
                  'ConstructionTotalArea': '',
                  'GroundArea': '',
                  'UnderGroundArea': '',
                  'PresaleTotalBuidlingArea': 'PresaleArea',
                  'Contacts': 'SalePhone',
                  'PresaleBuildingSupportingAreaInfo': '',
                  'PresaleHousingLandIsMortgage': '',
                  'ValidityDateStartDate': '',
                  'ValidityDateClosingDate': '',
                  'LssueDate': 'LssueDate',
                  'LssuingAuthority': '',
                  'PresaleRegistrationManagementDepartment': '',
                  'ValidityDateDescribe': '',
                  'ApprovalPresalePosition': '',
                  'LandUse': 'LandUse',
                  'EarliestStartDate': '',
                  'LatestDeliversHouseDate': '',
                  'EarliestOpeningDate': '',
                  'HouseSpread': '',
                  'PresalePermitTie': '',
                  'PresaleHouseCount/PresaleUnitCount': '',
                  'Remarks': '',
                  'SourceUrl': '',
                  'ExtraJson': '',
                  }


class HouseInfoItem(DjangoItem):
    django_model = HouseInfoXuzhou
    fields_map = {'RecordTime': '',
                  'CaseTime': '',
                  'ProjectName': 'ProjectName',
                  'RealEstateProjectID': '',
                  'BuildingName': 'BuildingName',
                  'BuildingID': '',
                  'DistrictName': '',
                  'UnitName': 'UnitName',
                  'UnitID': '',
                  'HouseNumber': '',
                  'HouseName': 'HouseName',
                  'HouseID': '',
                  'HouseUUID': 'HouseUUID',
                  'Address': '',
                  'FloorName': '',
                  'ActualFloor': '',
                  'FloorCount': '',
                  'FloorType': '',
                  'FloorHight': '',
                  'UnitShape': '',
                  'UnitStructure': '',
                  'Rooms': '',
                  'Halls': '',
                  'Kitchens': '',
                  'Toilets': '',
                  'Balconys': '',
                  'UnenclosedBalconys': '',
                  'HouseShape': '',
                  'Dwelling': '',
                  'ForecastBuildingArea': '',
                  'ForecastInsideOfBuildingArea': '',
                  'ForecastPublicArea': '',
                  'MeasuredBuildingArea': 'MeasuredBuildingArea',
                  'MeasuredInsideOfBuildingArea': 'MeasuredInsideOfBuildingArea',
                  'MeasuredSharedPublicArea': 'MeasuredSharedPublicArea',
                  'MeasuredUndergroundArea': '',
                  'Toward': '',
                  'HouseType': '',
                  'HouseNature': '',
                  'Decoration': '',
                  'NatureOfPropertyRight': '',
                  'HouseUseType': 'HouseUseType',
                  'BuildingStructure': 'BuildingStructure',
                  'HouseSalePrice': '',
                  'SalePriceByBuildingArea': '',
                  'SalePriceByInsideOfBuildingArea': '',
                  'IsMortgage': '',
                  'IsAttachment': '',
                  'IsPrivateUse': '',
                  'IsMoveBack': '',
                  'IsSharedPublicMatching': '',
                  'SellState': '',
                  'SellSchedule': '',
                  'HouseState': 'HouseState',
                  'HouseStateLatest': 'HouseStateLatest',
                  'HouseLabel': '',
                  'HouseLabelLatest': '',
                  'TotalPrice': '',
                  'Price': '',
                  'PriceType': '',
                  'DecorationPrice': '',
                  'Remarks': '',
                  'SourceUrl': '',
                  'ExtraJson': '',
                  }


class BuildingInfoItem(DjangoItem):
    django_model = BuildingInfoXuzhou
    fields_map = {'RecordTime': '',
                  'ProjectName': 'ProjectName',
                  'RealEstateProjectID': '',
                  'BuildingName': 'BuildingName',
                  'BuildingID': '',
                  'BuildingUUID': 'BuildingUUID',
                  'UnitName': '',
                  'UnitID': '',
                  'PresalePermitNumber': 'PresalePermitNumber',
                  'Address': '',
                  'OnTheGroundFloor': '',
                  'TheGroundFloor': '',
                  'EstimatedCompletionDate': '',
                  'HousingCount': 'ApprovalPresaleAmount',
                  'Floors': '',
                  'ElevatorHouse': '',
                  'IsHasElevator': '',
                  'ElevaltorInfo': '',
                  'BuildingStructure': '',
                  'BuildingType': '',
                  'BuildingHeight': '',
                  'BuildingCategory': '',
                  'Units': '',
                  'UnsoldAmount': 'UnsoldAmount',
                  'BuildingAveragePrice': '',
                  'BuildingPriceRange': '',
                  'BuildingArea': '',
                  'Remarks': '',
                  'SourceUrl': '',
                  'ExtraJson': '',
                  }