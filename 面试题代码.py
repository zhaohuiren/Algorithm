# 美团服务端面试题
#1.给定一无序列表，如何去重，代码实现
ids=[1,2,3,3,4,2,3,4,5,6,1]
new_ids=[]
for id in ids:
    if id not in new_ids:
        new_ids.append(id)
print(new_ids)


