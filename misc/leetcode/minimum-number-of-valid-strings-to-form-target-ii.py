#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


# 这题数据规模有点大，需要更简单的算法. 看题解可以学学AC算法
# class Solution:
#     def minValidStrings(self, words: List[str], target: str) -> int:
#         class Trie:
#             def __init__(self):
#                 self.child = [None] * 26
#
#         def insert(root, w):
#             for pos, c in enumerate(w):
#                 c = ord(c) - ord('a')
#                 if root.child[c] is None:
#                     x = Trie()
#                     root.child[c] = x
#                 root = root.child[c]
#
#         trie = Trie()
#         for idx, w in enumerate(words):
#             print(len(w))
#             insert(trie, w)
#
#         n = len(target)
#         inf = (1 << 63) - 1
#         dp = [inf] * (n + 1)
#         dp[0] = 0
#
#         for i in range(n):
#             old = dp[i]
#             root = trie
#             for j in range(i, n):
#                 c = ord(target[j]) - ord('a')
#                 if not root.child[c]: break
#                 dp[j + 1] = min(dp[j + 1], old + 1)
#                 root = root.child[c]
#
#         ans = dp[-1]
#         if ans == inf: return -1
#         return ans

class ACTrie:
    def __init__(self):
        self.child: List[ACTrie] = [None] * 26
        self.fail = None
        self.length = 0
        self.word = None

    def __repr__(self):
        return '%s' % (self.word if self.word else '?')

    def add(self, w):
        root = self
        for pos, c in enumerate(w):
            c = ord(c) - ord('a')
            if root.child[c] is None:
                x = ACTrie()
                root.child[c] = x
            root = root.child[c]
            root.length = pos + 1
            # root.word = w[:pos + 1]

    def build_fail(self):
        root = self
        from collections import deque
        q = deque()
        for i, t in enumerate(root.child):
            if t is not None:
                t.fail = root
                q.append(t)
            else:
                root.child[i] = root

        while q:
            x = q.popleft()
            for i, t in enumerate(x.child):
                f = x.fail
                while f and f.child[i] is None:
                    f = f.fail
                f = f.child[i] if f else root

                if t is not None:
                    t.fail = f
                    q.append(t)
                else:
                    x.child[i] = f


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:

        trie = ACTrie()
        for w in words:
            trie.add(w)
        trie.build_fail()

        n = len(target)
        dp = [0] * (n + 1)
        now = trie
        for i, c in enumerate(target):
            c = ord(c) - ord('a')
            now = now.child[c]
            if now is trie: return -1
            dp[i + 1] = dp[i + 1 - now.length] + 1
        return dp[-1]


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(words=["abc", "aaaaa", "bcdef"], target="aabcdabc", res=3),
    aatest_helper.OrderedDict(words=["abababab", "ab"], target="ababaababa", res=2),
    aatest_helper.OrderedDict(words=["abcdef"], target="xyz", res=-1),
    (["abc", ], "ab", 1),
    (["ba", "cabccabaaacabcd"], "babcc", 4),
    (["ba", "ca"], "babcc", 4),
]

# cases += aatest_helper.read_cases_from_file('tmp.in', 3)

aatest_helper.run_test_cases(Solution().minValidStrings, cases)

if __name__ == '__main__':
    pass
