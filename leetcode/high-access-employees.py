#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        def tomin(x):
            return int(x[:2]) * 60 + int(x[2:])

        from collections import defaultdict
        g = defaultdict(list)
        for name, time in access_times:
            g[name].append(tomin(time))

        ans = []
        for name, ts in g.items():
            ts.sort()
            ok = False
            for i in range(2, len(ts)):
                if ts[i] - ts[i - 2] < 60:
                    ok = True
                    break
            if ok:
                ans.append(name)
        ans.sort()
        return ans


if __name__ == '__main__':
    pass
