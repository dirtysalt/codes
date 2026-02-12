#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:

        def test(size):
            D = -1
            for d in range(1, 6):
                if 10 ** d > size:
                    D = d
                    break

            res = 0
            for d in range(1, D + 1):
                prev = 10 ** (d - 1) - 1
                now = 10 ** d - 1
                num = min(size - prev, now - prev)
                overhead = 3 + d + D
                # print(overhead, num)
                if overhead < limit:
                    res += (limit - overhead) * num
            return res >= len(message)

        def emit(message, size):
            ans = []
            for i in range(1, size + 1):
                end = '<{}/{}>'.format(i, size)
                room = limit - len(end)
                ans.append(message[:room] + end)
                message = message[room:]
            return ans

        s, e = 1, len(message)
        while s <= e:
            m = (s + e) // 2
            if test(m):
                e = m - 1
            else:
                s = m + 1
        if s > len(message):
            return []

        ans = emit(message, s)
        return ans


true, false, null = True, False, None
cases = [
    ("this is really a very awesome message", 9,
     ["thi<1/14>", "s i<2/14>", "s r<3/14>", "eal<4/14>", "ly <5/14>", "a v<6/14>", "ery<7/14>", " aw<8/14>",
      "eso<9/14>", "me<10/14>", " m<11/14>", "es<12/14>", "sa<13/14>", "ge<14/14>"]),
    ("boxpn", 5, [])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().splitMessage, cases)

if __name__ == '__main__':
    pass
