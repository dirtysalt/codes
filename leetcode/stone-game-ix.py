#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0] * 3
        for x in stones:
            cnt[x % 3] += 1
        cnt[0] %= 2

        mx = max(0, min(cnt[1], cnt[2]) - 1)
        cnt[1] -= mx
        cnt[2] -= mx

        def search(t, cnt, ab):
            if sum(cnt) == 0:
                # if this is alice, then lose
                # else win.
                return ab

            values = [1]
            for i in range(3):
                if (i + t) % 3 == 0: continue
                if cnt[i] > 0:
                    cnt2 = cnt.copy()
                    cnt2[i] -= 1
                    x = search(t + i, cnt2, 1 - ab)
                    values.append(x)

            m = min(values)
            return 1 - m

        ans = search(0, cnt, 0)
        return ans == 1


true, false, null = True, False, None
cases = [
    ([2, 1], true),
    ([2], false),
    ([5, 1, 2, 4, 3], false),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().stoneGameIX, cases)

if __name__ == '__main__':
    pass
