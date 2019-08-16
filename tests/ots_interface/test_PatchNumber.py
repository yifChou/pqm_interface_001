#!/user/bin/env python
#coding:utf-8


import unittest
from base.method import Method
from utils.assertion import isIn

'''转运换标-批次接口'''
class test_PatchNumber(unittest.TestCase):

    def setUp(self):

        self.obj=Method()

    def test_PatchNumber_001(self):
        '''批次预报：正常预报'''
        R=8
        r = self.obj.post_with_auth(row=R,account1="T0001",password1="asdfghjk")
        isIn(self,r=r,row=R)
        self.obj.db.update("delete from ots_inbound_order_info where batch_number='auto_test_number_001';")
    def test_PatchNumber_002(self):
        '''批次预报：同客户相同批次号'''
        R=9
        self.obj.post_with_auth(row=R, account1="T0001", password1="asdfghjk")
        r = self.obj.post_with_auth(row=R,account1="T0001",password1="asdfghjk")
        isIn(self,r=r,row=R)
    def test_PatchNumber_003(self):
        '''批次预报：不同客户相同批次号,可以预报成功'''
        R=10
        self.obj.post_with_auth(row=R, account1="T0001", password1="asdfghjk")
        r = self.obj.post_with_auth(row=R,account1="T0002",password1="123456")
        isIn(self, r=r, row=R)
        self.obj.db.update("delete from ots_inbound_order_info where batch_number='auto_test_number_001';")
if __name__ == '__main__':
    unittest.main(verbosity=2)