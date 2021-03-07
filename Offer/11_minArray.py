# -*- coding:utf-8 -*-
# @FileName  :11_minArray.py
# @Time      :2021/3/4 19:10
# @Author    :Haozr
from typing import List


# 解法1：
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        low = 0
        high = len(numbers) - 1

        while low < high:
            pivot = low + (high - low) // 2
            if numbers[high] > numbers[pivot]:
                high = pivot
            elif numbers[high] < numbers[pivot]:
                low = pivot + 1
            else:
                high -= 1
        return numbers[low]

if __name__ == '__main__':
    print(Solution().minArray([3,4,5,1,2]))
