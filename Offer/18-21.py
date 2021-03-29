# -*- coding:utf-8 -*-
# @FileName  :18-21.py
# @Time      :2021/3/8 9:41
# @Author    :Haozr
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """剑指 Offer 19. 正则表达式匹配"""
        m,n = len(s),len(p)
        f = [[False] * (n+1) for _ in range(m+1)] # (m+1)*(n+1)矩阵，j[i]j]是p[:j]与s[:i]是否匹配
        def match(ns,np):# 是否匹配
            return p[np-1] == '.' or s[ns-1] == p[np-1]
        f[0][0] = True
        # 初始化首行
        for j in range(2, n+1, 2):
            f[0][j] = f[0][j - 2] and p[j - 1] == '*'
        for i in range(1,m + 1):
            for j in range(1,n+1):
                if p[j-1] == '*':#或运算：只要有一种情况可以匹配就是真
                    f[i][j] |= f[i][j - 2]
                    if match(i,j-1):#
                        f[i][j] |= f[i-1][j]
                else:
                    if match(i,j):
                        f[i][j] |= f[i-1][j-1]
        return f[m][n]
            


if __name__ == '__main__':
    #print(Solution().isMatch("aaa", "ab*a*c*a"))#"aaa", "ab*a*c*a" true
    #print(Solution().isMatch("aa", "a*"))#"aa", "a*" true
    print(Solution().climbStairs(2))
