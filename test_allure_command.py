#!/usr/bin/python
# _*_ coding: utf-8 _*_
# @Time :2022/9/26 0:28
# Author : jingluo~
# @File : test_allure_command.py
import pytest

def test_success():
    """this test succeeds"""
    assert True

def test_failure():
    """this test fails"""
    assert False

def test_skip():
    "this test is skipped"
    pytest.skip("for a reason")

def test_broken():
    raise Exception("oops")