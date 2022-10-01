#!/usr/bin/python
# _*_ coding: utf-8 _*_
# @Time :2022/9/29 0:38
# Author : jingluo~
# @File : test_fixture_param.py
import pytest

@pytest.fixture(params=[["selenium",123],["appium",456]])
def login(request):
    print(f"用户名：{request.param}")
    return request.param

def test_demo1(login):
    print(f"demo1 case: 数据为：{login}")
