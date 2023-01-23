#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from collections import deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        if beginWord in wordList:
            wordList.remove(beginWord)
        if endWord in wordList:
            wordList.remove(endWord)
        else:
            return 0
        wordList = list(wordList)
        wordList.insert(0, beginWord)
        wordList.append(endWord)
        n = len(wordList)
        k = len(beginWord)

        G = []
        for i in range(n):
            G.append([])

        # 这里计算G有一些技巧
        # 如果简单地O(n^2)去计算两个word是否相差一个字符的话是会出现TLE的。
        # 我观察到的是，为什么hit和hot是相差一个字符的，是因为如果我们把字符串rotate一下的话
        # 那么就只需要检查除去最后一个字符串是否相同即可：hit -> thi,  hot -> tho.
        # 注意这里需要使用所有的位置来rotate. 好处是一旦rotate完成后，就是线性比较，速度会加快不少。

        for i in range(k):
            wl = [(x[:i] + x[i + 1:], idx) for (idx, x) in enumerate(wordList)]
            wl.sort(key=lambda x: x[0])
            pfx = 0
            groups = [[0]]
            for j in range(1, n):
                if wl[j][0] == wl[pfx][0]:
                    groups[-1].append(j)
                else:
                    pfx = j
                    groups.append([pfx])
            # print(wl, groups)
            for group in groups:
                for xi in range(0, len(group)):
                    for yi in range(xi + 1, len(group)):
                        x, y = group[xi], group[yi]
                        G[wl[x][1]].append(wl[y][1])
                        G[wl[y][1]].append(wl[x][1])

        Q = deque()
        visited = [0] * n
        visited[0] = 1

        Q.append((0, 0))
        while len(Q):
            (v, d) = Q.popleft()
            if v == (n - 1):
                return d + 1
            for v2 in G[v]:
                if visited[v2]: continue
                visited[v2] = 1
                Q.append((v2, d + 1))
        return 0
