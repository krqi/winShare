# coding=utf-8
import winxuan

########################################################################
"""查询店铺商品营销分类"""

class Request(winxuan.baseInterface.BaseReq):
    def __init__(self, ocCode = None, parentOcCode = None):
        
        """Constructor"""
        if ocCode: #如R1100,R1200,最大长度：20,商品营销分类编码列表;code用英文逗号分隔
            self.ocCode = ocCode
        if parentOcCode: #如R1000,最大长度：20，父分类编码
            self.parentOcCode = parentOcCode
            
        #(parentOcCode、ocCode都不填写,默认查询顶级父图书分类,Code为R1000;
        #只传ocCode列表,查询当前列表分类;
        #只传parentOcCode,查询当前父分类的所有子分类;
        #两个参数都传,查询给定分类与给定父分类所有子分类的交集)
        