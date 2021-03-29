# -*- coding:utf-8 -*-
# @FileName  :268_missingNumber.py
# @Time      :2021/3/25 19:37
# @Author    :Haozr
from typing import List
import unittest


# 解法1：
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """ 268. 丢失的数字 求和或者异或"""
        n = len(nums)
        t = n
        for i in range(n):
            t ^= i ^ nums[i]
        return t

class TestSolution(unittest.TestCase):
    def test_missingNumber(self):
        s = Solution()
        self.assertEqual(s.missingNumber([3,0,1]),2)

        self.assertEqual(s.missingNumber([0,1]),2)


if __name__ == '__main__':
    s = Solution()
    unittest.main()
