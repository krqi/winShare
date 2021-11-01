# coding=utf-8
import winxuan

########################################################################
"""商品编码转换SAP编码"""

class Request(winxuan.baseInterface.BaseReq):
    def __init__(self, ecIds):
        
        """Constructor"""
        self.ecIds = ecIds
        