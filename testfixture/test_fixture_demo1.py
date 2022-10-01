#!/usr/bin/python
# _*_ coding: utf-8 _*_
# @Time :2022/9/28 23:12
# Author : jingluo~
# @File : test_fixture_demo1.py
import pytest

# # 定义了登录的 fixture
# @pytest.fixture()
# def login():
#     print("登录操作")

def test_search():
    print("搜索")

# 因为传入了由 fixture 装饰的函数对象，因此执行该用例时，会先执行 login 函数
def test_cart(login):
    print("购物车")

def test_order(login):
    print("下单功能")