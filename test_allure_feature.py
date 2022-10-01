#!/usr/bin/python
# _*_ coding: utf-8 _*_
# @Time :2022/9/27 17:43
# Author : jingluo~
# @File : test_allure_feature.py
import allure

@allure.feature("搜索模块")
class TestSearch():
    @allure.story("搜索成功")
    def test_case1(self):
        print("case1")

    @allure.story("搜索失败")
    def test_case2(self):
        print("case2")

class TestLogin():
    @allure.story("登录成功")
    def test_login_success(self):
        with allure.step("步骤1：打开应用"):
            print("打开应用")
        with allure.step("步骤2：登录页面"):
            print("登录页面")
            # allure.attach.file 放文件
            allure.attach.file("D:\\tools\\Pycharm\\PyCharm Community Edition 2020.1.1\\workspace\\hogwarts_study\\test\cases\img\\test01.png",
                               name = "截图",
            attachment_type = allure.attachment_type.PNG,
            extension=".png")
            # allure.attach 放文本
            allure.attach("这是一段文本信息",name="文本展示")
        with allure.step("步骤3：输入用户信息"):
            # assert 1 == 2
            print("输入用户名和密码")
        with allure.step("步骤4：进入成功页面"):
            allure.attach('<a href="/"><picture><img src="https://ceshiren.com/uploads/default/original/1X/809c63f904a37bc0c6f029bbaf4903c27f03ea8a.png" alt="测试人社区" id="site-logo" /></picture></a>',
                          name='html展示',
                          attachment_type=allure.attachment_type.HTML)
            print("这是登录：测试用例，登录成功")

    @allure.story("登录成功")
    def test_login_success_a(self):
        print("这是登录：测试用例，登录成功")

    @allure.story("登录成功")
    def test_login_success_b(self):
        print("用户名缺失")

    @allure.story("登录失败")
    def test_login_failure(self):
        print("输入用户名")
        print("输入密码")
        print("点击登录")
        assert '1' == 1
        print("登录失败")

    @allure.story("登录失败")
    def test_login_failure_a(self):
        print("这是登录：测试用例，登录失败")