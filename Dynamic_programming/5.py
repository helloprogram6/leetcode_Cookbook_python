# -*- coding:utf-8 -*-
# @FileName  :5.py
# @Time      :2021/4/11 15:28
# @Author    :Haozr
from typing import List
import unittest


# 解法1：
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """5. 最长回文子串 动态规划 i是回文子串; ij是回文子串的前提是i==j; i...j是回文子串的前提是 ...是回文子串并且i==j"""
        # S表示字符串，P(i,j)表示S[i:j]是否为回文子串
        # 动态方程为 P(i,j)=P(i+1,j−1)∧(Si​==Sj)
        # 边界是：P(i,j)=true; P(i,i+1)=(Si==Sj)
        # 以一个字符、两个字符为中心向两边扩展，即可得到所有的回文子串，求出最长的即可 O(n^2)--O(1)，
        ress = ''
        maxlen = 0
        n = len(s)
        for k in range(n):
            i = j = k
            while True:
                i, j = i - 1, j + 1
                if i >= 0 and j < n:
                    if s[i] != s[j]:
                        break
                else:
                    break
            if len(s[i+1:j]) > maxlen:
                ress = s[i+1:j]
                maxlen = len(ress)
            i, j = k, k + 1
            while True:
                if i >= 0 and j < n:
                    if s[i] != s[j]:
                        break
                else:
                    break
                i, j = i - 1, j + 1
            if len(s[i+1:j]) > maxlen:
                ress = s[i+1:j]
                maxlen = len(ress)
        return ress



s = Solution()


class TestSolution(unittest.TestCase):
    def test_5(self):
        self.assertEqual(s.longestPalindrome("babad"),'bab')
        self.assertEqual(s.longestPalindrome("cbbd"),'bb')
        self.assertEqual(s.longestPalindrome("a"),'a')
        self.assertEqual(s.longestPalindrome("ac"),'a')


if __name__ == '__main__':
    #    s = Solution()
    unittest.main()
