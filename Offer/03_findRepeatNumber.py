# -*- coding:utf-8 -*-
# @FileName  :findRepeatNumber.py
# @Time      :2021/2/28 20:44
# @Author    :Haozr
from typing import List


# 解法1：
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                return num
        return 0


if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5, 3]
    print(Solution().findRepeatNumber(nums))
