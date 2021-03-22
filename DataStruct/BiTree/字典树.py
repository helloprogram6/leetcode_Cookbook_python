# -*- coding:utf-8 -*-
# @FileName  :字典树.py
# @Time      :2021/3/20 13:37
# @Author    :Haozr
from typing import List
class TrieNode:
    def __init__(self, val=''):
        self.val = val
        self.child = {}
        self.isWord = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        t = self.root
        for w in word:
            if w not in t.child:
                t.child[w] = TrieNode(w)
            t = t.child[w]
        t.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        t = self.root
        for w in word:
            if w not in t.child:
                return False
            t = t.child[w]
        if t.isWord:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for w in prefix:
            if w not in cur.child:
                return False
            cur = cur.child[w]
        return True


if __name__ == '__main__':
    s = Trie()
    print(s.insert("Trie"))
    print(s.startsWith("a"))
