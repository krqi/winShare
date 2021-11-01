# coding=utf-8
import winxuan

########################################################################
"""协同客户外部结算申请查询"""

class Request(winxuan.baseInterface.BaseReq):
    def __init__(self, bill,
                 pageNo = None,
                 pageSize = None,
                 outerOrder = None,
                 itemId = None,
                 outerItem = None):
        
        """Constructor"""
        self.bill = bill
        if pageNo:
            self.pageNo = pageNo
        if pageSize:
            self.pageSize = pageSize
        if outerOrder:
            self.outerOrder = outerOrder
        if itemId:
            self.itemId = itemId
        if outerItem:
            self.outerItem = outerItem        
