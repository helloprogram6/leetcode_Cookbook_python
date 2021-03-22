# -*- coding:utf-8 -*-
# @FileName  :栈_946.py
# @Time      :2021/3/16 17:17
# @Author    :Haozr
from typing import List


# 解法1：
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """ 946. 验证栈序列 使用一个栈模拟出栈的过程"""
        pu = 0
        n = len(pushed)
        stack = []
        for po in popped:
            if stack and po == stack[-1]:
                stack.pop()
                continue
            while pu < n and po != pushed[pu]:
                stack.append(pushed[pu])
                print(po, pushed[pu], stack)
                pu += 1
            if pu < n and po == pushed[pu]:#跳过第po个数，避免入栈后马上出栈
                pu += 1
            print(stack)
        if stack:
            return False
        return True

if __name__ == '__main__':
    print(Solution().validateStackSequences([1,2,3,4,5],[4,5,3,2,1]))#T
    print(Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))#F
    print(Solution().validateStackSequences([2,1,0], [1,2,0]))#T
