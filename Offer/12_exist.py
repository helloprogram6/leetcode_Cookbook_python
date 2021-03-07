# -*- coding:utf-8 -*-
# @FileName  :12_exist.py
# @Time      :2021/3/4 20:34
# @Author    :Haozr
from typing import List


# 解法1：
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        def dfs(i, j, s):
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != word[s]:
                """行或列索引越界 或 当前矩阵元素与目标字符不同(已经访问过)"""
                return False
            if s + 1 == len(word):
                return True
            board[i][j] = '' #走过的字符置空
            res = dfs(i+1,j,s+1) or dfs(i,j+1,s+1) or dfs(i-1,j,s+1) or dfs(i,j-1,s+1)
            board[i][j] = word[s]#恢复原本的路径
            return res

        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False

if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(Solution().exist(board, word))
