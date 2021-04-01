# -*- coding:utf-8 -*-
# @FileName  :DFS_BFS.py
# @Time      :2021/3/30 13:49
# @Author    :Haozr
from typing import List
import unittest
import sys
INF = sys.maxsize
# 解法1：
class Solution:
    def dfs_raverse(self,G):
        """图的深度优先搜索遍历"""
        visit_list = []
        def dfs(v):
            """从v开始遍历"""
            visit_list.append(v)
            for e in G[v]:
                if e not in visit_list:
                    dfs(e)
        for v in G.keys():
            if v not in visit_list:
                dfs(v)
        print(visit_list)

    def bfs_raverse(self,G):
        queue = []
        visit_list = []
        for v in G.keys():
            if v not in visit_list:
                visit_list.append(v)
                queue.append(v)
                while queue:
                    v = queue.pop(0)
                    for e in G[v]:
                        if e not in visit_list:
                            queue.append(e)
                            visit_list.append(e)
        print(visit_list)

    def dijkstra(self,v0,G):
        """迪杰斯特拉算法+小顶堆 单源点最短路径 顶点v到其余顶点的最短路径"""
        import heapq
        R = set()#还没有求出的最短路径顶点集合
        dist = {v0:0}#最短路径的距离，
        minheap = [] #小顶堆,寻找当前最短的路
        minPath = {v0:[v0]} #存放最短路径
        for e in G.keys():
            if e == v0:
                continue
            if e not in G[v0]:
                heapq.heappush(minheap, (INF, e))
                dist[e] = INF
            else:
                heapq.heappush(minheap, (G[v0][e], e))
                dist[e] = G[v0][e]
            minPath[e] = [v0]
            R.add(e)
        while len(R) > 0:
            min, minv = heapq.heappop(minheap)
            if min == INF:
                break
            minPath[minv].append(minv)
            R.remove(minv)
            #print(minv, dist, R,minheap)
            for k, v in G[minv].items():
                if dist[minv] + v < dist[k]:
                    dist[k] = dist[minv] + v
                    minPath[k].append(minv)

        for k,v in dist.items():
            print(v,minPath[k],k)

    def floyd(self,v0,G):
        """弗洛伊德  任意两个顶点之间的距离"""
        dist = {}#存放距离
        paths = {}#存放路径
        for i in G.keys():
            dist[i] = {}
            paths[i] = {}
            for j in G.keys():
                paths[i][j] = []
                if i == j:
                    dist[i][j] = 0
                dist[i][j] = INF
        for i in G.keys():
            for j in G[i].keys():
                dist[i][j] = G[i][j]
        print(paths)
        for k in G.keys():#从每个顶点走，更新所有距离矩阵的值
            for i in G.keys():
                for j in G.keys():
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        paths[i][j].append(k)
        for i in G.keys():
            for j in G.keys():
                print(i,j,dist[i][j])
                print(i,j,paths[i][j])


    def findWhetherExistsPath1(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        """面试题 04.01. 节点间通路 BFS+集合"""
        if start == target:
            return True
        visit = {start}
        g = {}
        for i in range(n):
            g[i] = set()
        for e in graph:
            g[e[0]].add(e[1])
        print(g)
        queue = [start]
        while queue:
            v = queue.pop()
            for e in g[v]:
                if e == target:
                    return True
                if not e in visit:
                    visit.add(e)
                    queue.append(e)
        return False

    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        """面试题 04.01. 节点间通路 DFS+集合"""
        if start == target:
            return True
        visit = set()
        g = {}
        for i in range(n):
            g[i] = set()
        for e in graph:
            g[e[0]].add(e[1])
        print(g)
        def dfs(v):
            if v == target:
                return True
            visit.add(v)
            for e in g[v]:
                if not e in visit:
                    if dfs(e):
                        return True
            return False
        return dfs(start)

    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        """1786. 从第一个节点出发到最后一个节点的受限路径数 dfs求出所有路径"""
        n_dist = [INF*n]
        R = set()
        g = {}
        for i in range(n):
            g[i+1] = {}
            R.add(i+1)
        for start, end, val in edges:
            g[start][end] = val
            g[end][start] = val
            if start == n:
                n_dist[end-1] = val
            elif end == n:
                n_dist[start-1] = val
        n_dist[n-1] = 0
        R.remove(n)
        k = n
        minv = n
        while len(R) > 0:
            min = INF
            for i in g[k].keys():
                if i in R and n_dist[i - 1] < min:
                    min = n_dist[i - 1]
                    minv = i
            if min == INF:
                break
            for i in g[minv].keys():
                if n_dist[minv] + g[minv][i] < n_dist[i-1]:
                    n_dist[i-1] = n_dist[minv] + g[minv][i]
        # 找1->n的所有路 bfs
        queue = [1]
        visited = [False]*n
        visited[0] = True
        paths = []
        while queue:
            k = queue.pop()
            for i in g[k].keys():
                if visited[i-1]:
                    visited[i-1] = False

s = Solution()


class TestSolution(unittest.TestCase):
    def test_findWhetherExistsPath(self):
        n = 3
        graph = [[0, 1], [0, 2], [1, 2], [1, 2]]
        start = 1
        target = 2
        self.assertEqual(s.findWhetherExistsPath(n,graph,start,target),True)

        n = 5
        graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3]]
        start = 0
        target = 4
        self.assertEqual(s.findWhetherExistsPath(n, graph, start, target), True)

    def test_dfs_bfs_raverse(self):
        Graph = {'A': ['B', 'C', 'D'],  # 构建图
                 'B': ['E'],
                 'C': ['D', 'F'],
                 'D': ['B', 'E', 'G'],
                 'E': [],
                 'F': ['D', 'G'],
                 'G': ['E']}
        s.dfs_raverse(Graph)#['A', 'B', 'E', 'C', 'D', 'G', 'F']
        s.bfs_raverse(Graph)#['A', 'B', 'C', 'D', 'E', 'F', 'G']
    def test_dijkstra(self):
        Graph = {'A': {'B':2, 'C':4, 'D':1},  # 构建图
                 'B': {'E':6},
                 'C': {'D':3, 'F':8},
                 'D': {'B':1, 'E':9, 'G':3},
                 'E': {},
                 'F': {'D':2, 'G':1},
                 'G': {'E':5}}
        s.dijkstra('F', Graph)
if __name__ == '__main__':
    #    s = Solution()
    unittest.main()
