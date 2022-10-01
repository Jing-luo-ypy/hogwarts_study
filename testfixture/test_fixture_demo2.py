#!/usr/bin/python
# _*_ coding: utf-8 _*_
# @Time :2022/9/28 23:24
# Author : jingluo~
# @File : test_fixture_demo2.py
import pytest
"""
# fixture 的作用域
# fixture 的方法 尽量避免以 test_ 开头
# yield 激活 teardown 操作
@pytest.fixture
def fixture_name():
    setup 操作
    yield 返回值
    teardown 操作
"""

# # 定义了登录的 fixture
# @pytest.fixture(scope="module")
# def login():
#     # setup 操作
#     print("完成登录操作")
#     token = "abcdefgsisfvvsd"
#     username = "hogwarts"
#     yield token,username # 相当于 return
#     # teardown 操作
#     print("完成登出操作")

def test_search(login):
    print("搜索")

# 因为传入了由 fixture 装饰的函数对象，因此执行该用例时，会先执行 login 函数
def test_cart(login):
    token,username = login
    print(f"token: {token}, name: {username}")
    print("购物车")

def test_order(login):
    print("下单功能")

class TestDemo:
    def test_case1(self,login):
        print("case1")

    def test_case2(self,login):
        print("case2")