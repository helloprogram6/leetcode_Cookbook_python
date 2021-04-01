# -*- coding:utf-8 -*-
# @FileName  :元素距离.py
# @Time      :2021/4/1 11:20
# @Author    :Haozr
from typing import List
import unittest


# 解法1：
class Solution:
    def minDistance1(self,nums:List[int],num1:int,num2:int)->int:
        """ 数组存在重复元素，求num1和num2的最短距离 """
        if num1 == num2:
            return 0
        pos1 = []
        pos2 = []
        for i,v in enumerate(nums):
            if v == num1:
                pos1.append(i)
            if v == num2:
                pos2.append(i)
        if len(pos1) == 0 or len(pos2) == 0:
            return -1#num1 or num2元素不存在数组中
        mindistance = len(nums)
        for i in pos1:
            for j in pos2:
                t = abs(i -j)
                if t < mindistance:
                    mindistance = t
        return mindistance

    def minDistance(self,nums:List[int],num1:int,num2:int)->int:
        """ 数组存在重复元素，求num1和num2的最短距离 最优解"""
        pos1, pos2 = None, None
        mind = len(nums)
        for i,v in enumerate(nums):
            if v == num1:
                pos1 = i
                if pos2:
                    mind = min(abs(pos1-pos2),mind)
            elif v == num2:
                pos2 = i
                if pos1:
                    mind = min(abs(pos1 - pos2), mind)
        return mind
s = Solution()


class TestSolution(unittest.TestCase):
    def test_minDistance(self):
        self.assertEqual(s.minDistance([4,5,6,4,7,4,6,4,7,8,5,6,4,3,10,8],4,8),2)
        self.assertEqual(s.minDistance1([4,5,6,4,7,4,6,4,7,8,5,6,4,3,10,8],4,8),2)


if __name__ == '__main__':
    #    s = Solution()
    unittest.main()
