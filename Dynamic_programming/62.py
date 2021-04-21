# -*- coding:utf-8 -*-
# @FileName  :62.py
# @Time      :2021/4/13 14:06
# @Author    :Haozr
from typing import List
import unittest


# 解法1：
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """62. 不同路径 dp[0,*]= 1,dp[*,0]=1; dp[i,j]=dp[i-1,j]+dp[i,j-1]==>空间优化为dp[j]=dp[j]+dp[j-1]"""
        # 因为只要上一行就可以计算本行
        if m > n:
            m, n = n, m
        dp = [1] * n
        for _ in range(1, m):
            for i in range(1, n):
                dp[i] = dp[i] + dp[i-1]
        return dp[n-1]

s = Solution()


class TestSolution(unittest.TestCase):
    def test_(self):
        self.assertEqual(s.uniquePaths(3,7),28)
        self.assertEqual(s.uniquePaths(3,2),3)
        self.assertEqual(s.uniquePaths(7,3),28)
        self.assertEqual(s.uniquePaths(3,3),6)


if __name__ == '__main__':
    #    s = Solution()
    unittest.main()
