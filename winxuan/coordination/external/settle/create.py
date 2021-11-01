# coding=utf-8
import winxuan

########################################################################
"""协同客户外部结算申请创建"""

class Request(winxuan.baseInterface.BaseReq):
    def __init__(self, bill, externalSettleRequisitions):
        
        """Constructor"""
        self.bill = bill
        self.externalSettleRequisitions = externalSettleRequisitions
        