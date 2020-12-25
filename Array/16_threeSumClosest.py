# -*- coding:utf-8 -*-
# @FileName  :16_threeSumClosest.py
# @Time      :2020/12/21 20:38
# @Author    :Haozr
from typing import List


# 解法1：
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min = 10**3
        sum = target
        print(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            L = i + 1
            R = len(nums) - 1
            while L < R:
                tempSum = nums[L] + nums[R] + nums[i]
                print(nums[i],nums[L],nums[R],tempSum,abs(target - tempSum))
                if target == tempSum:
                    return target
                elif tempSum - target < 0:
                    while L < R and nums[L] == nums[L + 1]:#在循环去重后，再向前走一步
                        L += 1
                    L += 1
                else:
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1
                    R -= 1
                if abs(target - tempSum) < min:
                    min = abs(target - tempSum)
                    sum = tempSum
        return sum

if __name__ == '__main__':
    sums = [-1, -1, -1, 2, 1, 1, 1, 0, 0, 0,-4]
    sums1 = [1, 1, 1, 0]
    sums2 =[-1,0,1,1,55]
    s = Solution().threeSumClosest(sums2,3)
    print(s)