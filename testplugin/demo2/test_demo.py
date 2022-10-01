#!/usr/bin/python
# _*_ coding: utf-8 _*_
# @Time :2022/9/30 23:29
# Author : jingluo~
# @File : test_demo.py
import pytest

# 1、测试用例的名字
# 2、测试用例的路径

@pytest.mark.parametrize('name',["哈利波特","赫敏"])
def test_mm(name):
    print(f"name: {name}")