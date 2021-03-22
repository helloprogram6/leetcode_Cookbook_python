# -*- coding:utf-8 -*-
# @FileName  :1679_K 和数对的最大数目.py
# @Time      :2021/3/17 10:06
# @Author    :Haozr
from typing import List


# 解法1：
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """1679 K和数对的最大数目 使用哈希表"""
        h = {}
        for n in nums:
            if n in h:
                h[n] += 1
            else:
                h[n] = 1
        res = 0
        for key,val in h.items():
            if k - key in h and  k - key != key:
                res += min(h[key],h[k-key])
        if k%2 == 0 and k //2 in h:
            return res // 2 + h[k//2]//2
        return res // 2


if __name__ == '__main__':
    print(Solution().maxOperations([3,1,3,4,3],6))
    print(Solution().maxOperations([1,2,3,4],5))




