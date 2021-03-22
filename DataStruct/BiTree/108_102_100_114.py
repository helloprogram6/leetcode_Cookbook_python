# -*- coding:utf-8 -*-
# @FileName  :108_102_100_114.py
# @Time      :2021/3/17 18:24
# @Author    :Haozr
from typing import List
class TreeNode:
    """二叉树结构"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """ 108 升序的整数数组nums 转换为一棵 高度平衡 二叉搜索树 【递归创建】"""
        n = len(nums)
        if n == 0:
            return None
        elif n == 1:
            return TreeNode(nums[0])
        elif n == 2:
            return TreeNode(nums[1],TreeNode(nums[0]))
        elif n == 3:
            return TreeNode(nums[1],TreeNode(nums[0]),TreeNode(nums[2]))
        else:
            mid = n // 2
            return TreeNode(nums[mid],self.sortedArrayToBST(nums[0:mid]),self.sortedArrayToBST(nums[mid+1:n]))

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """102 二叉树的层序遍历 用队列"""
        queue1 = []
        queue2 = []
        res = []
        if root:
            queue1.append(root)
        while queue1:
            temp = []
            while queue1:
                t = queue1.pop(0)
                temp.append(t.val)
                if t.left:
                    queue2.append(t.left)
                if t.right:
                    queue2.append(t.right)
            res.append(temp)
            queue1 = queue2
            queue2 = []
        return res

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """100. 相同的树 递归"""
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False

    def flatten2(self, root: TreeNode) -> None:
        """114 二叉树展开为链表 非递归的先序遍历 用栈 O(n) O(n)"""
        stack = []
        if not root:
            return None
        t = root
        l = []
        while stack or t:
            while t:#往左走到底
                stack.append(t)
                l.append(t)
                t = t.left
            if stack:
                t = stack.pop().right
        i = 0
        while i < len(l)-1:
            l[i].left = None
            l[i].right = l[i+1]
            i += 1
        l[i].right = None
        l[i].left = None
        t = root #测试
        print("root",[i.val for i in l])
        t = root #测试
        print("root",t.val)
        while t:
            if t.right:
                print(t.val, t.right.val)
            t = t.right

    def flatten(self, root: TreeNode) -> None:
        """114 二叉树展开为链表 第二种解法 O(n) O(1)
        对于cur节点,其左节点cur.left不为空，则左子树的最右节点的后继为cur.right。
        其左节点为空，则cur处理下一个节点
        """
        cur = root
        while cur:
            if cur.left:
                nex = cur.left#指向cur的左子树
                pre = nex
                while pre.right:#寻找左子树的最右节点
                    pre = pre.right
                pre.right = cur.right
                cur.left = None#处理cur的左右值
                cur.right = nex
                cur = nex
            else:
                cur = cur.right
        t = root  # 测试
        print("root", t.val)
        while t:
            if t.right:
                print(t.val, t.right.val)
            t = t.right

    def late(self,root:TreeNode)->None:
        """ 二叉树的后序遍历 非递归实现"""
        stack = []
        r = None  # 标记左子树是否遍历
        p = root
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack[-1]
                if p.right and p.right != r:  # 有右子树，并且没有遍历
                    p = p.right
                else:
                    r = stack.pop()
                    print([i.val for i in stack], r.val)
                    p = None
if __name__ == '__main__':
    Solution().flatten(TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(5,None,TreeNode(6))))
    Solution().flatten(TreeNode(1,TreeNode(2,TreeNode(3))))
    Solution().flatten(TreeNode(1,None,TreeNode(2,None,TreeNode(3))))
    Solution().flatten(TreeNode(1,TreeNode(2,TreeNode(3,TreeNode(5)),TreeNode(4))))
"""
    108
    #t = Solution().sortedArrayToBST([-10,-3,0,5,9])
    
    102
    #print(Solution().levelOrder(TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))))
    
    100
    print(Solution().isSameTree(TreeNode(1,TreeNode(2),TreeNode(3)),TreeNode(1,TreeNode(2),TreeNode(3))))
    print(Solution().isSameTree(TreeNode(1,TreeNode(2)),TreeNode(1,None,TreeNode(2))))
"""