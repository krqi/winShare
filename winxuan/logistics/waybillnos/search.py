# coding=utf-8
import winxuan

########################################################################
"""根据条件检索运单号"""

class Request(winxuan.baseInterface.BaseReq):
    def __init__(self, startTime, endTime = None, pageNo = None, pageSize = None, status = None):
        
        """Constructor"""
        self.startTime = startTime
        if endTime:
            self.endTime = endTime
        if pageNo:
            self.pageNo = pageNo
        if pageSize:
            self.pageSize = pageSize
        if status:
            self.status = status
        