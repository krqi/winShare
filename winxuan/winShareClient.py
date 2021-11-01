# coding=utf-8

'''公共hash、加解密'''
import hashlib
import time
import json
import httplib2
import requests
import urllib

class WinShareClient():

    def __init__(self,appKey, appSecret, accessToken, serverUrl = 'http://gw.api.winxuan.com/router/rest', timeout = 60):
        self.serverUrl = serverUrl
        self.appKey = appKey
        self.appSecret = appSecret
        self.accessToken = accessToken
        self.timeout = timeout
            
        self.baseHead = {'Accept':' */*',
            'Accept-Encoding':' gzip, deflate',
            'Accept-Language':' zh-CN,zh;q=0.9',
            'Connection':' keep-alive',
            'Content-Type':' application/x-www-form-urlencoded;charset=UTF-8',
            'User-Agent':' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}
        self.baseParam = {'accessToken':accessToken,
                 'appKey':appKey,
                 'v':'1.0',
                 'format':'json'}
    
    def md5(self, data):
        return hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
    
    def SHA1(self, data):
        return hashlib.sha1(data.encode(encoding='UTF-8')).hexdigest()
    
    def fillSign(self, reqParams):
        if reqParams == None or len(reqParams) == 0:
            return
        
        dd = sorted(reqParams.items(), key=lambda x:x[0])
        
        sb = self.appSecret
        for n,v in dd:
            sb += n
            sb += str(v)
        
        sb += self.appSecret
        
        reqParams['appSign'] = self.SHA1(sb).upper()

    def parseMutiToOneDict(self, tt):
        tx = {}
        for k,v in tt.items():
            if isinstance(v, list):
                i = 0
                for d in v:
                    if isinstance(d, dict):
                        for lk, lv in d.items():
                            nk = k + '[' + str(i) + '].' + lk
                            tx[nk] = lv
                    else:
                        tx[k+'['+str(i)+']'] = d
                    
                    i += 1
                
            elif isinstance(v, dict):
                for lk,lv in v.items():
                    tx[k+'.'+lk] = lv
            else:
                tx[k] = v
        return tx

    def exec(self, req):
        reqparam = req.getParams()
        reqparam['timeStamp'] = str(int(time.time() * 1000))
        reqparam['method'] = req.getApiPath()
        reqparam.update(self.baseParam)
        
        self.fillSign(reqparam)
        
        #body = json.dumps(reqparam, ensure_ascii=False)， 不是json编码是URL编码
        rparam = self.parseMutiToOneDict(reqparam)
        body = urllib.parse.urlencode(rparam)
        
        head = self.baseHead.copy()
        head['Content-Length'] = str(len(body))

        hobj = httplib2.Http(timeout = self.timeout)
        #rsp , cont = hobj.request(self.serverUrl, headers=head, method='GET')
        #head['Cookie'] = rsp['set-cookie']
        rsp, content = hobj.request(self.serverUrl, body=body, headers=head, method='POST')
        
        decontent = content.decode('UTF-8')
        js = json.loads(decontent)
        
        
        return js
        
