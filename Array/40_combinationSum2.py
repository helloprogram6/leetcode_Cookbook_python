# -*- coding:utf-8 -*-
# @FileName  :40_combinationSum2.py
# @Time      :2020/12/27 21:52
# @Author    :Haozr
from typing import List
'''回溯法模板
res = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        res.append(路径)
        return

    if 满足剪枝条件：
        return
        return

    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
'''


# 解法1：题目要求出总和为 sum 的所有组合，组合需要去重。
# 这一题是第 39 题的加强版，第 39 题中元素可以重复利用(重复元素可无限次使用).
# 这一题中元素只能有限次数的利用，因为存在重复元素，并且每个元素只能用一次(重复元素只能使用有限次)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        length = len(candidates)
        result = []
        def dfs(tar, combine, idx):#此处模仿39题的思路行不同，因为每次循环添加的数需要判断是否可以选择
            if idx >= length or tar < 0:
                return
            if tar == 0:
                result.append(combine)
                return
            if idx > 0 and candidates[idx] == candidates[idx - 1]:
                return
            if tar >= candidates[idx]:
                dfs(tar - candidates[idx], combine+[candidates[idx]], idx+1)
                dfs(tar, combine, idx + 1)
        dfs(target, [], 0)
        return result
#解法2：每次添加数字i时，只添加一次，
    def combinationSum22(self, candidates: List[int], target: int) -> List[List[int]]:
        length = len(candidates)
        candidates.sort()
        res = []
        def findcombinationSum(tar: int, index: int, c: List[int]):
            if tar < 0:
                return
            if tar == 0:
                res.append(c)
                return
            for i in range(index, length):
                if i>index and candidates[i] == candidates[i-1]:#只添加第一个重复的数
                    continue
                if candidates[i] <= tar:
                    findcombinationSum(tar-candidates[i], i+1, c+[candidates[i]])
        findcombinationSum(target,0,[])
        return res

if __name__ == '__main__':
    candidates = [10,1,2,7,6,1,6,5]
    target = 8
    candidates1 = [1,3,1,1,1,2,2,2]
    target1 = 3
    print(Solution().combinationSum2(candidates1,target1))
