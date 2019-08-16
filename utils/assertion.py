#coding=utf-8

import traceback
from utils.log import *
from base.method import IsContent

def assertHTTPCode(response, code_list=None):
    '''判断http协议码'''
    res_code = response.status_code
    if not code_list:
        code_list = [200]
    if res_code not in code_list:
        return logger.info('响应code不在列表中！')
        raise AssertionError('响应code不在列表中！')  # 抛出AssertionError，unittest会自动判别为用例Failure，不是Error

def isIn(self, r, row):
    '''判断是否包含返回的内容，并打印日志'''
    a = IsContent()
    assertHTTPCode(r, [200])
    self.assertTrue(a.isContent(row=row, str=r.text))

    '''
    try:
        assertHTTPCode(r, [200])
        self.assertTrue(a.isContent(row=row, str=r.text))
        return logger.info(r.text)
    except AssertionError as err:
        err_str = traceback.format_exc()
        logger.info(err_str)
        raise AssertionError('断言失败！')
    '''
    return logger.info(r.text)
def wcf_isIn(self, r, row):
    '''判断是否包含返回的内容，并打印日志'''
    a = IsContent()
    try:
        self.assertTrue(a.isContent(row=row, str=r))
        return logger.info(r)
    except AssertionError as err:
        err_str = traceback.format_exc()
        logger.info(err_str)
        raise AssertionError('断言失败！')
def isIn1(str1,response):
    '''判断http协议码'''
    str2 = response
    if str1 in str2:
        return logger.info(response)
    if str1 not in str2:
        return logger.info('断言失败！')
        raise AssertionError('断言失败！')  # 抛出AssertionError，unittest会自动判别为用例Failure，不是Error


