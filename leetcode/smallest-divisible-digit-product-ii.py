#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        cnt = 0
        t2 = t
        for p in (2, 3, 5, 7):
            while t2 % p == 0:
                t2 = t2 // p
                cnt += 1
        if t2 != 1:
            return "-1"

        pad = max(cnt - len(num), 0) + 1
        num = '0' * pad + num

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        ans = [0] * len(num)

        import functools
        @functools.lru_cache(None)
        def dfs(i, t, cap):
            if i == len(num):
                # print(ans, t)
                return t == 1

            if i < pad and not cap:
                if dfs(i + 1, t, cap):
                    return True

            d = int(num[i])
            low = d if not cap else 0
            for x in range(max(low, 1), 10):
                ans[i] = x
                if dfs(i + 1, t // gcd(t, x), cap or (x > d)):
                    return True
            return False

        dfs(0, t, False)
        dfs.cache_clear()
        ans = ''.join([str(x) for x in ans])
        # print(ans)
        return ans.lstrip('0')


true, false, null = True, False, None
import aatest_helper

cases = [
    # ('1234', 256, '1488'),
    # ('12355', 50, '12355'),
    # ('11111', 26, '-1'),
    ('10', 320, '588')
]

aatest_helper.run_test_cases(Solution().smallestNumber, cases)

if __name__ == '__main__':
    pass
