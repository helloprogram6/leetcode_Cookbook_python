# -*- coding:utf-8 -*-
# @FileName  :二叉树.py
# @Time      :2021/3/19 16:21
# @Author    :Haozr
from typing import List
class TreeNode:
    """二叉树结构"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 解法1：
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """ 236. 二叉树的最近公共祖先 递归 该函数的功能：判断root这颗树是否包含p或者q"""
        if not root or root == p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left,p,q)
        r = self.lowestCommonAncestor(root.right,p,q)
        if not l :return r
        if not r :return l
        return root

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        """ 1379. 找出克隆二叉树中的相同节点 后序的非递归遍历 寻找root到target的路径 可以写题解"""
        stack = []
        r = None  # 标记左子树是否遍历
        p = original
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack[-1]
                if p.right and p.right != r:  # 有右子树，并且没有遍历
                    p = p.right
                else:
                    if p == target:#找到target结点，stack中存放了所有路径
                        print([i.val for i in stack], p.val)
                        break
                    r = stack.pop()
                    # print([i.val for i in stack], r.val)
                    p = None
        if p == target:
            print(p.val)
            r = cloned
            cur = original
            p = 0
            while cur != target:
                print(cur.val,stack[p].val)
                p += 1
                if cur.right == stack[p]:
                    cur = cur.right
                    r = r.right
                else:
                    cur = cur.left
                    r = r.left
            print(r.val)
            return r
        return cloned

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        """112 路径总和 后序非递归遍历"""
        sum = 0
        r = None
        p = root
        stack = []
        while p or stack:
            if p:
                stack.append(p)
                sum += p.val
                p = p.left
            else:
                p = stack[-1]
                if p.right and p.right != r:#存在右子树，且没有遍历
                    p = p.right
                else:
                    r = stack.pop()
                    print(r.val,sum)
                    if not r.right and not r.left and sum == targetSum:
                        return True
                    sum -= r.val
                    p = None
        return False

    def pathSum_113(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        """113. 路径总和 II """
        sum = 0
        res = []
        r = None
        p = root
        stack = []
        while p or stack:
            if p:
                stack.append(p)
                sum += p.val
                p = p.left
            else:
                p = stack[-1]
                if p.right and p.right != r:  # 存在右子树，且没有遍历
                    p = p.right
                else:
                    print(p.val, sum)
                    if not p.right and not p.left and sum == targetSum:
                        res.append([i.val for i in stack])
                    r = stack.pop()
                    sum -= r.val
                    p = None
        return res

    def pathSum(self, root: TreeNode, sum: int) -> int:
        """ 437. 路径总和 III """
        tsum = 0
        preSums = [0]
        res = 0
        r = None
        p = root
        stack = []
        while p or stack:
            if p:
                stack.append(p)
                tsum += p.val
                preSums.append(tsum)
                p = p.left
            else:
                p = stack[-1]
                if p.right and p.right != r:  # 存在右子树，且没有遍历
                    p = p.right
                else:
                    print(p.val, tsum, preSums)
                    preSums.pop()
                    for s in preSums:
                        if tsum - s == sum:
                            res += 1
                    r = stack.pop()
                    tsum -= r.val
                    p = None
        return res

    def invertTree(self, root: TreeNode) -> TreeNode:
        """226. 翻转二叉树 """
        if root:
            root.left,root.right = self.invertTree(root.right),self.invertTree(root.left)
        return root

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(0, TreeNode(0),TreeNode(0, TreeNode(0), TreeNode(0)))
    root1 = TreeNode(1, TreeNode(2, TreeNode(1),TreeNode(3)),
                     TreeNode(7, TreeNode(6), TreeNode(9)))
    print(s.invertTree(root1))
    """1379
    root1 = TreeNode(1,TreeNode(2,TreeNode(4,TreeNode(8),TreeNode(9))),TreeNode(3,TreeNode(6),TreeNode(7)))
    root2 = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9))), TreeNode(3, TreeNode(6), TreeNode(7)))
    print(s.getTargetCopy(root1,root2,root1.right.left).val)
    """

    """236
    root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
                    TreeNode(1, TreeNode(0), TreeNode(8)))
    print(s.lowestCommonAncestor(root, root.left.left, root.left.right.left).val) 5 
    """
    """437 特殊测试用例
    [0,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0,null,0]
    0
    输出为：500500
    print(s.pathSum(root,0))
    """

