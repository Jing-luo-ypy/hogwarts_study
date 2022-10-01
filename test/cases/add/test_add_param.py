#!/usr/bin/python
# _*_ coding: utf-8 _*_
# @Time :2022/9/25 17:12
# Author : jingluo~
# @File : test_add_param.py
import pytest
import yaml
from base.base import Base

@allure.feature("相加功能")
class TestAdd(Base):

    @allure.story("相加 P0 级别用例")
    @pytest.mark.P0
    @pytest.mark.parametrize("x,y,expect",yaml.safe_load(open("../../../data/calculador_data.yaml",encoding='utf-8'))['add']['positive'])
    def test_add1(self,x,y,expect):
        with allure.step("step1：相加操作")
            result = self.cal.add(x,y)
        allure.attach.file("test/cases/img/test01.png", name="计算完成截图")
        with allure.step("step2：断言"):
            assert result == expect

    @allure.story("相加 P1 级别用例")
    @pytest.mark.P1
    @pytest.mark.parametrize("x,y,expect",yaml.safe_load(open("../../../data/calculador_data.yaml",encoding='utf-8'))['add']['ef_border'])
    def test_add2(self,x,y,expect):
        assert self.cal.add(x,y) == expect

    @allure.story("相加 P2 级别用例")
    @pytest.mark.P2
    @pytest.mark.parametrize("x,y",
                             yaml.safe_load(open("../../../data/calculador_data.yaml", encoding='utf-8'))['add'][
                                 'invd_border'])
    def test_add3(self, x, y):
        expect = "参数大小超出范围"
        assert self.cal.add(x, y) == expect

    @allure.story("相加 P2 级别用例")
    @pytest.mark.P2
    @pytest.mark.parametrize("x,y",
                             yaml.safe_load(open("../../../data/calculador_data.yaml", encoding='utf-8'))['add'][
                                 'chinese'])
    def test_add3(self, x, y):
        with pytest.raises(TypeError) as e:
            result = self.cal(x,y)

if __name__ == "__main__":
    data = yaml.safe_load(open("../../../data/calculador_data.yaml",encoding='utf-8'))
    print(type(data))
    print(data)
    print(data['add']['positive'])

