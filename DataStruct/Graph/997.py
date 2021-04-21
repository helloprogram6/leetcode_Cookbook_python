# -*- coding:utf-8 -*-
# @FileName  :997.py
# @Time      :2021/4/12 23:24
# @Author    :Haozr
from typing import List
import unittest


# 解法1：
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        """997. 找到小镇的法官 就是寻找 出度为0,入度为N-1的结点 只有法官的入度和出度的差值为 n-1"""
        counts = [0] * (N+1)
        for i, j in trust:
            counts[j] += 1
            counts[i] -= 1
        for i in range(1, N+1):
            if counts[i] == N - 1:
                return i
        return -1

s = Solution()


class TestSolution(unittest.TestCase):
    def test_(self):
        self.assertEqual(s.findJudge(2, [[1,2]]),2)
        self.assertEqual(s.findJudge(3, [[1,3],[2,3],[3,1]]),-1)
        self.assertEqual(s.findJudge(1, []),1)
        self.assertEqual(s.findJudge(2, []),-1)
        self.assertEqual(s.findJudge(2,[[1,2],[2,1]]),-1)


if __name__ == '__main__':
    #    s = Solution()
    unittest.main()
