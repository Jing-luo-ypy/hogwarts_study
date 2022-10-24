#!/usr/bin/python
# _*_ coding: utf-8 _*_
# @Time :2022/10/21 16:29
# Author : jingluo~
# @File : test_addressbook.py
import time
import yaml
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def click_exception(by, element, max_attempts=5):
    def _inner(driver):
        actul_attempts = 0
        while actul_attempts < max_attempts:
            actul_attempts += 1
            try:
                # 如果点击过程报错，则直接执行 except 逻辑，并继续循环
                # 没有报错，则直接 return ，循环结束
                driver.find_element(by, element).click()
                return True
            except Exception:
                print("在点击动作时报错")
        raise Exception("超出了最大点击次数")

    return _inner


class TestAddressBook:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.fake = Faker("zh_CN")

    def teardown_class(self):
        self.driver.quit()

    def test_get_cookies(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        time.sleep(15)
        cookies = self.driver.get_cookies()
        with open("../data/cookies.yaml","w",encoding="utf-8") as f:
            yaml.safe_dump(cookies,f)

    def login_cookies(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        cookies = yaml.safe_load(open("../data/cookies.yaml",encoding="utf-8"))
        for ck in cookies:
            self.driver.add_cookie(ck)
        self.driver.refresh()

    """添加通讯录成员"""
    def test_add_member(self):
        username = self.fake.name()
        acctid = self.fake.ssn()
        mainNumber = self.fake.phone_number()
        self.login_cookies()
        # 点击菜单“通讯录”
        self.driver.find_elements(By.CSS_SELECTOR,".frame_nav_item_title")[1].click()
        print(f"添加通讯录成员：{username}")
        # 点击 “添加成员” 按钮
        # self.driver.find_element(By.CSS_SELECTOR,".js_has_member .js_add_member").click()
        # 显式等待，等输入框存在，再执行后续操作
        addmember_loc = (By.CSS_SELECTOR,".js_has_member .js_add_member")
        # 成功地点击添加成员 ---> 能够跳转到输入页面就算成功了
        # 隐式等待： 去判断 dom 里是否存在这个元素
        # 显示曾带：真正地判断这些属性没有问题
        def wait_for(x:webdriver):
            try:
                # 显示等待会反复地执行这个方法
                # 1. 点击【添加成员】
                x.find_element(*addmember_loc).click()
                # 2. 判断是否进入到下一个页面，有输入框
                return x.find_element(By.ID,"username")
            except:
                return False
        WebDriverWait(self.driver,5).until(wait_for)
        # 姓名
        self.driver.find_element(By.ID,"username").send_keys(username)
        # 账号
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(acctid)
        # 手机号
        self.driver.find_element(By.CSS_SELECTOR, ".ww_telInput_mainNumber").send_keys(mainNumber)
        # 保存
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        # 获取冒泡信息
        ele = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//*[@class='ww_tip success']")
            ))
        res = ele.text
        assert "保存成功" == res

    """添加部门"""
    def test_create_party(self):
        party = "测试组01"
        self.login_cookies()
        # 点击菜单 “通讯录”
        self.driver.find_elements(By.CSS_SELECTOR, ".frame_nav_item_title")[1].click()
        # 点击 “添加部门” 按钮
        print(f"新建部门：{party}")
        # 点击 添加按钮（+）
        self.driver.find_element(By.CSS_SELECTOR,".member_colLeft_top_addBtn").click()
        # 点击 “添加部门”
        self.driver.find_element(By.CSS_SELECTOR,".js_create_party").click()
        # 输入部门名称
        self.driver.find_element(By.NAME,"name").send_keys(party)
        # 点击 “所属部门”选项框，使显示下拉框
        self.driver.find_element(By.CSS_SELECTOR,".js_toggle_party_list").click()
        # 点击 选中的所属部门
        self.driver.find_element(By.XPATH,"//div[@class='inputDlg_item']//a[text()='测试学习使用']").click()
        # 点击 “确定”按钮，保存
        self.driver.find_element(By.XPATH,"//*[@d_ck='submit']").click()

        ele = WebDriverWait(self.driver,10).until(
            expected_conditions.visibility_of_element_located(
                (By.ID,"js_tips")
            )
        )
        res = ele.text

        assert "新建部门成功" == res

