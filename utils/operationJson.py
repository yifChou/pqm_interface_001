#!/user/bin/env python
#coding:utf-8

import json
from utils.config import *
from utils.operationExcel import OperationExcel

class OperationJson:
    '''获取json文件中的数据'''
    def __init__(self):
        self.excel = OperationExcel()

    def getReadJson(self):
        #with open((DATA_PATH+'\\requestData.json'),encoding='utf-8') as fp:
        with open((DATA_PATH + '\\ots_requestData.json'), encoding='utf-8') as fp:
            data = json.load(fp)
            return data

    def getRequestsData(self,row):
         #return self.getReadJson()[self.excel.get_request_data(row=row)]
        return json.dumps(self.getReadJson()[self.excel.get_request_data(row=row)])
