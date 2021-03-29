# -*- coding:utf-8 -*-
# @FileName  :05_replaceSpace.py
# @Time      :2021/2/28 21:12
# @Author    :Haozr
from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
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

    def reversePrint(self, head: ListNode) -> List[int]:
        """06 从尾到头打印链表(用栈)"""
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
        """18 删除无头结点链表的节点"""
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

    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        """22 返回链表中倒数第k个节点 即是求正数第n-k+1个结点"""
        if head == None or k == 0:
            return None
        ne = head
        n = 0
        while ne: #求链表长度 n
            n += 1
            ne = ne.next
        if k > n:
            return None
        k = n - k + 1
        ne = head
        while k > 1:
            k -= 1
            ne = ne.next
        return ne
    def getKthFromEnd1(self, head: ListNode, k: int) -> ListNode:
        """22 返回链表中倒数第k个节点 双指针"""
        if head == None or k == 0:
            return None
        ne = head
        while k: #ne 先移动k
            k -= 1
            if ne == None:
                return None
            ne = ne.next
        later = head
        while ne:
            later = later.next
            ne = ne.next
        return later

    def reverseList(self, head: ListNode) -> ListNode:
        """24 反转链表 原地翻转"""
        nex = head
        later = None
        pre = None
        while nex:
            later = nex.next
            nex.next = pre
            pre = nex
            nex = later
        return pre

    def viewList(self,head:ListNode):
        """以列表的方式打印链表"""
        s = []
        while head:
            s.append(head.val)
            head = head.next
        print(s)

    def copyRandomList(self, head: Node) -> Node:
        """35. 复杂链表的复制 """
        if head == None:
            return None
        ne = head
        while ne:#扩展链表为 A-A-B-B-C-C
            newNode = Node(ne.val,None,None)
            newNode.next = ne.next
            ne.next = newNode
            ne = ne.next.next
        ne = head
        while ne:#置新链的rodom
            ne.next.random = ne.random.next if ne.random != None else None
            ne = ne.next.next
        ne = head
        new = head.next
        newHead = head.next
        while new.next:#置新链的next
            ne.next = new.next
            ne = ne.next
            new.next = ne.next
            new = new.next
        new.next = None#处理尾结点
        ne.next = None
        return newHead
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """52. 两个链表的|第一个公共节点 双指针 一共走 a+b+r"""
        if headA == None or headB == None:
            return None
        a,b = headA,headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
        """52. 两个链表的|第一个公共节点 """
        if headA == None or headB == None:
            return None
        a,b = headA,headB
        an = 0
        while a:
            an += 1
            a = a.next
        bn = 0
        while b:
            bn += 1
            b = b.next
        a, b = headA, headB
        if an > bn:
            t = an - bn
            while t > 0:
                t -= 1
                a = a.next
        else:
            t = bn - an
            while t > 0:
                t -= 1
                b = b.next
        while a != b:
            a = a.next
            b = b.next
        return a


if __name__ == '__main__':
    s = Solution()
    """35. 复杂链表的复制 
    head = Node(7,Node(13,Node(11,Node(10))))
    head.next.random = head
    head.next.next.random = head.next.next.next
    new = s.copyRandomList(head)
    print(new)
    """
    a = s.createLink([1,2,3,4,5])
    b = ListNode(2)
    b.next = a
    s.viewList(a)
    s.viewList(b)
    t =s.getIntersectionNode(a,b)
    s.viewList(t)
    #print(s.deleteNode(head,-3))
    #print(s.getKthFromEnd1(head,0).val)
