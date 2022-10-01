#!/usr/bin/python
# _*_ coding: utf-8 _*_
# @Time :2022/9/27 18:21
# Author : jingluo~
# @File : test_allure_links.py
import allure

TEST_CASE_LINK = "https://coding.imooc.com/class/592.html?utm_source=baidu&utm_medium=sem&utm_campaign=shizhan&utm_content=592&utm_term=Allure&bd_vid=8577187417264268849"

@allure.link("https://ceshiren.com")
def test_with_link():
    pass

@allure.link("https://www.baidu.com",name="百度")
def test_with_named_link():
    pass

@allure.issue("140","bug地址")   # 这里的"140" 是BUGID，不是链接，可以在运行时补充完整链接
def test_with_issue_link():
    pass

@allure.testcase(TEST_CASE_LINK,'测试用例管理平台地址')
def test_with_testcase_link():
    pass

