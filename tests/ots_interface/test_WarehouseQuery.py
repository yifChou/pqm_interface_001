#!/user/bin/env python
#coding:utf-8


import unittest
from base.method import Method
from utils.assertion import isIn


'''转运单查询'''
class test_WarehouseQuery(unittest.TestCase):

    def setUp(self):
        self.obj=Method()

    def test_WarehouseQuery_001(self):
        '''查询转运单信息：参数正确，查询美东仓成功'''
        r = self.obj.post(row=1)
        print(r.text)
        isIn(self,r=r,row=1)
    def test_WarehouseQuery_002(self):
        '''查询转运单信息：参数正确，查询ECDC仓成功'''
        r = self.obj.post(row=2)
        print(r.text)
        isIn(self,r=r,row=2)
    def test_WarehouseQuery_003(self):
        '''查询转运单信息：仓库代码为空，查询到所有仓成功'''
        r = self.obj.post(row=3)
        print(r.text)
        isIn(self,r=r,row=3)
    def test_WarehouseQuery_004(self):
        '''查询转运单信息：仓库代码不存在，查询到所有仓成功'''
        r = self.obj.post(row=4)
        print(r.text)
        isIn(self,r=r,row=4)


if __name__ == '__main__':
    unittest.main(verbosity=2)