# coding=utf-8
import winxuan

########################################################################
"""根据条件检索售后单信息"""

class Request(winxuan.baseInterface.BaseReq):
    def __init__(self, wxTradeId = None, status = None, startCreateTime = None, endCreateTime = None, 
                 pageNum = None, pageSize = None, deliveryCodes = None):
        
        """Constructor"""
        if wxTradeId:
            self.wxTradeId = wxTradeId
        if status:
            self.status = status
        if startCreateTime:
            self.startCreateTime = startCreateTime
        if endCreateTime:
            self.endCreateTime = endCreateTime
        if pageNum:
            self.pageNum = pageNum
        if pageSize:
            self.pageSize = pageSize
        if deliveryCodes:
            self.deliveryCodes = deliveryCodes
            