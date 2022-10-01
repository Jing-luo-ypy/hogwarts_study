#!/usr/bin/python
# _*_ coding: utf-8 _*_
# @Time :2022/9/27 17:20
# Author : jingluo~
# @File : test_allure_title.py
import allure


class TestSearch():
    @allure.title("搜索词为Android")
    def test_case1(self):
        print("case1")

    @allure.title("搜索词为ios")
    def test_case2(self):
        print("case2")