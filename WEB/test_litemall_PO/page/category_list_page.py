#!/usr/bin/python
# _*_ coding: utf-8 _*_
# @Time :2022/10/19 17:20
# Author : jingluo~
# @File : category_list_page.py
"""类目列表页面"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from WEB.test_litemall_PO.page.base_page import BasePage
from WEB.test_litemall_PO.utils.log_utils import logger


class CategoryListPage(BasePage):

    __BTN_ADD = (By.XPATH, "//*[text()='添加']")
    __MSG_ADD_OPERATE = (By.XPATH,"//p[contains(text(),'创建成功')]")
    __MSG_DELETE_OPERATE = (By.XPATH,"//p[contains(text(),'删除成功')]")

    """类目列表页面：点击添加"""
    def click_add(self):
        logger.info("类目列表页面：点击添加")
        # 点击“添加按钮”
        self.do_find(self.__BTN_ADD).click()

        # ==> 创建类目页面
        from WEB.test_litemall_PO.page.category_create_page import CategoryCreatePage
        return CategoryCreatePage(self.driver)

    """类目列表页面：获取操作结果"""
    def get_add_type_result(self):
        # 获取冒泡消息文本
        element = self.wait_element_util_visible(self.__MSG_ADD_OPERATE)
        msg = element.text
        logger.info(f"冒泡消息为：{msg}")
        # ==》返回消息文本
        return msg

    def delete_category(self,category_name):
        # 对指定类目进行删除
        logger.info(f"删除类目：{category_name}")
        self.do_find(By.XPATH, f"//*[text()='{category_name}']/../..//*[text()='删除']").click()

        # ==》跳转到当前页面
        return CategoryListPage(self.driver)

    def get_delete_type_result(self):
        # 获取冒泡消息文本
        element = self.wait_element_util_visible(self.__MSG_DELETE_OPERATE)
        msg = element.text
        logger.info(f"冒泡消息为：{msg}")
        # ==》返回消息文本
        return msg