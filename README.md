# winShare

#### 介绍
该库为文选书店python访问自行写作的SDK，可对接获取文选相关数据，容易扩展。


#### 安装教程

git clone 该项目
然后创建执行文件执行感兴趣的数据即可。


#### 使用说明
所有的请求都3步，构造请求，执行，获取请求结果。

`# coding=utf-8
import winxuan

#请更换你的appKey、appSecret、accessToken，默认访问正式环境，沙箱环境请传入serverUrl指定
wxc = winxuan.WinShareClient(appKey = '100032', appSecret = '2d90eed6ed5cdf68838388483ed', accessToken = '2d90eed6ed5cdf63c235581db56807ed')    

#创建请求
req = winxuan.items.area.sales.top.Request('YEAR')
#执行请求
rst = wxc.exec(req)
#获取返回可视化结果
rsp = winxuan.baseInterface.BaseRsp().getRsp(rst)`

