#!/user/bin/env python
#coding:utf-8


import unittest
from base.method import Method
from utils.assertion import isIn
from ddt import ddt,data,unpack
from tests.pqm_interface.example_test import test_All
import time
'''转运换标-箱子接口'''
@ddt
class test_AllInOne(unittest.TestCase):
    def setUp(self):
        self.obj=Method()
        self.start = time.time()
    argsall = []
    # for i in range(0, 64):
    for i in range(1,10):
       argsall.append(i)
    @data(*argsall)
    def test_AllInOne_001(self,args):
        test_All(self,args)
    def tearDown(self):
        run_time = time.time()-self.start
        print("执行时间：%.4f"% run_time,"响应时间结束")
if __name__ == '__main__':
    unittest.main(verbosity=2)
