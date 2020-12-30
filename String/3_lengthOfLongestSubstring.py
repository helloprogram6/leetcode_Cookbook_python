# -*- coding:utf-8 -*-
# @FileName  :3_lengthOfLongestSubstring.py
# @Time      :2020/12/30 10:18
# @Author    :Haozr
from typing import List


# 解法1：滑动窗口 hashmap存放字串中的所有字符的位置
# -->在缩小左边界时，左边界应该移动到重复字符的下一个位置,移动过程中应删除hashmap中对应的键值对
# 滑动窗口的右边界不断的右移，只要没有重复的字符，就持续向右扩大窗口边界。
# 一旦出现了重复字符，就需要缩小左边界，直到重复的字符移出了左边界，然后继续移动滑动窗口的右边界。
# 以此类推，每次移动需要计算当前长度，并判断是否需要更新最大长度，最终最大的值就是题目中的所求。
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        L = R = maxlen = 0
        while R < len(s):#扩大右字符
            if s[R] not in map:
                map[s[R]] = R
            else:
                tempL = map[s[R]] + 1#缩小左边界，使用了hash记录重复字符的位置
                while(map and L < tempL):
                    del map[s[L]]
                    L += 1
                map[s[R]] = R
            if R - L + 1 > maxlen:
                maxlen = R - L + 1
            print(maxlen, L, R, s[L:R+1])
            R += 1
        return maxlen
    #使用set集合，记录字符是否重复
    def lengthOfLongestSubstring1(self, s: str) -> int:
        map = set()
        L = R = maxlen = 0
        length = len(s)
        while L < length:
            if R < length and s[R] not in map:
                map.add(s[R])
                if R - L + 1 > maxlen:
                    maxlen = R - L + 1
                print(maxlen, L, R, s[L:R + 1])
                R += 1
            else:
                # 右侧字符重复，左字符右移缩小，直到右字符不重复
                map.remove(s[L])
                L += 1
        return maxlen

if __name__ == '__main__':
    s = "wobgrovwe"
    s1 = "bbbb"
    s2 = ""
    s3 = "abcabcbb"
    print(Solution().lengthOfLongestSubstring1(s))
