# -*- coding:utf-8 -*-
# @FileName  :wangyi_2.py
# @Time      :2021/4/10 15:16
# @Author    :Haozr
from typing import List
import unittest

class TreeNode:
    def __init__(self, x,left=None,right=None):
        self.val = x
        self.left = left
        self.right = right
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @return int整型
#
class Solution:
    def roomsAfterNDays(self , rooms , N ):
        # write code here 病房
        n = len(rooms)
        for j in range(N):
            print(rooms)
            pre = 0
            if j == 0:
                for i in range(n):
                    if i == 0 or i == n-1:
                        rooms[i] = 0
                        pre = 0
                    else:
                        temp = pre
                        pre = rooms[i]
                        if temp == rooms[i+1]:
                            rooms[i] = 1
                        else:
                            rooms[i] = 0
            else:
                for i in range(1,n-1):
                    temp = pre
                    pre = rooms[i]
                    if temp == rooms[i + 1]:
                        rooms[i] = 1
                    else:
                        rooms[i] = 0
        return rooms

    def maxWater(self , height ):
        # write code here 木桩水池
        maxres = 0
        res = 0
        max = height[0]
        n = len(height)
        for i in range(1, n):
            if height[i] >= max:
                max = height[i]
                if maxres < res:
                    maxres = res
                    res = 0
            else:
                res = res + max - height[i]
        max = height[n - 1]
        res = 0
        for i in range(n - 2, -1, -1):
            if height[i] >= max:
                max = height[i]
                if maxres < res:
                    maxres = res
                    res = 0
            else:
                res = res + max - height[i]
        return maxres

    def maxMoney(self , root ):
        # write code here 卖樱桃
        def isNode(t):
            if t.left or t.right:
                return False
            else:
                return True
        if root == None or isNode(root):
            return 0
        elif root.left == None and root.right != None:
            if isNode(root.right):
                return 2
            return self.maxMoney(root.right)
        elif root.left != None and root.right == None:
            if isNode(root.left):
                return 2
            return self.maxMoney(root.left)
        else:
            if isNode(root.left) and not isNode(root.right):
                return 2 + self.maxMoney(root.right)
            elif not isNode(root.left) and isNode(root.right):
                return 2 + self.maxMoney(root.left)
            elif isNode(root.left) and isNode(root.right):
                return 5
            else:
                return int(self.maxMoney(root.left) + self.maxMoney(root.right))

print(Solution().roomsAfterNDays([0,1,0,1,1,0,0,1,0,1,1],3))

#print(Solution().maxWater([4, 3, 2, 1, 3, 0, 5, 0, 1]))
#print(Solution().maxMoney(TreeNode(1,TreeNode(2,TreeNode(4)),TreeNode(3,TreeNode(5,TreeNode(7),TreeNode(8)),TreeNode(6,None,TreeNode(9))))))

def solution(n):
    # write code here变形的斐波拉数列
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a, b, c = 0, 1, 2
        i = 3
        while i <= n:
            a, b, c = b, c, a + b + c
            i += 1
        return c
#print(solution(14))#6
