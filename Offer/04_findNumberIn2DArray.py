# -*- coding:utf-8 -*-
# @FileName  :04_findNumberIn2DArray.py
# @Time      :2021/2/28 20:49
# @Author    :Haozr
from typing import List


# 解法1：暴力
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False
# 解法2：线性查找
class Solution2:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        i, j = 0,len(matrix[0])-1
        while -1 < i < len(matrix) and -1 < j < len(matrix[0]):
            if matrix[i][j] == target:
                print(i,j)
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False
if __name__ == '__main__':
    matrix = [[1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]]
    print(Solution2().findNumberIn2DArray(matrix, 20))