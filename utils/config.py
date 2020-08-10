#!/user/bin/env python
#coding:utf-8

# def data_dir(data='data',fileName=None):
#     '''查找文件的路径'''
#     return os.path.join(os.path.dirname(os.path.dirname(__file__)),data,fileName)


"""
读取配置文件。
"""
import os
from utils.fileReader import YamlReader
import xlrd
from xlutils.copy import copy


# 配置绝对路径。
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.yml')
DATA_PATH = os.path.join(BASE_PATH, 'data')
#DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')
REPORT_JENKINS_PATH = os.path.join(BASE_PATH, 'jenkins_report')
TESTS_PATH = os.path.join(BASE_PATH,'tests')
TESTCAST_PATH = os.path.join(BASE_PATH,"tests")
EXCEL_PATH = os.path.join(DATA_PATH,"data.xls")

class Config:
    def __init__(self, config=CONFIG_FILE):
        self.config = YamlReader(config).data

    def get(self, element, index=0):

        return self.config[index].get(element)

    def get_case(self,filename, sheetnum):
        case_dir = DATA_PATH + filename + '.xls'
        datas = xlrd.open_workbook(case_dir)
        table = datas.sheets()[sheetnum]
        nor = table.nrows
        nol = table.ncols

        return nor, table

    def write_file(self,filename,sheetnum):

        case_dir = DATA_PATH + filename + '.xls'
        datas = xlrd.open_workbook(case_dir)
        #rb = open_workbook('m:\\1.xls')

        # 通过sheet_by_index()获取的sheet没有write()方法
        rs = datas.sheet_by_index(sheetnum)

        wb = copy(rs)

        # 通过get_sheet()获取的sheet有write()方法
        ws = wb.get_sheet(sheetnum)
if __name__=="__main__":
    print(os.path.split(os.path.dirname(os.path.abspath(__file__))))