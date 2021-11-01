# coding=utf-8
import winxuan

########################################################################
"""查询区域"""

class Request(winxuan.baseInterface.BaseReq):
    def __init__(self, id = None):#, itemIds, fields = None):
        
        """Constructor"""
        if id:
            self.id = id
