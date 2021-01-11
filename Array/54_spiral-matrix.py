# -*- coding:utf-8 -*-
# @FileName  :54_spiral-matrix.py
# @Time      :2021/1/9 11:32
# @Author    :Haozr
from typing import List


# 解法1：按层模拟 每层的左上角位于 (top,left),右下角位于 (bottom,right) 下层是（top+1,left+1）、（bottom-1,right-1）
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        b = len(matrix) - 1
        r = len(matrix[0]) - 1
        l, t= 0,0
        order = []
        while l<=r and t<=b:
            for i in range(l,r+1):
                order.append(matrix[t][i])
            for i in range(t+1,b+1):
                order.append(matrix[i][r])
            if l<r and t<b:
                for i in range(r - 1,l,-1):
                    order.append(matrix[b][i])
                for i in range(b,t,-1):
                    order.append(matrix[i][l])
            l,t,r,b = l+1,t+1,r-1,b-1
        return order

if __name__ == '__main__':
    matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ]
]
    print(Solution().spiralOrder(matrix))
