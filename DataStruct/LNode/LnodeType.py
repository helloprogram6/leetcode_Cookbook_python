# -*- coding:utf-8 -*-
# @FileName  :LnodeType.py
# @Time      :2021/3/1 20:29
# @Author    :Haozr
# 定义链表类
from typing import List

class Node:
    """结点"""
    def __init__(self, x):
        self.item = x
        self.next = None


class SingleLinkList(object):
    """有头结点的单链表"""
    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        # 初始指针指向head
        cur = self._head
        count = 0
        # 指针指向None 表示到达尾部
        while cur is not None:
            count += 1
            # 指针下移
            cur = cur.next
        return count

    def items(self):
        """遍历链表"""
        # 获取head指针
        cur = self._head
        # 循环遍历
        while cur is not None:
            # 返回生成器
            #print(cur.item)
            yield cur.item
            # 指针下移
            cur = cur.next

    def add(self, item):
        """向链表头部添加元素"""
        node = Node(item)
        # 新结点指针指向原头部结点
        node.next = self._head
        # 头部结点指针修改为新结点
        self._head = node

    def append(self, item):
        """尾部添加元素"""
        node = Node(item)
        # 先判断是否为空链表
        if self.is_empty():
            # 空链表，_head 指向新结点
            self._head = node
        else:
            # 不是空链表，则找到尾部，将尾部next结点指向新结点
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, index, item):
        """指定位置插入元素"""
        # 指定位置在第一个元素之前，在头部插入
        if index <= 0:
            self.add(item)
        # 指定位置超过尾部，在尾部插入
        elif index > (self.length() - 1):
            self.append(item)
        else:
            # 创建元素结点
            node = Node(item)
            cur = self._head
            # 循环到需要插入的位置
            for i in range(index - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除值为item的节点"""
        cur = self._head
        pre = None
        while cur is not None:
            # 找到指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self._head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                return True
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next

    def find(self, item):
        """查找元素是否存在"""
        return item in self.items()

    def createLinkListFromList(self, nums: List):
        """根据列表正序创建有结点的单链表"""
        if len(nums) == 0:
            self._head = None
        self._head = Node(None)
        nexter = self._head
        for i in range(len(nums)):
            nexter.next = Node(nums[i])
            nexter = nexter.next

    def reverse(self):
        """原地翻转链表"""
        if self.is_empty():
            return
        pre, nex = None,None
        cur = self._head.next
        #从第一个结点开始翻转
        while cur is not None:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        self._head.next = pre

    def reverseHead(self):
        """头插法 翻转链表"""
        if self.is_empty():
            return
        nex = None
        cur = self._head.next
        # 把头结点断开，防止翻转后的尾结点（翻转前的起始）指向自己
        self._head.next = None
        while cur is not None:
            nex = cur.next
            cur.next = self._head.next
            self._head.next = cur
            cur = nex

    def removeDup(self):
        """从无序链表中移除重复项  双重循环/哈希表(空间换时间)"""
        if self.is_empty():
            return
        curi = self._head.next
        while curi is not None:
            curj = curi.next
            pre = curi
            while curj is not None:
                if curj.item == curi.item:#删除curj结点,pre不变
                    pre.next = curj.next
                else:
                    pre = curj
                curj = curj.next
            curi = curi.next

    def addNums(self, otherlist):
        """合并一个升序非空单链表到本链表"""
        if self.is_empty() or otherlist.is_empty():
            if self.is_empty():
                return otherlist
            else:
                return self._head
        cur1 = self._head.next
        pre = self._head
        cur2 = otherlist._head.next
        while cur1 is not None and cur2 is not None:
            if cur2.item < cur1.item:
                cur = cur2
                cur2 = cur2.next
                cur.next = cur1
                pre.next = cur
            pre = cur1
            cur1 = cur1.next
        if cur2 is not None:
            pre.next = cur2

if __name__ == '__main__':
    nums = [1,3,5,6,10]
    s = SingleLinkList()
    s1 = SingleLinkList()
    s1.createLinkListFromList([2,4,12])
    s.createLinkListFromList(nums)
    print([i for i in s.items()])
    s.addNums(s1)
    print([i for i in s.items()])
