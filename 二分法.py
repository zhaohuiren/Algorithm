#-*- coding: utf-8 -*-
# @Time    : 2017/9/27
# @File    : 二分法.py
# @Author  : zhaohui.ren
# 二分法 当列表为顺序排列 二分法才有用
def binary_search(list,item):
    low=0
    high=len(list)-1

    while low<=high: #只要范围没有缩小到一个元素
        mid=(low+high)//2#查找中间的元素
        guess=list[mid]
        if guess==item: #查到了就之间返回中间的
            return mid


        if guess>item:#如果大于查到的数
            high=mid-1 #高度就-1

        else: #猜的数字小了
            low=mid+1#最小值就+1
    return None

my_list=[1,3,5,7,9]
print(binary_search(my_list,3))