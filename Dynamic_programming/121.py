# -*- coding:utf-8 -*-
# @FileName  :121.py
# @Time      :2021/4/13 12:53
# @Author    :Haozr
from typing import List
import unittest


# 解法1：
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ 121. 买卖股票的最佳时机"""
        n = len(prices)
        if n < 2:
            return 0
        minprice = prices[0]
        maxprofit = 0
        for i in prices:
            if i - minprice > maxprofit:
                maxprofit = i - minprice
            if i < minprice:
                minprice = i
        return maxprofit
s = Solution()


class TestSolution(unittest.TestCase):
    def test_121(self):
        self.assertEqual(s.maxProfit([7,6,4,3,1]),0)
        self.assertEqual(s.maxProfit([7,1,5,3,6,4]),5)


if __name__ == '__main__':
    #    s = Solution()
    unittest.main()
