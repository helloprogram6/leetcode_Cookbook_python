# -*- coding:utf-8 -*-
# @FileName  :136_137_260_singleNumber.py
# @Time      :2021/3/25 20:06
# @Author    :Haozr
from typing import List
import unittest


# 解法1：
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """136. 只出现一次的数字 其它元素出现2次 顺序异或 """
        res = 0
        for i in nums:
            res ^= i
        return res

    def singleNumber_137(self, nums: List[int]) -> int:
        """137. 只出现一次的数字 II 其他元素出现3次 在每一位上出现3次就可以变成0 用有限状态机，写逻辑表达式"""
        x,y = 0,0#x,y共同代表一个状态
        for z in nums:#根据nums的输入，调整x y的状态
            x = ~y & (z ^ x)
            y = ~x & (z ^ y)
        print(x,y)
        return x

    def singleNumber_260(self, nums: List[int]) -> List[int]:
        """260. 只出现一次的数字 III 两个数出现1次，其他数出现2次 按照全部异或结果的第n位bit是否为1进行分组"""
        res = 0
        for i in nums:
            res ^= i
        n = res & (-res)
        a = 0
        for i in nums:
            if i & n:
                a ^= i
        b = a^res
        return [a,b]
s = Solution()
class TestSolution(unittest.TestCase):
    def test_137(self):
        self.assertEqual(s.singleNumber_137([2,2,3,2]),3)
        self.assertEqual(s.singleNumber_137([0,1,0,1,0,1,99]),99)

    def test_260(self):
        self.assertEqual(s.singleNumber_260([1, 2, 1, 3, 2, 5]), [3, 5])
        self.assertEqual(s.singleNumber_260([-1, 0]), [-1, 0])


if __name__ == '__main__':
#    s = Solution()
    unittest.main()
