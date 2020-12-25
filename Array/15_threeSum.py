import bisect
from collections import defaultdict
from typing import List
#解法1：暴力解,三次循环

#解法2：排序 + 双指针 难点：结果不重复
#「不重复」的本质是：第二重循环枚举到的元素不小于当前第一重循环枚举到的元素；第三重循环枚举到的元素不小于当前第二重循环枚举到的元素。
# 即：枚举的三元组(a,b,c)满足a≤b≤c。 同时，每层循环枚举的元素不能相同，否则会有重复。
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length<3:
            return []
        nums.sort()
        sumList = []
        for i in range(length):
            if nums[i] > 0:
                return sumList
            if i > 0 and nums[i] == nums[i-1]: #第一层循环的数不重复
                continue
            header = i + 1
            tailer = length - 1
            while header < tailer:
                sum = nums[i] + nums[header] + nums[tailer]
                if sum == 0:
                    sumList.append([nums[i], nums[header], nums[tailer]])
                    while header < tailer and nums[header] == nums[header + 1]:#第二三层循环的数不重复
                        header += 1
                    while header < tailer and nums[tailer] == nums[tailer - 1]:
                        tailer -= 1
                    header += 1
                    tailer -= 1
                elif sum < 0:
                    header += 1
                else:
                    tailer -= 1
        return sumList

if __name__ == "__main__":
    s = Solution()
    height = [-1, 0, 0, 0, 1, 1, 1, 2, -1, -1, -1, -2]
    height1 = [0, 0, 0]
    print(s.threeSum(height))