#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Trie:
    def __init__(self):
        self.nodes = [None] * 26
        self.index = []

    def insert(self, word, index):
        root = self
        for w in word:
            idx = ord(w) - ord('a')
            if root.nodes[idx] is None:
                root.nodes[idx] = Trie()
            root = root.nodes[idx]
            root.index.append(index)

    def collect(self, k):
        ans = []

        def walk(root: Trie, depth):
            if root is None:
                return
            if root is not self and len(root.index) < k:
                return
            if root.index:
                ans.append((depth, set(root.index)))
            for i in range(26):
                if root.nodes[i]:
                    walk(root.nodes[i], depth + 1)

        walk(self, 0)
        ans.sort(key=lambda x: x[0], reverse=True)
        return ans


class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        trie = Trie()
        for i in range(len(words)):
            trie.insert(words[i], i)
        stats = trie.collect(k)
        # stats = [x for x in stats if len(x[1]) >= k]

        ans = [0] * len(words)
        for i in range(len(words)):
            for d, s in stats:
                if (i in s and len(s) >= (k + 1)) or (i not in s and len(s) >= k):
                    ans[i] = d
                    break
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (["jump", "run", "run", "jump", "run"], 2, [3, 4, 4, 3, 4]),
    (["dog", "racer", "car"], 2, [0, 0, 0]),
]

aatest_helper.run_test_cases(Solution().longestCommonPrefix, cases)

if __name__ == '__main__':
    pass
