#coding=utf-8
# import urllib3
import requests
import json
#
# def get(self, url, params):
#     params = urllib3.parse.urlencode(eval(params))  # 将参数转为url编码字符串
#     url = 'http://' + self.host + ':' + str(self.port) + url + params
#     request = urllib3.request.Request(url, headers=self.headers)
#
#     try:
#         response = urllib3.request.urlopen(request)
#         response = response.read().decode('utf-8')  ## decode函数对获取的字节数据进行解码
#         json_response = json.loads(response)  # 将返回数据转为json格式的数据
#         return json_response
#     except Exception as e:
#         print('%s' % e)
#         return {}
#
# def post(self, url, data):
#     data = json.dumps(eval(data))
#     data = data.encode('utf-8')
#     url = 'http://' + self.host + ':' + str(self.port) + url
#     try:
#         request = urllib3.request.Request(url, headers=self.headers)
#         response = urllib3.request.urlopen(request, data)
#         response = response.read().decode('utf-8')
#         json_response = json.loads(response)
#         return json_response
#     except Exception as e:
#         print('%s' % e)
#         return {}
class runMethond:
    def post_main(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.post(url=url,data=data,headers=header)
        else:
            res = requests.post(url=url,data=data)
        return res.json()

    def get_main(self,url,data=None,header=None):
        res = None
        if header != None:
            res = requests.post(url=url,data=data,headers=header,verify=False)
        else:
            res = requests.post(url=url,data=data,verify=False)
        return res.json()

    def run_main(self,method,url,data=None,header=None):
        res = None

        if method == 'post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)

        return json.dumps(res,ensure_ascii=False)