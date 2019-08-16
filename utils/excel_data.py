#!/user/bin/env python
#coding:utf-8

class ExcelVarible:
    CaseId =0
    Pre_CaseID=1
    title=2
    Request_Type=3
    url = 4
    Authorization=5 #数组
    Headers=6
    data = 7
    sql=8 #数组
    expect = 9
    result = 10

def getCaseID():
    return ExcelVarible.CaseId
def getTitle():
    return ExcelVarible.title
def getUrl():
    return ExcelVarible.url
def getData():
    return ExcelVarible.data
def getExcept():
    return ExcelVarible.expect
def getResult():
    return ExcelVarible.result
def getsql():
    return ExcelVarible.sql
def getPre_CaseID():
    return ExcelVarible.Pre_CaseID
def getRequest_Type():
    return ExcelVarible.Request_Type
def getAuthorization():
    return ExcelVarible.Authorization
def getHeaders():
    return ExcelVarible.Headers
def getHeadersValue():
    '''获取请求头'''
    headers={"Content-Type":"application/json"}
    return headers
