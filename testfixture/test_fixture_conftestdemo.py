#!/usr/bin/python
# _*_ coding: utf-8 _*_
# @Time :2022/9/29 0:11
# Author : jingluo~
# @File : test_fixture_conftestdemo.py

def test_search():
    print("搜索")

def test_get_product(connectDB):
    print("验证 获取单品信息")

def test_cart():
    print("购物车")

def test_order():
    print("下单功能")

class TestDemo:
    def test_case1(self):
        print("case1")

    def test_case2(self):
        print("case2")