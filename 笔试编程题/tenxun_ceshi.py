# -*- coding:utf-8 -*-
# @FileName  :tenxun_ceshi-1.py
# @Time      :2021/4/4 19:41
# @Author    :Haozr

import unittest

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 解法1：
class Solution:
    def solve(self , root ):
        queue = []
        tempqueue = []#存放进队列
        if root != None:
            tempqueue.append(root)
        else:
            return root
        while tempqueue:
            queue = tempqueue
            tempqueue = []
            while queue:
                t = queue[0]
                if t.left == None or t.right == None:
                    break
                queue.pop(0)
                tempqueue.append(t.left)
                tempqueue.append(t.right)
            if queue:
                break
        for p in queue:
            p.left = None
            p.right = None
        return root
    #def solve1(self , root ):

s = Solution()


class TestSolution(unittest.TestCase):
    def test_(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        root.left.left.left = TreeNode(8)
        t = s.solve(root)
        print("done")
        #self.assertEqual(s.)


if __name__ == '__main__':
    #    s = Solution()
    unittest.main()
