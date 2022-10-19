#!/usr/bin/python
# _*_ coding: utf-8 _*_
# @Time :2022/10/19 17:21
# Author : jingluo~
# @File : category_create_page.py
"""新增类目页面"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from WEB.test_litemall_PO.page.base_page import BasePage
from WEB.test_litemall_PO.utils.log_utils import logger
from WEB.test_litemall_PO.utils.web_util import click_exception


class CategoryCreatePage(BasePage):

    __INPUT_CATEGORY_NAME = (By.CSS_SELECTOR, ".el-input__inner")
    __BTN_CONFIRM = (By.CSS_SELECTOR, ".el-dialog__footer .el-button--primary")
    """创建类目页面：创建类目"""
    def create_category(self,category_name):
        logger.info(f"新增类目为：{category_name}")
        # 输入类目名称
        self.do_send_keys(category_name,self.__INPUT_CATEGORY_NAME)
        # 点击“确定”按钮
        WebDriverWait(self.driver, 10).until(click_exception(*self.__BTN_CONFIRM))

        # ==> 类目列表页面
        from WEB.test_litemall_PO.page.category_list_page import CategoryListPage
        return CategoryListPage(self.driver)
