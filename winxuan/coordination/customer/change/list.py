# coding=utf-8
import winxuan

########################################################################
"""协同客户信息变动列表查询"""

class Request(winxuan.baseInterface.BaseReq):
    def __init__(self, changeStartTime, changeEndTime = None):
        
        """Constructor"""
        self.changeStartTime = changeStartTime
        if changeEndTime:
            self.changeEndTime = changeEndTime
        