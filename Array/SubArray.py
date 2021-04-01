# -*- coding:utf-8 -*-
# @FileName  :SubArray.py
# @Time      :2021/4/1 16:44
# @Author    :Haozr
from typing import List
import unittest


# 解法1：
class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        """53. 最大子序和f(i)代表以第 i个数结尾的「连续子数组的最大和」f(i)=max{f(i−1)+nums[i],nums[i]}"""
        maxSum, pre = nums[0],nums[0]
        for i in range(1,len(nums)):
            pre = max(nums[i],nums[i]+pre)
            maxSum = max(pre,maxSum)
        return maxSum

    def maxSubArrayPos(self, nums: List[int]) -> int:
        """53. 最大子序和的位置 f(i)代表以第 i个数结尾的「连续子数组的最大和」f(i)=max{f(i−1)+nums[i],nums[i]}"""
        maxSum, pre = nums[0], nums[0]
        begin, end = 0, 0
        temp_begin = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i] + pre:
                pre += nums[i]
            else:
                pre = nums[i]
                temp_begin = i
            if pre > maxSum:
                maxSum = pre
                begin, end = temp_begin, i
        print(maxSum, begin, end)
        return maxSum

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """523. 连续的子数组和 包含非负数的数组和一个目标整数 k,是否含有连续的子数组，其大小至少为 2,且总和为 k的倍数"""
        n = len(nums)
        yu = {0:-1}
        sum = 0
        for i in range(n):
            sum += nums[i]
            if k != 0:
                sum %= k
            if sum not in yu:
                yu[sum] = i
            else:
                if i - yu[sum] > 1:
                    return True
        return False

s = Solution()

class TestSolution(unittest.TestCase):

    def test_maxSubArrayPos(self):
        self.assertEqual(s.maxSubArrayPos([-2,1,-3,4,-1,2,1,-5,4]),6)
        self.assertEqual(s.maxSubArrayPos([1]),1)
        self.assertEqual(s.maxSubArrayPos([-1]),-1)
        self.assertEqual(s.maxSubArrayPos([0]),0)
        self.assertEqual(s.maxSubArrayPos([-100000]),-100000)
        self.assertEqual(s.maxSubArrayPos([-5,4]),4)

    def test_checkSubarraySum(self):
        self.assertEqual(s.checkSubarraySum([23,2,4,6,7],6),True)
        self.assertEqual(s.checkSubarraySum([23,2,6,4,7],6),True)
        self.assertEqual(s.checkSubarraySum([5,0,0,0],3),True)
        self.assertEqual(s.checkSubarraySum([1,1],2),True)
        self.assertEqual(s.checkSubarraySum([23,2,6,4,7],13),False)
        self.assertEqual(s.checkSubarraySum([23,2,4,6,6],7),True)
        self.assertEqual(s.checkSubarraySum([1,2,3],5),True)
        self.assertEqual(s.checkSubarraySum([1,2,3],0),False)
        self.assertEqual(s.checkSubarraySum([1,0,2,3,0],0),False)
        self.assertEqual(s.checkSubarraySum([1,2,0,3,0,0],0),True)

if __name__ == '__main__':
    #    s = Solution()
    unittest.main()
