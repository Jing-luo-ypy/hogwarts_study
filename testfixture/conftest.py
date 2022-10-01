#!/usr/bin/python
# _*_ coding: utf-8 _*_
# @Time :2022/9/29 0:08
# Author : jingluo~
# @File : conftest.py
# 文件名 conftest.py 是固定的，不能改变
import pytest

# @pytest.fixture(scope="function",autouse=True)
# def login():
#     # setup 操作
#     print("完成登录操作")
#     token = "abcdefgsisfvvsd"
#     username = "hogwarts"
#     yield token,username # 相当于 return
#     # teardown 操作
#     print("完成登出操作")

@pytest.fixture()
def connectDB():
    print("连接数据库")
    yield
    print("断开数据库")