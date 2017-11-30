#-*- coding: utf-8 -*-
# @Time    : 2017/11/29
# @File    : 贪婪算法.py
# @Author  : zhaohui.ren
# 贪婪算法
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
#创建一个列表 里边有所有的洲 传入一个数组，他被转换成集合
#散列表
stations={}
stations["kone"]=set(["id","nv","ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])
#集合在存储最终的电台
final_stations=set()

while states_needed:
    #存最多未覆盖州的广播台
    best_station=None
    states_covered=set() #未覆盖的洲
    for station,states in stations.items():
        covered=states_needed&states  #计算交集
        if len(covered)>len(states_covered): #检查覆盖的州是否比未覆盖的州多
            best_station=station
            states_covered=covered
    states_needed-=states_covered
    final_stations.add(best_station)

print(final_stations)








