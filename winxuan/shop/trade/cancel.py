# coding=utf-8
import winxuan

########################################################################
"""取消店铺交易单,在[WAIT_DELIVERY]等待出库之前可以取消."""

class Request(winxuan.baseInterface.BaseReq):
    def __init__(self, wxTradeId, reason):
        
        """Constructor"""
        self.wxTradeId = wxTradeId
        self.reason = reason
        