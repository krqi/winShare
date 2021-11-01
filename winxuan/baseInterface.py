# coding=utf-8

class BaseReq():
    def __init__(self):
        raise Exception('必须实现参数初始化接口')
    
    def getParams(self): #子类必须实现 def __init__(self):
        attr = self.__dict__.copy()
        
        #for key in list(attr.keys()):
                #if attr.get(key) == None or attr.get(key) == '':
                    #del attr[key]
        return attr
    
    def getApiPath(self):
        return self.__module__
    
class BaseRsp():
    def getRsp(self, data):
        if (not isinstance(data, dict)) and (not isinstance(data, list)):
            raise Exception('返回消息非dict 或者list')
        
        rst = []
        if isinstance(data, list):
            for r in data:
                rst.append(self.parseRsp(r))
        else:
            rst = self.parseRsp(data)
        return rst

    def parseRsp(self, data):
        dit = {}
        lit = []
        for k,v in data.items():
            if isinstance(v, dict):
                fdd = self.getDictFlatData(v)
                dit.update(fdd)
            elif isinstance(v, list):
                sd = ''
                for lo in v:
                    if isinstance(lo, dict):
                        fdd = self.getDictFlatData(lo)
                        lit.append(fdd)
                    else:
                        sd += str(v)+';'
                if sd != '':
                    dit[k] = sd
            else:
                dit[k] = v
        
        if len(dit) > 0:
            if len(lit) > 0:
                raise Exception('Rsp消息结构异常')
            else:
                return dit
        else:
            if len(lit) > 0:
                return lit
            else:
                return []
            
    def getDictFlatData(self, data):
        rst = {}
        for k,v in data.items():
            if isinstance(v, dict):
                vget = self.getDictFlatData(v)
                rst.update(vget)
            elif isinstance(v, list):
                i = 0
                for lo in v:
                    i += 1
                    dit = self.getDictFlatData(lo)
                    for k2,v2 in dit.items():
                        rst[k2+str(i)] = v2
            else:
                rst[k] = v
        
        return rst

