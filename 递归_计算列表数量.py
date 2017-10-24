
# @Time    : 2017/10/8
# @File    : sum.py
# @Author  : zhaohui.ren
# 将一个数字数组相加
def count(list):
    if list==[]:
        return 0
    return  1+count(list[1:])

print(count([1,2,3,45]))