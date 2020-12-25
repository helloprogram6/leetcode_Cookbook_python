# -*- coding:utf-8 -*-
# @FileName  :26_removeDuplicates.py
# @Time      :2020/12/23 21:22
# @Author    :Haozr
from typing import List


# 解法1：数组去重，两个指针，将不重复的数移动到前面，直接覆盖不移动
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        i,j = 0,0
        while(j < length):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i+1


if __name__ == '__main__':
    nums = [1,1,2]
    nums1 = [0,0,1,1,1,2,2,3,3,4]
    nums2 = []
    print(Solution().removeDuplicates(nums2))
