#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        wordList = wordList.copy()
        if endWord not in wordList:
            return []
        if beginWord not in wordList:
            wordList.append(beginWord)

        from collections import defaultdict
        k = len(beginWord)
        n = len(wordList)
        adj = [[] for _ in range(n)]

        for i in range(k):
            subwords = defaultdict(list)
            for idx, w in enumerate(wordList):
                for c in range(26):
                    x = chr(ord('a') + c)
                    if x == w[i]:
                        continue
                    s = w[:i] + x + w[i + 1:]
                    subwords[s].append(idx)
            for idx, w in enumerate(wordList):
                xs = subwords[w]
                for x in xs:
                    adj[idx].append(x)

        # print(wordList)
        # print(adj)
        begin = wordList.index(beginWord)
        end = wordList.index(endWord)

        from collections import deque
        dq = deque()
        depth = [0] * n
        depth[begin] = 1
        dq.append(begin)

        fwd_links = [[] for _ in range(n)]
        back_links = [[] for _ in range(n)]
        while dq:
            s = dq.popleft()
            if s == end:
                break

            for t in adj[s]:
                if depth[t] == 0:
                    depth[t] = depth[s] + 1
                    dq.append(t)

                if depth[t] == (depth[s] + 1):
                    fwd_links[s].append(t)
                    back_links[t].append(s)

        if depth[end] == 0:
            return []

        fwd_iter = False

        if fwd_iter:
            ans = [[begin]]
            for i in range(1, depth[end]):
                tmp = []
                for path in ans:
                    e = path[-1]
                    d = len(path) + 1
                    for v in fwd_links[e]:
                        assert depth[v] == d
                        tmp.append(path + [v])
                ans = tmp

            ans = [[wordList[i] for i in path] for path in ans if path[-1] == end]
            # ans = [[wordList[i] for i in path] for path in ans]
            return ans

        fwd_rec = False
        if fwd_rec:
            ans = []

            def dfs(v, path):
                if v == end:
                    ans.append([wordList[i] for i in path])
                    return

                for t in fwd_links[v]:
                    assert depth[t] == len(path) + 1
                    path.append(t)
                    dfs(t, path)
                    path.pop()

            dfs(begin, [begin])
            return ans

        back_rec = True
        if back_rec:
            ans = []

            def dfs(v, path, d):
                if depth[v] > d:
                    return

                if v == begin:
                    ans.append([wordList[i] for i in reversed(path)])
                    return

                for t in back_links[v]:
                    path.append(t)
                    dfs(t, path, d - 1)
                    path.pop()

            dfs(end, [end], depth[end])
            return ans


cases = [
    ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"],
     [
         ["hit", "hot", "dot", "dog", "cog"],
         ["hit", "hot", "lot", "log", "cog"]
     ]),
    ("a", "c", ["a", "b", "c"], [["a", "c"]])

]

import aatest_helper

aatest_helper.run_test_cases(Solution().findLadders, cases)
