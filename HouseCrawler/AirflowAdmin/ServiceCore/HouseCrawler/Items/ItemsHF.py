# coding = utf-8
from scrapy_djangoitem import DjangoItem
from HouseNew.models import *


class ProjectBaseItem(DjangoItem):
    django_model = None


class ProjectInfoItem(DjangoItem):
    django_model = ProjectInfoHefei


class BuildingInfoItem(DjangoItem):
    django_model = BuildingInfoHefei


class HouseInfoItem(DjangoItem):
    django_model = HouseInfoHefei
