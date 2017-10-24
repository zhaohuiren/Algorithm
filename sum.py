#-*- coding: utf-8 -*-
# @Time    : 2017/10/8
# @File    : sum.py
# @Author  : zhaohui.ren
# 将一个数字数组相加
def sum(arr):
    total=0
    for x in arr:
        total+=x
    return total
print(sum([1,2,3,5]))