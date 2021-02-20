#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


from collections import deque


class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        if beginWord in wordlist:
            wordlist.remove(beginWord)
        if endWord in wordlist:
            wordlist.remove(endWord)
        else:
            return []

        # beginWord = 0, endWord = n - 1
        wordlist = list(wordlist)
        wordlist.insert(0, beginWord)
        wordlist.append(endWord)
        n = len(wordlist)
        k = len(beginWord)

        tb = []
        G = []
        for i in range(n):
            G.append([])
            tb.append([])

        # 这里计算G有一些技巧
        # 如果简单地O(n^2)去计算两个word是否相差一个字符的话是会出现TLE的。
        # 我观察到的是，为什么hit和hot是相差一个字符的，是因为如果我们把字符串rotate一下的话
        # 那么就只需要检查除去最后一个字符串是否相同即可：hit -> thi,  hot -> tho.
        # 注意这里需要使用所有的位置来rotate. 好处是一旦rotate完成后，就是线性比较，速度会加快不少。
        # 或者是我们枚举所有忽略字符的位置，然后只比较剩余位置的字符串，这样可能会更简单一些

        # print(wordlist)
        # 比如[hit, hot, hat]，如果忽略第二个字符的话，那么变为[ht/0, ht/1, ht/2]
        # 说明这第三个字符串其实相差距离为1

        for i in range(k):
            wl = [(x[:i] + x[i + 1:], idx) for (idx, x) in enumerate(wordlist)]
            from collections import defaultdict
            groups = defaultdict(list)
            for w, idx in wl:
                groups[w].append(idx)
            for w, xs in groups.items():
                for j in range(len(xs)):
                    for k in range(j + 1, len(xs)):
                        x, y = xs[j], xs[k]
                        G[x].append(y)
                        G[y].append(x)

        Q = deque()
        visited = [0] * n
        Q.append((0, 0))

        while len(Q):
            (v, d) = Q.popleft()
            if v == (n - 1):
                break

            for v2 in G[v]:
                tb[v2].append((v, d + 1))
                if not visited[v2]:
                    visited[v2] = 1
                    Q.append((v2, d + 1))

        # for i in range(n):
        #     print '{} -> {}'.format(i, tb[i])

        if not tb[n - 1]: return []

        min_dist = min([x[1] for x in tb[n - 1]])
        res = []

        def backtrace(idx, dist, r):
            if idx == 0:
                res.append([wordlist[x] for x in reversed(r)])
                return

            for (v, d) in tb[idx]:
                if d > dist: break
                r.append(v)
                backtrace(v, dist - 1, r)
                r.pop()

        r = [n - 1]
        backtrace(n - 1, min_dist, r)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findLadders('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]))
    print(s.findLadders('hot', 'dog', ["hot", 'dog']))
    print(s.findLadders("lost", "miss", ["most", "mist", "miss", "lost", "fist", "fish"]))
