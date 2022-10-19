#!/usr/bin/python
# _*_ coding: utf-8 _*_
# @Time :2022/10/19 17:35
# Author : jingluo~
# @File : test_categorygenery.py
import time

import pytest

from WEB.test_litemall_PO.page.login_page import LoginPage


class TestCategoryGenery:
    def setup_class(self):
        self.home = LoginPage().login()

    def teardown_class(self):
        # 退出浏览器
        time.sleep(3)
        self.home.do_quit()
    @pytest.mark.parametrize("category_name",["a","b","c"])
    def test_add_type(self,category_name):
        """系统首页：进入商品类目"""
        """类目列表页面：点击添加"""
        """创建类目页面：创建类目"""
        """类目列表页面：获取操作结果"""
        # category_name = "新增商品测试001"
        list_page = self.home\
             .go_to_category()\
             .click_add()\
             .create_category(category_name)
        res = list_page.get_add_type_result()
        # 数据清理
        list_page.delete_category(category_name)
        # 断言
        assert "创建成功" == res

    # 删除功能
    @pytest.mark.parametrize("category_name",["delA","delB","delC"])
    def test_del_type(self,category_name):
        """
        用户登录
        进入商品类目菜单
        点击添加
        创建商品类目
        点击删除
        获取删除操作结果
        断言测试结果
        :return:
        """
        # category_name = "删除类目测试"
        res = self.home \
            .go_to_category() \
            .click_add() \
            .create_category(category_name)\
            .delete_category(category_name)\
            .get_delete_type_result()
        assert "删除成功" == res