# coding=utf-8
import winxuan

########################################################################
"""查询账务账目明细列表"""

class Request(winxuan.baseInterface.BaseReq):
    def __init__(self, type, startTime, endTime = None, pageNo = None, pageSize = None):
        
        """Constructor"""
        self.type = type
        self.startTime = startTime
        if endTime:
            self.endTime = endTime
        if pageNo:
            self.pageNo = pageNo
        if pageSize:
            self.pageSize = pageSize
    