#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    class BIT:
        def __init__(self, n):
            self.n = n
            self.values = [0] * (n + 1)

        def update(self, x):
            x += 1
            n = self.n
            while x <= n:
                self.values[x] += 1
                x += (x & -x)

        def query(self, x):
            x += 1
            ans = 0
            while x > 0:
                ans += self.values[x]
                x -= (x & -x)
            return ans

    class BS:
        def __init__(self, n):
            self.bs = []

        def update(self, x):
            import bisect
            bisect.insort(self.bs, x)

        def query(self, x):
            import bisect
            return bisect.bisect(self.bs, x)

    def minInteger(self, num: str, k: int) -> str:

        qs = [[] for _ in range(10)]
        buf = []
        for i in reversed(range(len(num))):
            c = int(num[i])
            qs[c].append(i)

        BSClass = self.BIT
        bs = BSClass(len(num))
        while k and len(buf) < len(num):
            ok = False
            for i in range(10):
                if not qs[i]: continue
                q = qs[i][-1]
                j = bs.query(q)
                # print(q, j)
                if (q - j) <= k:
                    qs[i].pop()
                    bs.update(q)
                    k -= (q - j)
                    buf.append(q)
                    ok = True
                    break
            if not ok: break

        used = set(buf)
        ans = []
        for q in buf:
            ans.append(num[q])
        for i in range(len(num)):
            if i in used: continue
            ans.append(num[i])

        ans = ''.join(ans)
        return ans


cases = [
    ("4321", 4, "1342"),
    ("9438957234785635408", 23, "0345989723478563548"),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minInteger, cases)
