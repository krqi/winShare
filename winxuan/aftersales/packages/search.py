# coding=utf-8
import winxuan

########################################################################
"""售后单包件查询"""

class Request(winxuan.baseInterface.BaseReq):
    def __init__(self, signStartTime = None, signEndTime = None, deliveryCodes = None, 
                 packageId = None, pageNum = None, pageSize = None):
        
        """Constructor"""
        if signStartTime:
            self.signStartTime = signStartTime
        if signEndTime:
            self.signEndTime = signEndTime
        if deliveryCodes:
            self.deliveryCodes = deliveryCodes
        if packageId:
            self.packageId = packageId
        if pageNum:
            self.pageNum = pageNum
        if pageSize:
            self.pageSize = pageSize
