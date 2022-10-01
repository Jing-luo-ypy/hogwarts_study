#!/usr/bin/python
# _*_ coding: utf-8 _*_
# @Time :2022/9/30 16:42
# Author : jingluo~
# @File : test_order.py
import pytest

# @pytest.mark.run(order=2)
@pytest.mark.third
def test_foo():
    assert True

# @pytest.mark.run(order=1)
@pytest.mark.first
def test_bar():
    assert True

# @pytest.mark.run(order=1)
@pytest.mark.second
def test_bar1():
    assert True

