# coding=utf-8
import winxuan

########################################################################
"""批量修改运单状态"""

class Request(winxuan.baseInterface.BaseReq):
    def __init__(self, waybillNos):
        
        """Constructor"""
        self.waybillNos = waybillNos
