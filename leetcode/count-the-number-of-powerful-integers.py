#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:

        def find_upper(S):
            if len(s) > len(S): return 0
            ok = (s <= S[-len(s):])
            S = [ord(x) - ord('0') for x in S]

            import functools
            @functools.cache
            def search(i, less):
                if (i + len(s)) == len(S):
                    return 1 if (less or ok) else 0
                ans = 0
                for d in range(limit + 1):
                    if not less and d > S[i]: break
                    r = search(i + 1, less or (d < S[i]))
                    ans += r
                return ans

            return search(0, False)

        A = find_upper(str(start - 1))
        B = find_upper(str(finish))
        return B - A


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(start=1, finish=6000, limit=4, s="124", res=5),
    aatest_helper.OrderedDict(start=15, finish=215, limit=6, s="10", res=2),
    aatest_helper.OrderedDict(start=1000, finish=2000, limit=4, s="3000", res=0),
    (20, 1159, 5, "20", 8),
]

aatest_helper.run_test_cases(Solution().numberOfPowerfulInt, cases)

if __name__ == '__main__':
    pass
