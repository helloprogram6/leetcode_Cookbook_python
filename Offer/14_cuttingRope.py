# -*- coding:utf-8 -*-
# @FileName  :14_cuttingRope.py
# @Time      :2021/3/6 21:18
# @Author    :Haozr
from typing import List


# 解法1：
class Solution:
    def cuttingRope(self, n: int) -> int:
        """offer 14-I 剪绳子 绳子优先距离：3>2>1"""
        if n <= 3:
            return n - 1
        a, b  = n//3, n%3
        if b == 1:
            return 3**(a-1)*4
        elif b == 2:
            return 3**a*b
        else:
            return 3**a

    def cuttingRope1(self,n:int) ->int:
        """动态规划 转移方程：dp[i] = max(dp[i],max(j*(i-j),j*dp[i-j]) dp存放结果，绳长i剪j剩下i-j"""
        dp = [0,1,1,2]
        for i in range(4, n+1):
            dp.append(1)
            for j in range(2, i):
                dp[i] = max(dp[i],j*(i-j),j*dp[i-j])
        return dp[n]




if __name__ == '__main__':
    print(Solution().cuttingRope1(6))
