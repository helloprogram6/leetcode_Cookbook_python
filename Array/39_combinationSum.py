# -*- coding:utf-8 -*-
# @FileName  :39_combinationSum.py
# @Time      :2020/12/26 21:48
# @Author    :Haozr
from typing import List


# 解法1：搜索回溯法，
# dfs函数的作用是：寻找所有和为target的数组列表；终止条件是 tar == 第idx个数或者idx超出界限；
# 分两个方向搜索：1）tar不变,idx+1
# 2)tar变为tar-candidates[idx],idx不变。即candidates[idx]是结果的一部分，看剩下的那部分是否可以在数组中找到，找不到就要移除candidates[idx]

#注：把dfs看作是一个已经实现了功能的函数
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        length = len(candidates)
        def dfs(tar, temp, idx):
            if idx >= length:
                return
            if tar == candidates[idx]:
                result.append(temp+[candidates[idx]])
                return
            if tar > candidates[idx]:
                dfs(tar - candidates[idx], temp+[candidates[idx]], idx)
                dfs(tar, temp, idx+1)
        dfs(target, [], 0)
        return result
#相当于上面的解法，用for循环代替了一个内部的函数调用
    def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
        length = len(candidates)
        if length == 0:
            return []
        candidates.sort()
        res = []
        def findcombinationSum(tar: int, index: int, c: List[int]):
            if tar < 0:#满足结束条件
                return
            if tar == 0:#满足结束条件
                res.append(c)
                return
            for i in range(index, length):
                if candidates[i] > tar:#满足剪枝条件
                    break
                findcombinationSum(tar-candidates[i], i, c+[candidates[i]])
        findcombinationSum(target,0,[])
        return res
if __name__ == '__main__':
    candidates = [2,3,5]
    target = 8
    print(Solution().combinationSum1(candidates, target))
