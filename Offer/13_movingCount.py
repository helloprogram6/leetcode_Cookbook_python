# -*- coding:utf-8 -*-
# @FileName  :13_movingCount.py
# @Time      :2021/3/4 22:00
# @Author    :Haozr
from typing import List


# 解法1：
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        """广度优先搜索"""
        def he(s):
            sum = 0
            while s != 0:
                sum += s%10
                s = s // 10
            return sum
        stack = [(0,0)]
        res = 0
        s = set()#集合，存放走过的所有路径
        while stack:
            res += 1
            i,j = stack.pop()
            s.add((i,j))
            if 0 <= i+1 < m and 0 <= j < n and he(i+1) + he(j) <= k and (i+1,j) not in s:#向右搜索
                stack.append((i+1,j))
            if 0 <= i < m and 0 <= j+1 < n and he(i) + he(j+1) <= k and (i,j+1) not in s:#向下搜索
                stack.append((i, j+1))
        return res

if __name__ == '__main__':
    print(Solution().movingCount(16,8,4))#16 8 4-> 15
