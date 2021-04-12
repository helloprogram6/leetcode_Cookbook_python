# -*- coding:utf-8 -*-
# @FileName  :Ugly_263_264.py
# @Time      :2021/4/11 12:41
# @Author    :Haozr
from typing import List
import unittest
"""
丑数 就是只包含质因数 2、3 和/或 5 的正整数。
"""

# 解法1：
class Solution:
    def isUgly(self, n: int) -> bool:
        """263 判断 n 是否为丑数"""
        if n < 1:
            return False
        while n != 1:
            if n % 5 == 0:
                n = n / 5
            elif n % 3 == 0:
                n = n/3
            elif n % 2 == 0:
                n = n /2
            else:
                return False
        return True

    def nthUglyNumber(self, n: int) -> int:
        """264 返回第 n 个丑数 用三个指针dp2,dp3,dp5"""
        # dp2 代表还没有与2相乘的最小丑数的位置
        dp2, dp3, dp5 = 1, 1, 1
        dp = [0] * ( n + 1)
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = min(dp[dp2]*2, dp[dp3]*3, dp[dp5]*5)
            if dp[i] == dp[dp2] * 2:
                dp2 += 1
            if dp[i] == dp[dp3] * 3:
                dp3 += 1
            if dp[i] == dp[dp5] * 5:
                dp5 += 1
        return dp[n]

s = Solution()


class TestSolution(unittest.TestCase):
    def test_264(self):
        self.assertEqual(s.nthUglyNumber(10),12)
        self.assertEqual(s.nthUglyNumber(1),1)


if __name__ == '__main__':
    #    s = Solution()
    unittest.main()
