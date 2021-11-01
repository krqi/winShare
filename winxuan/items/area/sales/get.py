# coding=utf-8
import winxuan

########################################################################
"""查询文轩图书区域销售TOP1000商品数据"""

class Request(winxuan.baseInterface.BaseReq):
    def __init__(self, periodType, province = None, city = None, mcType = None, ):
        self.periodType = periodType
        if province:
            self.province = province
        if city:
            self.city = city
        if mcType:
            self.mcType = mcType
            