#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        MOD = 10 ** 9 + 7

        def convert(s):
            value = 0
            for c in s:
                value = value * 10 + int(c)
            arr = []
            while value > 0:
                arr.append(value % b)
                value //= b
            return arr[::-1]

        def search(s):
            import functools
            @functools.cache
            def dfs(i, last, less):
                if i == len(s): return 1
                d = s[i]
                ans = 0
                upper = (d + 1) if not less else b
                for bit in range(last, upper):
                    ans += dfs(i + 1, bit, less or (bit < d))
                    ans = ans % MOD
                return ans

            return dfs(0, 0, False)

        def ok(s):
            for i in range(1, len(s)):
                if s[i] < s[i - 1]: return False
            return True

        br, bl = convert(r), convert(l)
        # print(br, bl)
        rr, rl = search(br), search(bl)
        res = rr - rl
        if ok(bl):
            res += 1
        res = (res + MOD) % MOD
        return res


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(l="23", r="28", b=8, res=3),
    aatest_helper.OrderedDict(l="2", r="7", b=2, res=2),
]

aatest_helper.run_test_cases(Solution().countNumbers, cases)

if __name__ == '__main__':
    pass
