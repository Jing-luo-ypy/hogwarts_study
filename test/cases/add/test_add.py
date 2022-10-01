#!/usr/bin/python
# _*_ coding: utf-8 _*_
# @Time :2022/9/25 15:38
# Author : jingluo~
# @File : test_add.py
import pytest
from func.calculator import Calculator

def setup_module():
    print("开始测试")

def teardown_module():
    print("结束测试")

class TestAdd:
    def setup_class(self):
        self.cal = Calculator()

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    @pytest.mark.pstv1
    def test_add11(self):
        result = self.cal.add(1,1)
        expect = 2
        assert result == expect

    @pytest.mark.pstv2
    def test_add12(self):
        result = self.cal.add(-0.01,0.02)
        expect = 0.01
        assert result == expect

    @pytest.mark.pstv3
    def test_add13(self):
        result = self.cal.add(10,0.02)
        expect = 10.02
        assert result == expect

    @pytest.mark.ef_border1
    def test_add21(self):
        result = self.cal.add(98.99,99)
        expect = 197.99
        assert result == expect

    @pytest.mark.ef_border2
    def test_add22(self):
        result = self.cal.add(99,98.99)
        expect = 197.99
        assert result == expect

    @pytest.mark.ef_border3
    def test_add23(self):
        result = self.cal.add(-99,-98.99)
        expect = -197.99
        assert result == expect

    @pytest.mark.ef_border4
    def test_add24(self):
        result = self.cal.add(-98.99,-99)
        expect = -197.99
        assert result == expect

    @pytest.mark.invd_border1
    def test_add31(self):
        result = self.cal.add(99.01,0)
        expect = "参数大小超出范围"
        assert result == expect

    @pytest.mark.invd_border2
    def test_add32(self):
        result = self.cal.add(-99.01,-1)
        expect = "参数大小超出范围"
        assert result == expect

    @pytest.mark.invd_border3
    def test_add33(self):
        result = self.cal.add(2,99.01)
        expect = "参数大小超出范围"
        assert result == expect

    @pytest.mark.invd_border4
    def test_add34(self):
        result = self.cal.add(1,-99.01)
        expect = "参数大小超出范围"
        assert result == expect

    @pytest.mark.invd_ch1
    def test_add41(self):
        # try:
        #     result = self.cal.add('文',9.3)
        # except TypeError as e:
        #     print(e)
        with pytest.raises(TypeError) as e:
            result = self.cal.add('文',9.3)

    @pytest.mark.invd_ch2
    def test_add42(self):
        result = self.cal.add(4,'字')
        expect = "参数大小超出范围"
        assert result == expect

