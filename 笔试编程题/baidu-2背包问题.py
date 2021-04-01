# -*- coding:utf-8 -*-
# @FileName  :baidu2.py
# @Time      :2021/3/30 20:27
# @Author    :Haozr

t = input().split(' ')
n = int(t[0])
m = int(t[1])
k = int(t[2])

weight = []
price = []
v = []
for i in range(n):
    t = input().split(' ')
    weight.append(int(t[0]))
    price.append(int(t[1]))
    v.append(int(t[2]))

save = []
rw = m
rm = k
for i in range(n):
    if weight[i] < rw and price[i] < rm:
        save += 1
        rw -= weight[i]
        rm -= price
        save.append(i)
for i in range(len(save)):
    for j in range(n):
        if i == j:
            continue
        if v[j] >= v[i] and weight[j] <= weight[i] and price[j] < price[i]:
            save.reverse()
print(len(save))