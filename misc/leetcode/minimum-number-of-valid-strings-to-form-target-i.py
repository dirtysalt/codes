#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        class Trie:
            def __init__(self):
                self.child = [None] * 26

        def insert(root, w):
            for pos, c in enumerate(w):
                c = ord(c) - ord('a')
                if root.child[c] is None:
                    x = Trie()
                    root.child[c] = x
                root = root.child[c]

        trie = Trie()
        for idx, w in enumerate(words):
            insert(trie, w)

        n = len(target)
        inf = (1 << 63) - 1
        dp = [inf] * (n + 1)
        dp[0] = 0

        for i in range(n):
            old = dp[i]
            root = trie
            for j in range(i, n):
                c = ord(target[j]) - ord('a')
                if not root.child[c]: break
                dp[j + 1] = min(dp[j + 1], old + 1)
                root = root.child[c]

        ans = dp[-1]
        if ans == inf: return -1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(words=["abc", "aaaaa", "bcdef"], target="aabcdabc", res=3),
    aatest_helper.OrderedDict(words=["abababab", "ab"], target="ababaababa", res=2),
    aatest_helper.OrderedDict(words=["abcdef"], target="xyz", res=-1),
    (["abc", ], "ab", 1),
    (["ba", "cabccabaaacabc"], "babcc", 4),
]
#
# cases += aatest_helper.read_cases_from_file('tmp.in', 3)

aatest_helper.run_test_cases(Solution().minValidStrings, cases)

if __name__ == '__main__':
    pass
