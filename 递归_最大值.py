# @Time    : 2017/10/8
# @File    : sum.py
# @Author  : zhaohui.ren
# 找列表中的最大的值
def max(list):
    if len(list)==2:  #基线条件，就剩下俩个数字
        return list[0] if list[0]>list[1] else list[1]
    sub_max=max(list[1:])
    return list[0] if list[0]>sub_max else sub_max

print(max([1,2,3,4,5,20,15]))