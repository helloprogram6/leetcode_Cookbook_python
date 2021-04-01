# -*- coding:utf-8 -*-
# @FileName  :tt.py
# @Time      :2021/3/30 19:49
# @Author    :Haozr
from typing import List
import unittest

"""
# 解法1：
class Solution:


s = Solution()


class TestSolution(unittest.TestCase):
    def test_(self):
        self.assertEqual(s.)
        self.assertEqual(s.)
"""
t = input().split(' ')
n = int(t[0])
if n > 1:
    m = int(t[1])
ml = []
pos = [(-1,0),(1,0),(0,-1),(0,1)]
for i in range(n):
    t = input().split(' ')
    k = []
    for j in t:
        k.append(int(j))
    ml.append(k)
for i in range(n):
    for j in range(m):
        sum = ml[i][j]
        num = 1
        for pi,pj in pos:
            if -1<pi+i<n and -1<pj+j<m:
                sum += ml[pi+i][pj+j]
                num += 1
        ml[i][j] = int(sum/num + 0.5)%256
for i in range(n):
    str1 = ""
    for j in range(m):
        str1 += str(ml[i][j])+' '
    print(str1)

if __name__ == '__main__':
    #    s = Solution()
    #unittest.main()
    pass
