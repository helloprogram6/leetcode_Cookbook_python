# -*- coding:utf-8 -*-
# @FileName  :数组去重.py
# @Time      :2021/3/20 14:33
# @Author    :Haozr
from typing import List


# 解法1：
class Solution:


    def findRepeatNumber(self, nums: List[int]) -> int:
        """ 剑指 Offer 03. 数组中重复的数字 原地置换，长度为n的数组数值：[0:n-1]"""
        for n in range(len(nums)):
            print(n,nums[n],nums[nums[n]],nums)
            if n != nums[n] and nums[n] == nums[nums[n]]:
                return nums[n]
            else:
                temp = nums[nums[n]]
                nums[nums[n]] = nums[n]
                nums[n] = temp

if __name__ == '__main__':
    s = Solution()
    print(s.findRepeatNumber([3, 1, 2, 3]))#3
    print(s.findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))#2或3
    print(s.findRepeatNumber([0, 1, 2, 3, 4, 11, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))#11

