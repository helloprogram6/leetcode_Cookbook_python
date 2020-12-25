# -*- coding:utf-8 -*-
# @FileName  :27_removeElement.py
# @Time      :2020/12/23 21:49
# @Author    :Haozr
from typing import List


# 解法1：当 nums[j]与给定的值相等时，递增j以跳过该元素。只要nums[j]≠val,我们就复制nums[j]到nums[i],并同时递增两个索引。
# 重复这一过程，直到 j到达数组的末尾，该数组的新长度为 i。
#
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        if length == 0:
            return 0
        i,j = 0,0
        while(j < length):
            print(nums)  # tests
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i
# 解法二：用后面的数覆盖前面是val的数
class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        i = 0
        while(i < n):
            print(nums,i,n)#test
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n
if __name__ == '__main__':
    nums,val = [3,2,2,3],3
    nums1,val1 = [0, 1, 2, 2, 3, 0, 4, 2],2
    nums2,val2 = [2],2
    print(Solution1().removeElement(nums1,val1))
