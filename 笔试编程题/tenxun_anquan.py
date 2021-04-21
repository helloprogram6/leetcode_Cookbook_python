# -*- coding:utf-8 -*-
# @FileName  :tenxun_anquan.py
# @Time      :2021/4/3 21:22
# @Author    :Haozr
from typing import List
import unittest


# 解法1：
class Solution:
    def ispipei(self,ss:str):
        """括号匹配 一串字符须按照{[()]}的顺序匹配，否则返回-1 """
        stack = []
        for s in ss:
            print(s,stack)
            if s == '{':
                if stack and (stack[-1] == '(' or stack[-1] == '[' ):
                    return -1
                stack.append(s)
            elif s == '[':
                if stack and stack[-1] == '(':
                    return -1
                stack.append(s)
            elif s == '(':
                stack.append(s)
            elif s == '}':
                if not stack:
                    return -1
                if stack[-1] != '{':
                    return -1
                else:
                    stack.pop()
            elif s == ']':
                if not stack:
                    return -1
                if stack[-1] != '[':
                    return -1
                else:
                    stack.pop()
            elif s == ')':
                if not stack:
                    return -1
                if stack[-1] != '(':
                    return -1
                else:
                    stack.pop()
        print("*******")
        if stack:
            return -1
        else:
            return 1

s = Solution()


class TestSolution(unittest.TestCase):
    def test_(self):
        self.assertEqual(s.ispipei("{skjdf[killl]}"),1)
        self.assertEqual(s.ispipei("[kdfdl]"),1)
        self.assertEqual(s.ispipei("(sdfsgg)"),1)
        self.assertEqual(s.ispipei("([]ksdfs"),-1)
        self.assertEqual(s.ispipei("([])"),-1)
        self.assertEqual(s.ispipei("({})"),-1)
        self.assertEqual(s.ispipei("[{}]"),-1)


if __name__ == '__main__':
    #    s = Solution()
    unittest.main()
