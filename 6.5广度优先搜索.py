from collections import deque

def preson_is_seller(name):
        return  name[-1]=='m'
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def search(name):
    search_queue=deque()   #创建一个队列
    search_queue+=graph[name]  #将你邻居都加入到这个搜索队列中


    searched=[]
    #这个数组用于记录检查过得人
    while search_queue:  #只要队列不为空
        person=search_queue.popleft()#就取出其中的第一个人 popleft 从队列中取出第一个
        print(searched)
        if not person  in searched: #仅当这个人没检查过才检查
            if preson_is_seller(person): #检查这个人是不是芒果经销商
                print(person+"is a mangp seller")

                return True
            else:
                search_queue+=graph[person] #不是芒果的 把这个人的朋友加到搜索队列
                searched.append(person)   #标记为检查过

    return False

search("you")