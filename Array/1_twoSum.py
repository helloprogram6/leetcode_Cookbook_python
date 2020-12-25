from typing import List
#解法1:暴力解----O(n^2)
# 两次循环
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]

#解法2：哈希表----O(n)
#如果 target - x 不在哈希表中，那么就把x放进哈希表中；
#如果 target - x 在哈希表中，就返回x和target-x的下标。
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            otherNum = target - num
            if otherNum in map:
                return [map[otherNum], i]
            else:
                map[num] = i
        return []
#最优解：顺序扫描数组，对每一个元素，在 map 中找能组合给定值的另一半数字，如果找到了，直接返回 2 个数字的下标即可。
#      如果找不到，就把这个数字存入 map 中，等待扫到“另一半”数字的时候，再取出来返回结果。
if __name__ == "__main__":
    nums = [2,7,7,15]
    target = 14
    s1 = Solution2().twoSum(nums,target)
    print(s1)