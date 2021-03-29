# -*- coding:utf-8 -*-
# @FileName  :07_buildTree.py
# @Time      :2021/3/2 21:28
# @Author    :Haozr
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 解法1：
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        pass

    def maxDepth(self, root: TreeNode) -> int:
        """递归迭代"""
        def depth(root: TreeNode):
            if root == None:
                return 0
            if root.left == None and root.right == None:
                return 1
            return max(depth(root.left),depth(root.right))+1
        return depth(root)
    def maxDepth1(self,root:TreeNode) -> int:
        """利用广度深度遍历"""
        stack= []
        if root == None:
            return 0
        stack.append(root)
        height = 0
        while stack:
            size = len(stack)
            height += 1
            while size:
                size -= 1
                s = stack.pop(0)
                if s.left:
                    stack.append(s.left)
                if s.right:
                    stack.append(s.right)
        return height


if __name__ == '__main__':
    root = TreeNode(3)
    root.right=TreeNode(9)
    root.left = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(7)
    print(Solution().maxDepth1(root))
