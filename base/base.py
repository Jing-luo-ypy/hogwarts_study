#!/usr/bin/python
# _*_ coding: utf-8 _*_
# @Time :2022/9/25 18:05
# Author : jingluo~
# @File : base.py
from func.calculator import Calculator
from utils.log_util import logger

class Base:
    def setup_class(self):
        logger.info("实例化 Caculator 对象")
        self.cal = Calculator()

    def teardown_class(self):
        print("结束测试")

    def setup(self):
        logger.info("开始计算")

    def  teardown(self):
        logger.info("结束计算")