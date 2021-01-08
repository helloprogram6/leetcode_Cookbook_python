# -*- coding:utf-8 -*-
# @FileName  :41_firstMissingPositive.py
# @Time      :2020/12/28 14:39
# @Author    :Haozr
from typing import List


# 解法1：【原地哈希】为了减少时间复杂度，可以把 input 数组都装到 map 中，
# 然后 i 循环从 1 开始，依次比对 map 中是否存在 i，
# 只要不存在 i 就立即返回结果，即所求。
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        maps = {}
        for i in range(length):
            maps[nums[i]] = i
        j = 1
        while j in maps:
            j += 1
        return j
#解法2：【置换】如果x在[1,n]之间的话，数字x应该在x-1的位置上。第一次循环将数组重新排序，[3,4,-1,1]--->>[-1,1,3,4]
#第二次循环依次查看哪个位置上的数不正确，就缺少哪个正数；都正确，缺少n+1。
    def firstMissingPositive2(self, nums: List[int]) -> int:
        length = len(nums)
        i = 0
        while i<length:
            if 0<nums[i]<length and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
            else:
                i += 1
        for i in range(length):
            if nums[i] != i+1:
                return i+1
        return length+1 #考虑到顺序数组[1,2,3,4]这种

if __name__ == '__main__':
    nums = [1,2,0]
    nums1 = [3,4,-1,1]
    nums2 = [7,8,9,11,12]
    nums3 = [1]
    print(Solution().firstMissingPositive2(nums3))
