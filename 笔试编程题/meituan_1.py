# -*- coding:utf-8 -*-
# @FileName  :meituan-1.py
# @Time      :2021/4/4 10:10
# @Author    :Haozr
from typing import List
import unittest


# 解法1：
class Solution:
    def youmei(self,ss):
        res = [""]
        n = len(ss)
        for s in ss:
            for r in res:
                flag = False
                for t in r:
                    if t == s:
                        flag =True
                        break
                if flag == False:
                    res.append(r+s)
        print(res)
        print("****")
        return len(res)%20210101

    def hz(self):
        n = int(input())
        kuai = 1
        allx = []
        ally = []
        while n:
            tt = input().split(' ')
            nowt = int(tt[0])
            nowx = int(tt[1])
            if nowt == 1:
                ally.append(nowx)
            else:
                allx.append(nowx)
            n -= 1
        print(allx, ally)
        nx = len(allx)
        ny = len(ally)
        for i in range(nx):
            if i > 180:
                nx[i] = 360 - nx[i]
        for i in range(ny):
            if i > 180:
                ny[i] = 360 - ny[i]
        allx.sort()
        ally.sort()
        kuai += nx #先横着切
        for y in ally:
            count = 0
            for x in allx:
                if x > y:
                    count += 1
            print("count", count)
            kuai = kuai + 1 + count
        print(kuai)

s = Solution()


class TestSolution(unittest.TestCase):
    def test_2(self):
        s.hz()
    def test_(self):
        #ss = input()
        #print(ss,len(ss))
        self.assertEqual(s.youmei("ssss"),5)
        self.assertEqual(s.youmei("aabc"),12)
        self.assertEqual(s.youmei("aabca"),16)
        self.assertEqual(s.youmei(""),1)
        #self.assertEqual(s.youmei("aabca"),12)


if __name__ == '__main__':
    #    s = Solution()
    unittest.main()
