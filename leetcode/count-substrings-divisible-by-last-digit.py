#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        def next_dist(dist, d):
            dist2 = [0] * 10
            for x in range(10):
                dist2[(x * 10) % d] += dist[x]
            return dist2

        ans = 0
        for d in range(1, 10):
            dist = [0] * 10
            dist[0] = 1
            count = 0
            now = 0
            for i in range(n):
                x = int(s[i])
                dist = next_dist(dist, d)
                now = (now * 10 + x) % d
                if x == d:
                    # find dist[z] where (now - z) % d == 0
                    # z % d == (now % d)
                    count += dist[now]
                dist[now] += 1
            ans += count
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ('12936', 11),
    ('5701283', 18),
    ('1010101010', 25),
]

aatest_helper.run_test_cases(Solution().countSubstrings, cases)

if __name__ == '__main__':
    pass
