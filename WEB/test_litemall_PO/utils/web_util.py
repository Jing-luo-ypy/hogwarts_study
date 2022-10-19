#!/usr/bin/python
# _*_ coding: utf-8 _*_
# @Time :2022/10/19 22:26
# Author : jingluo~
# @File : web_util.py
from WEB.test_litemall_PO.utils.log_utils import logger


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
                logger.debug("在点击动作时报错")
        raise Exception("超出了最大点击次数")

    return _inner