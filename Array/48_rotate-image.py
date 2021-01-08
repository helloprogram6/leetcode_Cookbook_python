# -*- coding:utf-8 -*-
# @FileName  :48_rotate-image.py
# @Time      :2020/12/28 17:02
# @Author    :Haozr
from typing import List


# 解法1：两次翻转==旋转 顺时针旋转==左斜对角线翻+左右翻、上下翻+左斜对角线翻、右斜对角线翻+上下翻、左右翻+右斜对角线翻
#逆时针旋转==左斜对角线翻+上下翻、左右翻+左斜对角线翻、右斜对角线翻+左右翻、上下翻+右斜对角线翻
class Solution:
    def upToDown(self, matrix: List[List[int]]) -> None:
        """
        上下翻转
        """
        i = 0
        j = len(matrix)-1
        while i < j:
            matrix[i],matrix[j] = matrix[j],matrix[i]
            i += 1
            j -= 1
    def leftToRight(self, matrix: List[List[int]]) -> None:
        """
        左右翻转
        """
        for mat in matrix:
            i = 0
            j = len(mat) - 1
            while i < j:
                mat[i], mat[j] = mat[j], mat[i]
                i += 1
                j -= 1
    def leftSymmetry(self, matrix: List[List[int]]) -> None:
        """
        左斜对角线翻转
        """
        w = len(matrix)
        for i in range(w):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    def rightSymmetry(self, matrix: List[List[int]]) -> None:
        """
        右斜对角线翻转
       """
        w = len(matrix)
        for i in range(w)[::-1]:
            for j in range(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    def rotate(self, matrix: List[List[int]]) -> None:
        self.leftSymmetry(matrix)
        self.leftToRight(matrix)

#解法2：原地旋转 顺序交换4个值 交换的方向就是顺时针或者逆时针
# 4个位置：matrix[row][col]左上、matrix[col][n-row-1]右上、matrix[n-row-1][n-col-1]右下、matrix[n-col-1][row]左下
# 1)n = 偶数：枚举 n^2/4=(n/2)*(n/2) 个位置，即1/4的数
# 2)n = 奇数：枚举 (n^2−1)/4 =[(n-1)/2]*[(n+1)/2]个位置，即中心数字不动
class Solution2:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        rows = n//2
        cols = (n + 1)//2
        for row in range(rows):
            for col in range(cols):
                matrix[row][col], matrix[col][n-row-1], matrix[n-row-1][n-col-1], matrix[n-col-1][row]  \
                    = matrix[n-col-1][row], matrix[row][col], matrix[col][n-row-1], matrix[n-row-1][n-col-1]

if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(matrix)
    Solution2().rotate(matrix)
    print(matrix)
