#!/user/bin/env python
#coding:utf-8


import unittest
from base.method import Method
from utils.assertion import isIn


'''袋子签入'''
class test_SignInBags(unittest.TestCase):

    def setUp(self):

        self.obj=Method()

    def test_SignInBags_001(self):
        '''袋子签入：正常签入'''
        r = self.obj.post(row=5)
        isIn(self,r=r,row=5)
        self.obj.db.update('update transfer_bag_mapping set check_in="N",check_in_time= NULL,check_in_by =null WHERE bag_id in(select bag_id from bag_infos where rf_id="313930353034303030303337");')
    def test_SignInBags_002(self):
        '''袋子签入：袋号已签入'''
        r = self.obj.post(row=6)
        isIn(self,r=r,row=6)
    def test_SignInBags_003(self):
        '''袋子签入：仓库代码不传'''
        r = self.obj.post(row=7)
        isIn(self, r=r, row=7)
    def test_SignInBags_004(self):
        '''袋子签入：袋号不存在'''
        R = 11
        r = self.obj.post(row=R)
        isIn(self, r=r, row=R)
if __name__ == '__main__':
    unittest.main(verbosity=2)