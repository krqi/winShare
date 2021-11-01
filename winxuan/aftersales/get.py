# coding=utf-8
import winxuan

########################################################################
"""检索单个售后单信息"""

class Request(winxuan.baseInterface.BaseReq):
    def __init__(self, aftersalesId, fields = None):
        
        """Constructor"""
        self.aftersalesId = aftersalesId
        if fields:
            self.fields = fields
            