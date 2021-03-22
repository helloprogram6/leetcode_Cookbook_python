# -*- coding:utf-8 -*-
# @FileName  :二叉搜索树.py
# @Time      :2021/3/18 9:57
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
    def verifyPostorder(self, postorder: List[int]) -> bool:
        """Offer 33. 二叉搜索树的后序遍历序列 递归 划分左右子树 寻找数组中第一个大于根节点的树就是右子树的第一个节点"""
        #print(postorder)
        n = len(postorder)
        if n <= 1:
            return True
        root = postorder[-1]
        i = 0
        while i < n -1:# 寻找右子树的第一个节点
            if postorder[i] > root:
                break
            i += 1
        t = i
        while i < n - 1:
            if postorder[i] < root:
                return False
            i += 1
        return self.verifyPostorder(postorder[t:n-1]) and self.verifyPostorder(postorder[:t-1])
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """ 235. 二叉搜索树的最近公共祖先 """
        #print(p.val,q.val)
        cur = root
        while cur:
            if cur.val > p.val and cur.val > q.val:#p,q在cur左边
                cur = cur.left
            elif cur.val < p.val and cur.val < q.val:#p,q在cur右边
                cur = cur.right
            elif cur.val == p.val:
                return p
            elif cur.val == q.val:
                return q
            else:
                return cur
        return cur


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3,TreeNode(5,TreeNode(6),TreeNode(2,TreeNode(7),TreeNode(4))),TreeNode(1,TreeNode(0),TreeNode(8)))
    print(s.lowestCommonAncestor(root,root.left.left,root.left.right.left).val)
    """ offer 33
    print(Solution().verifyPostorder([1,2,5,10,6,9,4,3]))#false
    print(Solution().verifyPostorder([5, 2, -17, -11, 25, 76, 62, 98, 92, 61]))#false
    print(Solution().verifyPostorder([1,3,2,6,5]))#true
    """

