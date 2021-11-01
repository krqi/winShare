# coding=utf-8
import winxuan

########################################################################
"""批量查询限价商品"""

class Request(winxuan.baseInterface.BaseReq):
    def __init__(self, changeStartTime, changeEndTime = None, pageSize = None, pageNo = None):
        
        """Constructor"""
        self.changeStartTime = changeStartTime
        if changeEndTime:
            self.changeEndTime = changeEndTime
        if pageSize:
            self.pageSize = pageSize
        if pageNo:
            self.pageNo = pageNo
