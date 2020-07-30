#!/user/bin/env python
#coding:utf-8

import requests
from utils.operationJson import OperationJson
from utils.operationExcel import OperationExcel,OperationExcel_two
from utils.operationMysql import database
from utils.excel_data import *
import hashlib
from suds.client import Client
import time,random
def now():
    return time.strftime("%Y-%m-%d %H:%M:%S")
def ymd():
    return time.strftime("%Y%m%d")
def time_str():
    return time.strftime("%Y%m%d%H%M%S")
def rand100_999():
    return str(random.randint(100, 999))

class Method:

    def __init__(self):
        self.operationJson =OperationJson()
        self.excel = OperationExcel()
        self.excel_pre = OperationExcel_two()
        self.db=database()
        self.header_test = {
            "Host": "10.168.95.149:8022",
            "Content-Type": "application/json;charset=UTF-8",
            "Content-Length": "228",
        }

    def request_wcf(self, url,data):
        # headers = {'Content-Type': 'application/soap+xml; charset="UTF-8"'}
        url_main,url,interface = url.split(",")
        #print(url_main,url,interface)
        client = Client(url_main)
        client.set_options(location = url)#(location = "http://10.168.95.32:5004/FmsAPIServicesForHttpDelegate")
        #print(data_type,type(interface),type(data))
        canshu, data_value = data.split("=", 1) # 把请求数据分成2分，用于判断是对象数据还是一般参数数据
        if data_value[0]!="{":
            "如果接口是正常参数，一个一个赋值"
            request_str = "client.service."+interface+"("+data+")"
            print("请求接口：",request_str)
            result = eval(request_str)
            return str(result)
        else:
            "如果接口参数是对象，则需先创建对象数据"
            data_dict = eval(data_value)
            print(data_dict)
            request_str = "client.service."+interface+"(" + canshu + "=data_dict)"
            print("请求接口：",request_str)
            result = eval(request_str)
            return str(result)
    def get_md5(self,data):
        m = hashlib.md5()
        m.update(data.encode("utf-8"))
        print(m.hexdigest()[8:-8], type(m.hexdigest()[8:-8]))
        return m.hexdigest()[8:-8].upper()

    def get_authorizaiton(self,header_test,account, password):
        author = account + "&" + self.get_md5(account + "&" + password)
        header_test["Authorization"] = "Basic {}".format(author)
        # print(header_test)
        return header_test

    def post(self,row):
        # url = Config().get(self.URL)
        url = self.excel.getUrl(row=row)
        try:
            r = requests.post(
                url=url,
                data=self.operationJson.getRequestsData(row=row),
                headers=getHeadersValue(),
                timeout=6)
            return r
        except Exception as e:
            raise RuntimeError('接口请求发生未知的错误')
    def post_new(self,url,data,header =getHeadersValue("json") ):
        # url = Config().get(self.URL)
        try:
            r = requests.post(
                url=url,
                data=data,
                headers=header,
                timeout=600)
            return r
        except Exception as e:
            raise RuntimeError('接口请求发生未知的错误')
    def post_with_auth(self,row,account1,password1):
        # url = Config().get(self.URL)
        header_test = {
            "Host": "10.168.95.149:8022",
            "Content-Type": "application/json;charset=UTF-8",
            "Content-Length": "228",
        }
        def get_md5(data):
            m = hashlib.md5()
            m.update(data.encode("utf-8"))
            print(m.hexdigest()[8:-8], type(m.hexdigest()[8:-8]))
            return m.hexdigest()[8:-8].upper()

        def get_authorizaiton(account, password):
            author = account + "&" + get_md5(account + "&" + password)
            header_test["Authorization"] = "Basic {}".format(author)
            #print(header_test)
            return header_test
        url = self.excel.getUrl(row=row)
        try:
            r = requests.post(
                url=url,
                data=self.operationJson.getRequestsData(row=row),
                headers=get_authorizaiton(account1,password1),
                timeout=6,
                )
            return r
        except Exception as e:
            raise RuntimeError('接口请求发生未知的错误')

    def get(self,row):
        url = self.excel.getUrl(row=row)
        try:
            r = requests.get(url=url,
                             timeout=6)
            return r
        except Exception as e:
            raise RuntimeError('接口请求发生未知的错误')
    def get_new(self,row,header):
        url = self.excel.getUrl(row=row)
        try:
            r = requests.get(url=url,headers=header,
                             timeout=6)
            return r
        except Exception as e:
            raise RuntimeError('接口请求发生未知的错误')

    # def post(self,row,data):
    #         try:
    #             r = requests.post(
    #                 url=self.excel.getUrl(row=row),
    #                 data=data,
    #                 headers=getHeadersValue(),
    #                 timeout=6)
    #             return r
    #         except Exception as e:
    #             raise RuntimeError('接口请求发生未知的错误')


class IsContent:
    def __init__(self):
        self.excel = OperationExcel()
    def isContent(self,row,str):
        flag=None
        #print(self.excel.getExcept(row=row))
        if self.excel.getExcept(row=row) in str:
            flag=True
        else:
            flag=False
        print(flag)
        return flag

