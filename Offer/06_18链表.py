# -*- coding:utf-8 -*-
# @FileName  :05_replaceSpace.py
# @Time      :2021/2/28 21:12
# @Author    :Haozr
from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 解法1：
class Solution:
    def createLink(self, nums: List) -> ListNode:
        """创建有头结点的链表"""
        global header, nexter
        if len(nums) == 0:
            return ListNode(None)
        for i in range(len(nums)):
            if i == 0:
                header = ListNode(nums[i])
                nexter = header
            else:
                nexter.next = ListNode(nums[i])
                nexter = nexter.next
        return header
    # 用栈
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head != None:
            stack.append(head.val)
            head = head.next
        return stack[::-1]

    # 递归
    def reversePrint1(self, head: ListNode) -> List[int]:
        """06 从尾到头打印链表"""
        if head == None:
            return []
        return self.reversePrint(head.next) + [head.val]

    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        """删除无头结点链表的节点"""
        if head.val == val:
            head = head.next
            return head
        nex = head.next
        pre = head
        while nex != None:
            if nex.val == val:
                pre.next = nex.next
            pre = nex
            nex = nex.next
        return head


if __name__ == '__main__':
    s = Solution()
    nums = [[-3,5,-99]]
    head = s.createLink(nums)
    print(s.deleteNode(head,-3))
