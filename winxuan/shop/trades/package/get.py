# coding=utf-8
import winxuan

########################################################################
"""查询交易单发货商品包裹信息(发货12小时后方可查询到包裹信息)"""

class Request(winxuan.baseInterface.BaseReq):
    def __init__(self, wxTradeIds):
        
        """Constructor"""
        if len(wxTradeIds) > 449:
            raise Exception('字符长度超过限制')
        self.wxTradeIds = wxTradeIds #wxTradeId(文轩交易单号)，支持多个单号用英文逗号分开 列表限制：20,字符长度550
