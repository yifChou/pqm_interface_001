#!/user/bin/env python
#coding:utf-8


import xlrd
from utils.config import *
from utils.excel_data import *
import time,random
from utils.log import *
def now():
    return time.strftime("%Y-%m-%d %H:%M:%S")
def ymd():
    return time.strftime("%Y%m%d")
def rand100_999():
    return str(random.randint(100, 999))

class OperationExcel:
    '''获取excel文件中的内容'''
    def getExcel(self):
        db = xlrd.open_workbook(EXCEL_PATH)
        sheet = db.sheet_by_index(2)
        return sheet

    def get_rows(self):
        '''获取excel的行数'''
        return self.getExcel().nrows

    def get_row_cel(self,row,col):
        '''获取单元格的内容'''
        return self.getExcel().cell_value(row,col)

    def getCaseID(self,row):
        '''获取CaseID'''
        return self.get_row_cel(row, getCaseID())

    def getTitle(self,row):
        '''获取title'''
        return self.get_row_cel(row, getTitle())

    def getUrl(self,row):
        '''获取url'''
        return self.get_row_cel(row,getUrl())

    def get_request_data(self,row):
        '''获取请求参数'''
        return self.get_row_cel(row,getData())

    def getExcept(self,row):
        '''获取期望结果'''
        return self.get_row_cel(row,getExcept())

    def getResult(self,row):
        '''获取实际结果'''
        return self.get_row_cel(row,getResult())

    def getPre_CaseID(self, row):
        '''获取准备参数'''
        return self.get_row_cel(row, getPre_CaseID())
    def getRequest_Type(self, row):
        '''获取请求类型'''
        return self.get_row_cel(row, getRequest_Type())
    def getAuthorization(self, row):
        '''获取用户验证账号密码'''
        return self.get_row_cel(row, getAuthorization())
    def getHeaders(self, row):
        '''获取请求头信息'''
        return self.get_row_cel(row, getHeaders())
    def getsql(self, row):
        '''获取要执行的sql语句'''
        return self.get_row_cel(row, getsql())
    def getWaitTime(self, row):
        '''获取要执行的sql语句前等待时间'''
        return self.get_row_cel(row, getWaitTime())
    def getDefaultHeaders(self):
        '''获取请求头'''
        return getHeadersValue("json")
    def getSheetName(self):
        '''获取sheet名称'''
        return self.getExcel().name
    def getSheetIndex(self):
        '''获取sheet的index'''
        return self.getExcel().number
class OperationExcel_two:
    '''获取excel文件中的内容'''
    def getExcel(self):
        db = xlrd.open_workbook(DATA_PATH+'\data.xls')
        sheet = db.sheet_by_index(3)
        return sheet
    def getSheetName(self):
        '''获取sheet名称'''
        return self.getExcel().name
    def getSheetIndex(self):
        '''获取sheet位置'''
        return self.getExcel().number
    def get_rows(self):
        '''获取excel的行数'''
        return self.getExcel().nrows

    def get_row_cel(self,row,col):
        '''获取单元格的内容'''
        return self.getExcel().cell_value(row,col)

    def getCaseID(self,row):
        '''获取CaseID'''
        return self.get_row_cel(row, getCaseID())

    def getTitle(self,row):
        '''获取title'''
        return self.get_row_cel(row, getTitle())

    def getUrl(self,row):
        '''获取url'''
        return self.get_row_cel(row,getUrl())

    def get_request_data(self,row):
        '''获取请求参数'''
        return self.get_row_cel(row,getData())

    def getExcept(self,row):
        '''获取期望结果'''
        return self.get_row_cel(row,getExcept())

    def getResult(self,row):
        '''获取实际结果'''
        return self.get_row_cel(row,getResult())

    def getPre_CaseID(self, row):
        '''获取准备参数'''
        return self.get_row_cel(row, getPre_CaseID())
    def getRequest_Type(self, row):
        '''获取请求类型'''
        return self.get_row_cel(row, getRequest_Type())
    def getAuthorization(self, row):
        '''获取用户验证账号密码'''
        return self.get_row_cel(row, getAuthorization())
    def getHeaders(self, row):
        '''获取请求头信息'''
        return self.get_row_cel(row, getHeaders())
    def getsql(self, row):
        '''获取要执行的sql语句'''
        return self.get_row_cel(row, getsql())
    def getDefaultHeaders(self):
        return getHeadersValue("json")
def check_json(a):
    if a!="":
        print(a)
        zhong1 = 0 #中括号[数量
        zhong2 = 0 #中括号]数量
        da1 = 0 #大括号{数量
        da2 = 0 #大括号}数量
        syh = 0 #单引号数量
        dyh = 0 #双引号数量
        for i in a:
            if i == "[":
                zhong1 += 1
            elif i == "]":
                zhong2 += 1
            elif i == "{":
                da1 += 1
            elif i == "}":
                da2 += 1
            elif i == '"':
                syh += 1
            elif i == "'":
                dyh += 1
        flag = 1
        error_list = []
        if zhong1 != zhong2:
            print("缺少中括号")
            error_list.append("缺少中括号")
            flag = 0
        if da1 != da2:
            print("缺少大括号")
            error_list.append("缺少大括号")
            flag = 0
        if syh%2!=0:
            print("缺少双引号")
            error_list.append("缺少双引号")
            flag = 0
        if dyh%2!=0:
            print("缺少单引号")
            error_list.append("缺少单引号")
            flag = 0
        if flag == 0:
            print("填写有误")
            return error_list
        else:
            print("数据格式正常")
            return 1

def check_sheet_data(sheet,row):
    request_data = sheet.get_request_data(row=row).replace("null", '""')
    result_data = check_json(request_data)
    logger.info("第"+str(row + 1)+"行")
    if result_data != 1:
        '''请求参数有误，记录日志'''
        logger_check_excel.info(str(result_data))
    if sheet.getCaseID(row=row)=="":
        logger_check_excel.info("caseid不能为空")
    if sheet.getTitle(row=row) == "":
        logger_check_excel.info("用例描述不能为空")
    if sheet.getRequest_Type(row=row) == "":
        logger_check_excel.info("请求方式不能为空")
    if sheet.getUrl(row=row) == "":
        logger_check_excel.info("请求地址不能为空")
    else:
        if sheet.getUrl(row=row).lower() == "post":
            if sheet.get_request_data(row=row)== "":
                logger_check_excel.info("请求方式为post，请求参数不能为空")
    if sheet.getExcept(row=row) == "":
        logger_check_excel.info("期望不能为空")
if __name__=="__main__":
    import json
    test = OperationExcel()
    print(test.getSheetName(),test.getSheetIndex())
    #a = test.get_request_data(27)
    check_sheet_data(test,34)






