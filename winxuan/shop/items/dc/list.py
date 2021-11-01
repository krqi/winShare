# coding=utf-8
import winxuan

########################################################################
"""查询店铺商品分仓库存"""

class Request(winxuan.baseInterface.BaseReq):
    def __init__(self, itemIds):
        
        """Constructor"""
        self.itemIds = itemIds
