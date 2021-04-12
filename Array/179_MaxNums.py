# -*- coding:utf-8 -*-
# @FileName  :179_MaxNums.py
# @Time      :2021/4/12 20:32
# @Author    :Haozr
from typing import List
import unittest


# 解法1：
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """179. 最大数 直接排序"""
        import functools
        nums_str = list(map(str,nums))
        #nums_str.sort(key=functools.cmp_to_key(lambda x,y: 1 if x+y<y+x else -1))
        nums_str = sorted(nums_str, key=functools.cmp_to_key(lambda x,y: 1 if x+y<y+x else -1))
        res = ''.join(nums_str)
        if res[0] == '0':
            return '0'
        return res
s = Solution()


class TestSolution(unittest.TestCase):
    def test_179(self):
        self.assertEqual(s.largestNumber([10,2]),'210')
        self.assertEqual(s.largestNumber([10,20]),'2010')


if __name__ == '__main__':
    #    s = Solution()
    unittest.main()
