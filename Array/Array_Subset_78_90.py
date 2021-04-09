# -*- coding:utf-8 -*-
# @FileName  :Array_Subset.py
# @Time      :2021/4/1 21:13
# @Author    :Haozr
from typing import List
import unittest
#数组子集，幂集相关题目

# 解法1：
class Solution:
    def subsetsWithDup78(self, nums: List[int]) -> List[List[int]]:
        """78. 子集 数组元素互不相同"""
        res = [[]]
        for i in nums:
            temp = []
            for j in res:
                temp.append(j + [i])
            res += temp
        return res

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """90. 子集 II 存在重复元素 看成 n叉树，去重只去同一层的相同元素，同一树分支的元素不去重。
        对于数组[2,2,3]比如第一层取2；3,2的下一层取2，3；3没有下一层"""
        nums.sort()
        res = []
        n = len(nums)
        def dfs(cur,path):
            res.append(path)
            for i in range(cur,n):#从当前元素往后探索
                if i > cur and nums[i] == nums[i-1]:#从第二个元素开始，遇到相同的元素就跳过
                    continue
                dfs(i+1, path+[nums[i]])
        dfs(0,[])
        return res

s = Solution()


class TestSolution(unittest.TestCase):
    def test_78(self):
        self.assertEqual(s.subsetsWithDup([1,2,3]),[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertEqual(s.subsetsWithDup([0,0]),[[],[0],[0,0]])

    def test_90(self):
        self.assertEqual(s.subsetsWithDup([1,2,2,3]),[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertEqual(s.subsetsWithDup([0,0]),[[],[0],[0,0]])

if __name__ == '__main__':
    #    s = Solution()
    unittest.main()
