# coding=utf-8
import winxuan

########################################################################

"""批量查询店铺商品库存信息"""
class Request(winxuan.baseInterface.BaseReq):
    # itemIds 商品id(文轩商品编码)，支持多个商品用，号分开。列表限制：20,字符长度550
    def __init__(self, itemIds):
        
        """Constructor"""
        self.itemIds = itemIds
