# -*- coding:utf-8 -*-
# @FileName  :146_LRU.py
# @Time      :2021/3/16 21:26
# @Author    :Haozr
from typing import List

class ListNode:
    """双链表"""
    def __init__(self,key=-1,val=-1):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cacheSize = capacity
        self.page = {}
        self.head = ListNode(0)
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key in self.page:#刚访问的key放在头指针后面
            now = self.page[key]
            if now == self.head.next:
                return now.val
            now.pre.next = now.next#删除now
            now.next.pre = now.pre
            self.head.next.pre = now#添加到头结点
            now.next = self.head.next
            now.pre = self.head
            self.head.next = now
            return now.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.page:#刚访问的key放在头指针后面
            now = self.page[key]
            if now.val != value:
                now.val = value
            if now == self.head.next:
                return
            now.pre.next = now.next
            now.next.pre = now.pre
            self.head.next.pre = now
            now.next = self.head.next
            now.pre = self.head
            self.head.next = now
        else:
            if self.head.key ==  self.cacheSize:#缓存已满，删出尾结点
                self.page.pop(self.tail.pre.key)
                self.tail.pre.pre.next = self.tail
                self.tail.pre = self.tail.pre.pre

            now = ListNode(key,value)#刚添加的key放在头指针后面
            self.head.next.pre = now
            now.next = self.head.next
            now.pre = self.head
            self.head.next = now

            self.page[key] = now
            if self.head.key != self.cacheSize:
                self.head.key += 1

if __name__ == '__main__':
    # lRUCache = LRUCache(2)
    # lRUCache.put(1, 1)
    # lRUCache.put(2, 2)
    # print(lRUCache.get(1))
    # lRUCache.put(3, 3)
    # print(lRUCache.get(2))
    # lRUCache.put(4, 4)
    # print(lRUCache.get(1))
    # print(lRUCache.get(3))
    # print(lRUCache.get(4))

    lRUCache = LRUCache(2)
    print("next ")
    lRUCache.put(2, 1)
    lRUCache.put(1, 1)
    lRUCache.put(2, 3)
    lRUCache.put(4, 1)
    print(lRUCache.get(1))
    print(lRUCache.get(2))

