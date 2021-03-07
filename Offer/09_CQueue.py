# -*- coding:utf-8 -*-
# @FileName  :09_CQueue.py
# @Time      :2021/3/2 21:58
# @Author    :Haozr
from typing import List


# 解法1：
class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if self.stack2:#栈2不为空
            return self.stack2.pop()
        else:#栈2为空，将栈1中的元素出栈到栈2
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            if self.stack2:
                return self.stack2.pop()
            else:
                return -1
class Solution:
    def fib(self, n: int) -> int:
        """offer 10-1斐波那契数列"""
        a, b = 0, 1
        if n == 0:
            return 0
        while n > 1:
            n -= 1
            a, b = b, a + b
        return b % 1000000007

    def numWays(self, n: int) -> int:
        """offer 10-2青蛙跳台阶"""
        a, b = 1, 2
        while n > 1:
            n -= 1
            a, b = b, a + b
        return a % 1000000007

if __name__ == '__main__':
    print(Solution().numWays(7))
    value = 1
    obj = CQueue()
    obj.appendTail(value)
    obj.appendTail(2)
    obj.appendTail(3)
    obj.appendTail(4)
    print(obj.stack1," / ",obj.stack2)
    param_2 = obj.deleteHead()
    print(obj.stack1, " / ", obj.stack2,param_2)
    obj.appendTail(5)
    print(obj.stack1, " / ", obj.stack2)
    param_2 = obj.deleteHead()
    print(obj.stack1, " / ", obj.stack2, param_2)
