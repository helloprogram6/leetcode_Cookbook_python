# -*- coding:utf-8 -*-
# @FileName  :Top.py
# @Time      :2021/3/24 10:33
# @Author    :Haozr
import unittest
from typing import List
import heapq

# 解法1：
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """347. 前K个高频元素 建hash表，然后调整k次堆 nlogk"""
        h = {}
        for n in nums:#建哈希表
            if n in h:
                h[n] += 1
            else:
                h[n] = 1
        print(h)
        #堆排序
        res = []
        #l = sorted(h.items(),key = lambda k:k[1],reverse=True)
        #print(l)
        h = list(h.items())
        for t in range(1,k+1,1):
            print(h,t)
            n = len(h) - t
            i = n // 2
            if n % 2:
                if h[n][1] > h[i][1]:
                    h[n],h[i] = h[i],h[n]
                n -= 1
            for j in range(i - 1,-1,-1):
                for _ in range(2):
                    if h[n][1] > h[j][1]:
                        h[n], h[j] = h[j], h[n]
                    n -= 1
            h[0],h[len(h) - t] = h[len(h) - t],h[0]
            res.append(h[len(h) - t][0])
        print(", ", h, t)
        return res

    #def
        """692. 前K个高频单词 """

class TestSolution(unittest.TestCase):
    def test_topKFrequent(self):
        s = Solution()
        nums = s.topKFrequent([1,2,3,4,2,3,-1],2)
        self.assertEqual(nums,[3,2])

        nums = s.topKFrequent([1, 1,1,1,1], 1)
        self.assertEqual(nums, [1])
if __name__ == '__main__':
    #s = Solution()
    #print(s.topKFrequent([1,1,1,2,2,3],2))
    #print(s.topKFrequent([4,1,-1,2,-1,2,3],2))
    unittest.main()