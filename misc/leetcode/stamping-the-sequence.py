#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        from collections import defaultdict
        stampDist = defaultdict(list)
        for i in range(len(stamp)):
            stampDist[stamp[i]].append(i)

        targetUnmatched = set(range(len(target)))

        def match(p, x):
            mark = []
            for y in targetUnmatched:
                # x - y = p - p2
                p2 = p + y - x
                if 0 <= p2 < len(stamp):
                    if stamp[p2] != target[y]:
                        return False, []
                    mark.append(y)
            return True, mark

        def search():
            for x in targetUnmatched:
                ps = stampDist[target[x]]
                for p in ps:
                    if x < p or (len(target) - x + p) < len(stamp): continue

                    # target[x] == stamp[c]
                    # 看其他位置是否都匹配上
                    ok, mark = match(p, x)
                    if ok:
                        for y in mark:
                            targetUnmatched.remove(y)
                        return x - p
            return None

        ans = []
        while targetUnmatched:
            res = search()
            # print(res, targetUnmatched)
            if res is None:
                return []
            ans.append(res)
        ans = ans[::-1]
        return ans


cases = [
    ("abc", "ababc", [0, 2]),
    ("abca", "aabcaca", [3, 0, 1]),
    ("ffebb", "fffeffebbb", [5, 0, 1, 4]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().movesToStamp, cases)
