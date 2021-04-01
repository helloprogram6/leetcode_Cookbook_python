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
        x,y = 0,0#x,y共同代表一个状态 00表示其他元素出现0次，01表示1次，10表示2次；即00+1=01，01+1=10，10+1=00
        for z in nums:#根据nums的输入，调整x y的状态 x=-y(x*-z+-x*z) y=-x(y*-z+-y*z)
            x = ~y & (z ^ x)
            y = ~x & (z ^ y)
        print(x,y)
        return x

    def singleNumber_260(self, nums: List[int]) -> List[int]:
        """260. 只出现一次的数字 III 两个数a,b出现1次，其他数出现2次 按照全部异或结果的第n位bit是否为1进行分组"""
        res = 0
        for i in nums:
            res ^= i
        n = res & (-res)#负数的补码是全部取反加1
        # res = a^b res的第n位bit为1，是因为a或者b在第n位上的bit位不一致，依此分为两组，把情况转化为136的情况
        a = 0
        for i in nums:
            if i & n:
                a ^= i
        b = a^res
        return [a,b]

    def isOne(self, nums: List[int]) -> int:
        """三个数出现1次，其余数出现偶次，输出3个数中任意一个 """
        length = len(nums)
        n = 1
        for j in range(32):#按照每个bit把所有数分为两组，a,b,c总会分别分为两个组中
            n <<= j
            a = 0
            b = 0
            t = 0
            for i in nums:
                if i & n:
                    a ^= i
                    t += 1
                else:
                    b ^= i
            if t % 2 != 0:#有一个组的个数为奇数
                return a
            if (length - t) % 2 !=0:
                return b
        return -1

s = Solution()
class TestSolution(unittest.TestCase):
    def test_137(self):
        self.assertEqual(s.singleNumber_137([2,2,3,2]),3)
        self.assertEqual(s.singleNumber_137([0,1,0,1,0,1,99]),99)

    def test_260(self):
        self.assertEqual(s.singleNumber_260([1, 2, 1, 3, 2, 5]), [3, 5])
        self.assertEqual(s.singleNumber_260([-1, 0]), [-1, 0])

    def test_isOne(self):
        self.assertIn(s.isOne([6,3,4,5,9,4,3]),[6,5,9])

if __name__ == '__main__':
#    s = Solution()
    unittest.main()
