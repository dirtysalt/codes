#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        def expect(s):
            postfix = []
            prefix = []
            n = len(s)
            for i in range(0, n + 1):
                x = s[:i]
                y = s[i:]
                if y == y[::-1]:
                    postfix.append(x[::-1])
                if x == x[::-1]:
                    prefix.append(y[::-1])

            return prefix, postfix

        from collections import defaultdict
        post_exp = defaultdict(list)
        pre_exp = defaultdict(list)

        for i, w in enumerate(words):
            pre, post = expect(w)
            for x in pre:
                pre_exp[x].append(i)
            for x in post:
                post_exp[x].append(i)

        # print(pre_exp, post_exp)
        ans = []
        visited = set()
        for i, w in enumerate(words):
            for j in post_exp[w]:
                if i != j and (j, i) not in visited:
                    visited.add((j, i))
                    ans.append((j, i))
            for j in pre_exp[w]:
                if i != j and (i, j) not in visited:
                    visited.add((i, j))
                    ans.append((i, j))

        return ans

