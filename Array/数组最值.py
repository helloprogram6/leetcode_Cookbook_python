# -*- coding:utf-8 -*-
# @FileName  :数组最值.py
# @Time      :2021/3/20 15:08
# @Author    :Haozr
from typing import List


# 解法1：
class Solution:
    def findMin2(self, nums: List[int]) -> int:
        """153. 寻找旋转排序数组中的最小值 同offer-11
        154. 寻找旋转排序数组中的最小值 II 数组中有重复元素
        顺序遍历寻找旋转点
        """
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return nums[i+1]
        if nums:
            return nums[0]
        else:
            return None
    def findMin(self, nums: List[int]) -> int:
        """153. 寻找旋转排序数组中的最小值 同offer-11
        变形的二分查找：寻找旋转点
        """
        low,high = 0,len(nums)-1
        while low < high:
            mid = low + (high - low) // 2
            if nums[high] > nums[mid]:#[mid:high]这右半部分是正常增序,min在左半部分
                high = mid
            elif nums[high] < nums[mid]:#min在右半部分，[low:mid]这左半部分是正常增序
                low = mid + 1
            else:#忽略high这个端点
                high -= 1
        return nums[low]

    def findMin154(self, nums: List[int]) -> int:
        """"""
        pass

if __name__ == '__main__':
    s = Solution()
    print(s.findMin([3,4,5,1,2]))
    print(s.findMin([4,5,6,7,0,1,2]))
    print(s.findMin([1]))
    print(s.findMin2([0,1,2,2,2,-1]))
