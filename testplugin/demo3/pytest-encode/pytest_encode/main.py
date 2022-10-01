#!/usr/bin/python
# _*_ coding: utf-8 _*_
# @Time :2022/10/1 23:25
# Author : jingluo~
# @File : main.py
from typing import List

def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(items)
    # name 用例的名字
    # nameid 测试用例路径
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')