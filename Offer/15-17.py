# -*- coding:utf-8 -*-
# @FileName  :15-17.py
# @Time      :2021/3/7 10:29
# @Author    :Haozr
from typing import List


# 解法1：
class Solution:
    def hammingWeight(self, n: int) -> int:
        """15 二进制中1的个数 转为字符串"""
        num = 0
        for s in bin(n):
            if s == '1':
                num += 1
        return num
    def hammingWeight1(self,n:int)->int:
        """15 二进制中1的个数 位运算 n&(n-1)将最小位1置0"""
        res = 0
        while n !=0:
            n = n & (n-1)
            res += 1
        return res

    def myPow(self, x: float, n: int) -> float:
        """16 数值的整数次方 实现pow() 快速幂"""
        if x == 0:
            return 0
        if n < 0:
            n = -n
            x = 1/x
        res = 1
        while n:
            print(x,n)
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res
    def printNumbers(self, n: int) -> List[int]:
        """17 打印从1到最大的n位数"""
        return [i for i in range(1,10**n)]


if __name__ == '__main__':
    #print(Solution().hammingWeight(11))
    #print(Solution().myPow(3,11))
    print(Solution().printNumbers(1))
