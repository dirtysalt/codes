#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        from collections import defaultdict
        his = defaultdict(list)
        ans = []
        for k, t in zip(keyName, keyTime):
            m = int(t[:2]) * 60 + int(t[3:])
            his[k].append(m)

        for k, xs in his.items():
            n = len(xs)
            xs.sort()
            for i in range(2, n):
                if (xs[i] - xs[i - 2]) <= 60:
                    ans.append(k)
                    break

        ans = list(ans)
        ans.sort()
        return ans


cases = [
    (["a", "a", "a", "a", "a", "b", "b", "b", "b", "b", "b"],
     ["23:20", "11:09", "23:30", "23:02", "15:28", "22:57", "23:40", "03:43", "21:55", "20:38", "00:19"], ['a']),
    (["a", "a", "a", "a", "a", "a", "b", "b", "b", "b", "b"],
     ["23:27", "03:14", "12:57", "13:35", "13:18", "21:58", "22:39", "10:49", "19:37", "14:14", "10:41"], ['a']),
    (["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"],
     ["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"], ["daniel"]),
    (["alice", "alice", "alice", "bob", "bob", "bob", "bob"],
     ["12:01", "12:00", "18:00", "21:00", "21:20", "21:30", "23:00"], ["bob"]),
    (["john", "john", "john"],
     ["23:58", "23:59", "00:01"], []),
    (["leslie", "leslie", "leslie", "clare", "clare", "clare", "clare"],
     ["13:00", "13:20", "14:00", "18:00", "18:51", "19:30", "19:49"], ["clare", "leslie"]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().alertNames, cases)
