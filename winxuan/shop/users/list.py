# coding=utf-8
import winxuan

########################################################################

class Request(winxuan.baseInterface.BaseReq):
    """查询用户列表"""
    def __init__(self, pageSize = None, pageNo = None):
        #pageSize 分页数量,默认为50,最大不能超过200
        #pageNo	分页页码,默认为1
        
        """Constructor"""
        if pageSize:
            self.pageSize = pageSize
        if pageNo:
            self.pageNo = pageNo
        