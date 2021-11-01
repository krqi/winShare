# coding=utf-8
import winxuan

########################################################################
"""创建物流轨迹"""

class Request(winxuan.baseInterface.BaseReq):
    def __init__(self, waybillNo, eventCode, eventTitle, eventTime, eventContent, facilityType, facilityName, 
                 facilityCode = None, 
                 countryName = None, 
                 provinceName = None, 
                 cityName = None, 
                 districtName = None, 
                 townName = None, 
                 contacter = None, 
                 contactPhone = None, 
                 nextCity = None, 
                 nextNodeType = None, 
                 nextNodeCode = None, 
                 nextNodeName = None, 
                 description = None, 
                 address = None, 
                 remark = None):
        
        """Constructor"""
        self.waybillNo = waybillNo
        self.eventCode = eventCode
        self.eventTitle = eventTitle
        self.eventTime = eventTime
        self.eventContent = eventContent
        self.facilityType = facilityType
        self.facilityName = facilityName
        if facilityCode:
            self.facilityCode = facilityCode
        if countryName:
            self.countryName = countryName
        if provinceName:
            self.provinceName = provinceName
        if cityName:
            self.cityName = cityName
        if districtName:
            self.districtName = districtName
        if townName:
            self.townName = townName
        if contacter:
            self.contacter = contacter
        if contactPhone:
            self.contactPhone = contactPhone
        if nextCity:
            self.nextCity = nextCity
        if nextNodeType:
            self.nextNodeType = nextNodeType
        if nextNodeCode:
            self.nextNodeCode = nextNodeCode
        if nextNodeName:
            self.nextNodeName = nextNodeName
        if description:
            self.description = description
        if address:
            self.address = address
        if remark:
            self.remark = remark