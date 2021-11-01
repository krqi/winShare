# coding=utf-8
import winxuan
import time

########################################################################
"""查询店铺商品信息变动列表"""

class Request(winxuan.baseInterface.BaseReq):
    
    #名称	类型	示例值	更多限制	描述
    #changeStartTime	Date	2018/1/1 0:00		变更开始时间,时间格式为:yyyy-MM-dd HH:mm:00; 
    #最小时间粒度间隔为10分钟,若传入"2018-01-01 12:31:21"平台将以"2018-01-01 12:30:00"为准
    #pageSize	Number	50	200	分页数量,默认为50,最大不能超过200
    #changeEndTime	Date	2018/1/1 1:00		变更结束时间,默认当前时间,开始结束时间间隔不能超过1天,时间格式为:yyyy-MM-dd HH:mm:00; 
    #最小时间粒度间隔为10分钟,若传入"2018-01-01 12:45:21"平台将以"2018-01-01 12:40:00"为准
    #pageNo	Number	1		分页页码,默认为1
    #changeTypes	String	TITLE_UPDATE,BASEINFO_UPDATE	变动类型最多传11种,最大长度160	
    #变动类型种类: 
    #1.TITLE_UPDATE: 标题更新; 
    #2.BASEINFO_UPDATE: 基础信息更新; 
    #3.DESCRIPTION_UPDATE: 描述更新; 
    #4.IMAGE_UPDATE: 图片更新; 
    #5.CLASSIFY_UPDATE: 分类更新; 
    #6.FREIGHT_UPDATE: 运费更新; 
    #7.PRESELL_UPDATE: 预售更新; 
    #8.SELLINGPOINTS_UPDATE: 卖点更新; 
    #9.ON_SHELF; 商品上架; 
    #10.UNDER_SHELF; 商品下架; 
    #11.NEW_UPLOAD; 新品上传;
    
    def __init__(self, changeTypes, changeStartTime, changeEndTime = None, pageSize = None, pageNo = None):
        
        """Constructor"""
        self.changeTypes = changeTypes
        self.changeStartTime = changeStartTime
        if changeEndTime:
            self.changeEndTime = changeEndTime
        if pageSize:
            self.pageSize = pageSize
        if pageNo:
            self.pageNo = pageNo
