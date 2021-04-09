# -*- coding:utf-8 -*-
# @FileName  :Array_rotate.py
# @Time      :2021/4/6 13:37
# @Author    :Haozr
from typing import List
import unittest


# 解法1：
class Solution:
        def rotate1(self, nums: List[int], k: int) -> None:
            """189. 旋转数组 将数组中的元素向右移动k个位置 空间换时间"""
            n = len(nums)
            if n == 0:
                return
            k = k % n
            subset = nums[-k:]
            for i in range(n - k - 1, -1, -1):
                nums[i + k] = nums[i]
            i = 0
            for s in subset:
                nums[i] = s
                i += 1
            print(nums)

        def rotate(self, nums: List[int], k: int) -> None:
            """189. 旋转数组 将数组中的元素向右移动k个位置 三次翻转(xT*yT)T=y*x"""
            n = len(nums)
            if n == 0:
                return
            k = k % n
            def sub_rotate(start,end):
                while start < end:
                    nums[start], nums[end] = nums[end], nums[start]
                    start += 1
                    end -= 1
            sub_rotate(0, n-k-1)
            sub_rotate(n-k, n-1)
            sub_rotate(0, n-1)
            print(nums)


s = Solution()


class TestSolution(unittest.TestCase):
    def test_(self):
        self.assertIsNone(s.rotate([1,2],5))
        self.assertIsNone(s.rotate([1,2,3,4,5,6,7],3))
        self.assertIsNone(s.rotate([1,2,3,4,5,6,7],0))
        self.assertIsNone(s.rotate([],10))


if __name__ == '__main__':
    #    s = Solution()
    unittest.main()
