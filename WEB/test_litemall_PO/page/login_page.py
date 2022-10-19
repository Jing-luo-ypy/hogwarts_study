#!/usr/bin/python
# _*_ coding: utf-8 _*_
# @Time :2022/10/19 17:20
# Author : jingluo~
# @File : login_page.py
"""登录页面"""
from selenium.webdriver.common.by import By
from WEB.test_litemall_PO.page.base_page import BasePage
from WEB.test_litemall_PO.utils.log_utils import logger


class LoginPage(BasePage):
    _BASE_URL = "http://litemall.hogwarts.ceshiren.com/#/login"

    __INPUT_USERNAME = (By.NAME, "username")
    __INPUT_PASSWORD = (By.NAME, "password")
    __BTN_LOGIN = (By.CSS_SELECTOR, ".el-button.el-button--primary.el-button--mini")
    """登录页面：用户登录"""
    def login(self):
        # 访问登录页面
        logger.info("访问登录页面")
        # 输入“用户名”
        self.do_send_keys("manage", self.__INPUT_USERNAME)
        # 输入“密码”
        self.do_send_keys("manage123", self.__INPUT_PASSWORD)
        # 点击“登录”按钮
        self.do_find(self.__BTN_LOGIN).click()

        # ==》首页
        from WEB.test_litemall_PO.page.home_page import HomePage
        return HomePage(self.driver)