# coding=utf-8
import winxuan

########################################################################
"""根据条件检索店铺交易单信息"""

class Request(winxuan.baseInterface.BaseReq):
    def __init__(self, status = None, startPurchaseTime = None, endPurchaseTime = None, pageNum = None, pageSize = None):
        
        """Constructor"""
        if status:
            self.status = status
        if startPurchaseTime:
            self.startPurchaseTime = startPurchaseTime
        if endPurchaseTime:
            self.endPurchaseTime = endPurchaseTime
        if pageNum:
            self.pageNum = pageNum
        if pageSize:
            self.pageSize = pageSize
        