# coding=utf-8
import winxuan

########################################################################
"""创建店铺交易单"""

class Request(winxuan.baseInterface.BaseReq):
    #http://open.winxuan.com/#/app/docApi/detail/?apiId=50&cateId=3
    def __init__(self, outerTrade, sellType, purchaseTime, listPrice, deliveryType, stockOutOption, salePrice, #必选
                 items, #ShopTradeItem[]  数据集
                 tradeConsignee, #数据集
                 wayBill = None,  # 
                 maxDeliveryTime = None,  # 
                 dc = None,  # 
                 deliveryFee = None,  # int
                 invoiceType = None,  # 
                 tradeInvoice =  None # 数据集
                 ):
        
        """Constructor"""
        self.outerTrade = outerTrade
        self.sellType = sellType
        self.purchaseTime = purchaseTime
        self.listPrice = listPrice
        self.deliveryType = deliveryType
        self.stockOutOption = stockOutOption
        self.salePrice = salePrice
        self.items = items
        self.tradeConsignee = tradeConsignee
        if wayBill:
            self.wayBill = wayBill
        if maxDeliveryTime:
            self.maxDeliveryTime = maxDeliveryTime
        if dc:
            self.dc = dc
        if deliveryFee:
            self.deliveryFee = deliveryFee
        if invoiceType:
            self.invoiceType = invoiceType
        if tradeInvoice:
            self.tradeInvoice = tradeInvoice
