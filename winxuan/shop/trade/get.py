# coding=utf-8
import winxuan

########################################################################
"""检索单个店铺交易单信息"""

class Request(winxuan.baseInterface.BaseReq):
    def __init__(self, outerTrade = None, wxTradeId = None, fields = None): #内外部交易号必选其中之一
        
        """Constructor"""
        if not (outerTrade or wxTradeId):
            raise Exception('必须输入外部交易号或者文轩交易号其中之一')
            
        if outerTrade:
            self.outerTrade = outerTrade
        if wxTradeId:
            self.wxTradeId = wxTradeId
        if fields:
            self.fields = fields
        