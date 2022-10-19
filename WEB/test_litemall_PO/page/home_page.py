#!/usr/bin/python
# _*_ coding: utf-8 _*_
# @Time :2022/10/19 17:20
# Author : jingluo~
# @File : home_page.py
"""首页"""
from selenium.webdriver.common.by import By

from WEB.test_litemall_PO.page.base_page import BasePage
from WEB.test_litemall_PO.utils.log_utils import logger


class HomePage(BasePage):

    __MENU_MALL_MANAGE = (By.XPATH, "//*[text()='商场管理']")
    __MENU_PRODUCT_CATEGORY = (By.XPATH, "//*[text()='商品类目']")
    """系统首页：进入商品类目"""
    def go_to_category(self):
        logger.info("进入商品类目")
        # 点击菜单“商场管理”
        self.do_find(self.__MENU_MALL_MANAGE).click()
        # 点击菜单“商品类目”
        self.do_find(self.__MENU_PRODUCT_CATEGORY).click()

        # ==》 类目列表页面
        from WEB.test_litemall_PO.page.category_list_page import CategoryListPage
        return CategoryListPage(self.driver)