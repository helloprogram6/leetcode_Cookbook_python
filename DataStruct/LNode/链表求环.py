# -*- coding:utf-8 -*-
# @FileName  :链表求环.py
# @Time      :2021/3/15 9:53
# @Author    :Haozr
from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def viewListNode(head:ListNode):
    l = []
    while head:
        l.append(head.val)
        head = head.next
    print(l)
def reverse(head,tail):
    """返回翻转后链表的新头与尾"""
    cur = head
    nex = None
    pre = tail.next#注意尾节点的处理
    while cur != tail:
        nex = cur.next
        cur.next = pre
        pre = cur
        cur = nex
    cur.next = pre
    tail = head
    head = cur
    return head,tail
# 解法1：
class Solution:
    def detectCycle(self, head: ListNode) -> bool:
        """141. 环形链表 检测链表是否有环 双指针"""
        fast = head
        low = head
        while fast and fast.next:
            fast = fast.next.next
            low = low.next
            if fast == low:
                return True
        return False

    def detectCycle2(self, head: ListNode) -> ListNode:
        """ 142 环形链表 II 返回链表开始入环的第一个节点"""
        fast = head
        slow = head
        while fast and fast.next:#寻找相遇点
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if fast and fast.next:#找到相遇点
            ptr = head
            while fast!=ptr:#相遇点与新点在环入口节点相遇
                ptr = ptr.next
                fast = fast.next
            return ptr
        return None

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """25. K 个一组翻转链表"""
        if k == 1:
            return head
        nextlist = head
        end = head
        pre = None
        while end:
            begin = nextlist
            end = begin
            i = 1
            while end and i < k:#寻找长度为k子链表
                end = end.next
                i += 1
            if end:#找到k子链表
                nextlist = end.next
                begin, end = reverse(begin,end)
                if pre:
                    pre.next = begin
                else:
                    head = begin
                pre = end
        return head

if __name__ == '__main__':
    listNode = ListNode(1)
    listNode.next = ListNode(2)
    #listNode.next.next = ListNode(3)
    #listNode.next.next.next = ListNode(4)
    #listNode.next.next.next.next = ListNode(5)
    h = Solution().reverseKGroup(listNode,4)
    viewListNode(h)
