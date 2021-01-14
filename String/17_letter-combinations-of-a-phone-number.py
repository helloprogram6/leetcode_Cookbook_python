# -*- coding:utf-8 -*-
# @FileName  :17_letter-combinations-of-a-phone-number.py
# @Time      :2021/1/14 20:47
# @Author    :Haozr
from typing import List
'''回溯法模板
回溯算法有三个要点：
1. 选择
    决定了你每个节点有哪些分支，帮助你构建出解的空间树。
2. 约束条件
    用来剪枝，剪去不满足约束条件的子树，避免无效的搜索。
3. 目标
    决定了何时捕获解，或者剪去得不到解的子树，提前回溯。
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
# 解法1：回溯（其实就是走路）
# index代表当前路径（走到哪里了），temp代表已经走过的路径（走过哪些路）
# findComb函数代表走index这条路
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dicts = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],
                 '5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],
                 '8':['t','u','v'],'9':['w','x','y','z']}
        if len(digits) == 0:
            return []
        result = []
        def findComb(index, temp):
            if len(digits) == index:#走到底了
                result.append(temp)
            else:
                for s in dicts[digits[index]]:#走哪些路
                    findComb(index+1, temp+s)
        findComb(0,'')
        return result
# 解法二 ：BFS 利用一个队列，按层遍历树的思想

if __name__ == '__main__':
    digits ='23'
    digits1 = ""
    print(Solution().letterCombinations(digits1))
