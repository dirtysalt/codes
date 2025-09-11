#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alienOrder(self, words):
        # Write your code here

        from collections import Counter, defaultdict
        ind = defaultdict(int)
        edges = defaultdict(list)
        chars = set()

        # O(N * W)
        for i in range(1, len(words)):
            w0 = words[i - 1]
            w1 = words[i]
            chars.update(w0)
            chars.update(w1)
            for j in range(min(len(w0), len(w1))):
                if w0[j] != w1[j]:
                    edges[w0[j]].append(w1[j])
                    ind[w1[j]] += 1
                    if w0[j] not in ind:
                        ind[w0[j]] = 0
                    break

        opts = []
        # O(V)
        for k, v in ind.items():
            if v == 0:
                opts.append(k)

        # O(E)
        orders = {}
        while opts:
            k = opts.pop()
            orders[k] = len(orders)
            for k2 in edges[k]:
                ind[k2] -= 1
                if ind[k2] == 0:
                    opts.append(k2)

        # print(orders, ind)
        # 确保orders的数量 == ind的数量，这意味着没有环
        if len(orders) != len(ind):
            return ""

        ans = list(chars)

        def cmpfn(x, y):
            if x in orders and y in orders:
                return orders[x] - orders[y]
            else:
                return ord(x) - ord(y)

        import functools
        ans.sort(key=functools.cmp_to_key(cmpfn))
        ans = ''.join(ans)
        return ans


cases = [
    (["wrt", "wrf", "er", "ett", "rftt"], "wertf"),
    (["z", "x"], "zx"),
    (["zy", "zx"], "yxz"),
    (["ay", "ax"], "ayx"),
    (["abc", "bcd", "qwert", "ab"], ""),
    (["ze", "yf", "xd", "wd", "vd", "ua", "tt", "sz", "rd", "qd", "pz", "op", "nw", "mt", "ln", "ko", "jm", "il", "ho",
      "gk", "fa", "ed", "dg", "ct", "bb", "ba"], "zyxwvutsrqponmlkjihgfedcba")
]

import aatest_helper

aatest_helper.run_test_cases(Solution().alienOrder, cases)
