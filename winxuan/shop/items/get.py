# coding=utf-8
import winxuan

########################################################################
"""批量查询店铺商品详细信息"""

class Request(winxuan.baseInterface.BaseReq):
    
    #itemIds 商品id(文轩商品编码)，支持多个商品用，号分开。列表限制：20,字符长度550
    def __init__(self, itemIds, fields = None):
        """Constructor"""
        self.itemIds = itemIds
        if fields:
            self.fields = fields
        