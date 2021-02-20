#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        from collections import defaultdict
        map = defaultdict(list)
        for w in allowed:
            map[w[:2]].append(w[2:])

        dp = {}

        def fn(s):
            if len(s) == 1:
                return True

            # print(s)
            if s in dp:
                return dp[s]

            cs = []
            ret = True
            for i in range(len(s) - 1):
                w = s[i:i + 2]
                xs = map[w]
                if not xs:
                    ret = False
                    break
                cs.append(map[w])

            if not ret:
                dp[s] = ret
                return ret

            def gen(s, i):
                if i == len(cs):
                    yield s
                else:
                    for x in cs[i]:
                        yield from gen(s + x, i + 1)

            ret = False
            for x in gen('', 0):
                if fn(x):
                    ret = True
                    break

            dp[s] = ret
            return ret

        ans = fn(bottom)
        return ans


cases = [
    ("AABA", ["AAA", "AAB", "ABA", "ABB", "BAC"], False),
    ("BCD", ["BCG", "CDE", "GEA", "FFF"], True),
    ("CCC",
     ["CBB", "ACB", "ABD", "CDB", "BDC", "CBC", "DBA", "DBB", "CAB", "BCB", "BCC", "BAA", "CCD", "BDD", "DDD", "CCA",
      "CAA", "CCC", "CCB"], True)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().pyramidTransition, cases)
