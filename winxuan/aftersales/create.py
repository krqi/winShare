# coding=utf-8
import winxuan

########################################################################
"""创建售后单"""

class Request(winxuan.baseInterface.BaseReq):
    def __init__(self, wxTradeId, responsible, outerAftersales, holder, reason, type, deliveryCompany, deliveryCode, items, remark = None):
        
        """Constructor"""
        self.wxTradeId = wxTradeId
        self.responsible = responsible
        self.outerAftersales = outerAftersales
        self.holder = holder
        self.reason = reason
        self.type = type
        self.deliveryCompany = deliveryCompany
        self.deliveryCode = deliveryCode
        self.items = items
        if remark:
            self.remark = remark
