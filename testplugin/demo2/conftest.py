#!/usr/bin/python
# _*_ coding: utf-8 _*_
# @Time :2022/9/30 17:39
# Author : jingluo~
# @File : conftest.py
from typing import Optional, List
import yaml
import pytest

# 定义命令行参数
def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")     #group 将下面所有的 option都展示在这个group下。
    mygroup.addoption("--env",    #注册一个命令行选项
        default='test',      # 参数的默认值
        dest='env',            #  存储的变量，为属性命令，可以使用Option对象访问到这个值，暂用不到
        help='set your run env'    # 帮助提示 参数的描述信息
        )

    mygroup = parser.getgroup("hogwarts")     #group 将下面所有的 option都展示在这个group下。
    mygroup.addoption("--env1",    #注册一个命令行选项
        default='test',      # 参数的默认值
        dest='env1',            #  存储的变量，为属性命令，可以使用Option对象访问到这个值，暂用不到
        help='set your run env1'    # 帮助提示 参数的描述信息
        )
# # 如何针对传入的不同参数完成不同的逻辑处理
# @pytest.fixture(scope='session')
# def cmdoption(request):  # 函数名可以自定义，但是必须有 参数 request
#     return request.config.getoption("--env")

@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env",default="test")
    if myenv == 'test':
        datapath = "datas/test/data.yaml"
    elif myenv == 'dev':
        datapath = "datas/dev/data.yaml"

    with open(datapath) as f:
        datas = yaml.safe_load(f)
    return myenv,datas

# def pytest_runtest_setup(item:"Item") -> None:
#     print("hook: setup")
#
# def pytest_runtest_teardown(item: "Item", nextitem: Optional["Item"]) -> None:
#     print("hook: teardown")
#
# # 收集完测试用例之后 被调用的 hook 函数
# def pytest_collection_modifyitems(
#     session: "Session", config: "Config", items: List["Item"]
# ) -> None:
#     print(items)
#     # name 用例的名字
#     # nameid 测试用例路径
#     for item in items:
#         item.name = item.name.encode('utf-8').decode('unicode-escape')
#         item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
#     # 修改用例执行顺序（倒置）
#     items.reverse()