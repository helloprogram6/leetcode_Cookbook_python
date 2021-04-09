# -*- coding:utf-8 -*-
# @FileName  :Array_search.py
# @Time      :2021/4/6 15:18
# @Author    :Haozr
from typing import List
import unittest


# 解法1：
class Solution:
    def searchMatrix74(self, matrix: List[List[int]], target: int) -> bool:
        """74. 搜索二维矩阵 行升序，每行的第一个整数大于前一行的最后一个整数 映射为一个升序数组，一次二分查找"""
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m * n - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid//n][mid%n] > target:
                high = mid - 1
            elif matrix[mid//n][mid%n] < target:
                low = mid + 1
            else:
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """240. 搜索二维矩阵 II 行升序，列升序 从左下角开始遍历"""
        m = len(matrix)
        n = len(matrix[0])
        row, col = m - 1, 0
        while row >= 0 and col < n:
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                col += 1
            else:
                row -= 1
        return False

    def search(self, nums: List[int], target: int) -> bool:
        """81. 搜索旋转排序数组 II """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target or nums[low] == target or nums[high] == target:
                return True
            if nums[mid] < nums[high]:
                if nums[high] > target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            elif nums[low] < nums[mid]:
                if nums[low] < target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                low += 1
                high -= 1
        return False

s = Solution()


class TestSolution(unittest.TestCase):
    def test_74(self):
        self.assertEqual(s.searchMatrix74([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3),True)
        self.assertEqual(s.searchMatrix74([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13),False)

    def test_240(self):
        self.assertEqual(s.searchMatrix([[1, 4, 7, 11,15],
                                         [2, 5, 8, 12,19],
                                         [3, 6, 9, 16,22],
                                         [10,13,14,17,24],
                                         [18,21,23,26,30]],5),True)
        self.assertEqual(s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],20),False)

    def test_81(self):
        #self.assertEqual(s.search([2,5,6,0,0,1,2],0),True)
        self.assertEqual(s.search([1,0,1,1,1],0),True)
        self.assertEqual(s.search([2,5,0,2],0),True)
        self.assertEqual(s.search([2,5,6,0,0,1,2],3),False)


if __name__ == '__main__':
    #    s = Solution()
    unittest.main()
