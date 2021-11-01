# coding=utf-8
import winxuan

########################################################################
"""SAP编码转换商品编码"""

class Request(winxuan.baseInterface.BaseReq):
    def __init__(self, sapIds):
        
        """Constructor"""
        self.itemIds = sapIds
