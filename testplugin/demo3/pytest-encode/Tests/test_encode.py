#!/usr/bin/python
# _*_ coding: utf-8 _*_
# @Time :2022/10/1 23:27
# Author : jingluo~
# @File : test_encode.py
import pytest

@pytest.mark.parametrize('name',["哈利波特","赫敏"])
def test_mm(name):
    print(f"name: {name}")