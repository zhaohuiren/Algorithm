#-*- coding: utf-8 -*-
# @Time    : 2017/9/29
# @File    : 排序.py
# @Author  : zhaohui.ren
# 排序

def findSmallest(arr):
#找最小的值
    smallest=arr[0] #存储最小的值
    smallest_index=0    #存储最小元素的索引
    for i in range(1,len(arr)): #从1开始一个一个取
        if arr[i]<smallest:  #如果小于最小值
            smallest=arr[i]  #最小值就=这个数
            smallest_index=i  #索引
    return  smallest_index


def selectionSort(arr):
#排序
    newArr=[]  #新建一个数组
    for i in range(len(arr)):
        smallest=findSmallest(arr)#找出数组中最小的元素。加入新的数组
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5,3,6,2,10]))

