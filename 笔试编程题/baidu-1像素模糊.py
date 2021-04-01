# -*- coding:utf-8 -*-
# @FileName  :te.py
# @Time      :2021/3/29 19:07
# @Author    :Haozr

nums = int(input())
tt = input().split(" ")
n = int(tt[0])
m = int(tt[1])
d = int(tt[2])
Tu = {}
for i in range(n):
    Tu[i] = {i:0}
for _ in range(m):
    tt = input().split(" ")
    start = int(tt[0])
    end = int(tt[1])
    dis = int(tt[2])
    Tu[start][end] = dis
def dijk(Tu,v):
    book = set()
    minv = v
    dis = dict((k,9999)for k in Tu.keys())
    dis[v] = 0
    while len(book) < len(Tu):
        book.add(minv)
        for w in Tu[minv]:
            if dis[minv] + Tu[minv][w] < dis[w]:
                dis[w] = dis[minv] + Tu[minv][w]
        new = 99999
        for v in dis.keys():
            if v in book:
                continue
            if dis[v] < new:
                new = dis[v]
                minv = v
    return dis

"""选票问题-暴力
#    s = Solution()
n = int(input())
l = input().split(" ")
l = [int(i) for i in l]
#n = 5
#l = [1,1,1,5,1]
max = 0
sum = 0
for i in l:
    sum += i
    if i>max:
        max = i
if n*max > 2*sum:
    print(max)
else:
    while n*max <= 2*sum:
        max += 1
    print(max)
"""
