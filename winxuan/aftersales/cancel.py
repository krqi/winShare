# coding=utf-8
import winxuan

########################################################################
"""取消售后单"""

class Request(winxuan.baseInterface.BaseReq):
    def __init__(self, aftersalesId):
        
        """Constructor"""
        self.aftersalesId = aftersalesId
        