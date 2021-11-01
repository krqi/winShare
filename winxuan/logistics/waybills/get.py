# coding=utf-8
import winxuan

########################################################################
"""批量查询运单信息"""

class Request(winxuan.baseInterface.BaseReq):
    def __init__(self, waybillNos):
        
        """Constructor"""
        self.waybillNos = waybillNos
        