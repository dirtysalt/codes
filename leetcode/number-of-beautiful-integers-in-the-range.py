#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def OkOddEven(isStart, odd, even, left):
            if isStart:
                for x in range(0, left + 1):
                    if (odd + x) == (even + left - x):
                        return True
                return False
            else:
                if (odd + left) < even or (even + left) < odd:
                    return False
                return True

        def search(ss):
            import functools
            @functools.cache
            def f(i, isLimit, isStart, odd, even, value):
                # print(i, isLimit, isStart, odd, even, value)
                if i == len(ss):
                    if not isStart: return 0
                    if odd == even and value % k == 0:
                        # print(value)
                        return 1
                    return 0

                left = len(ss) - i
                if not OkOddEven(isStart, odd, even, left):
                    return 0

                ans = 0
                if not isStart:
                    ans += f(i + 1, True, False, odd, even, value)

                from_value = 1 if not isStart else 0
                to_value = int(ss[i]) if not isLimit else 9
                for x in range(from_value, to_value + 1):
                    ans += f(i + 1, isLimit or x < int(ss[i]), isStart or x != 0,
                             odd + (x % 2), even + (x + 1) % 2,
                             # value * 10 + x)
                             (value * 10 + x) % k)
                return ans

            return f(0, False, False, 0, 0, 0)

        h = search(str(high))
        l = search(str(low - 1))
        ans = h - l
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (10, 20, 3, 2),
    (1, 10, 1, 1),
    (5, 5, 2, 0),
    (47, 100, 18, 3),
    (1, (10 ** 9), 1, 24894045)
]

aatest_helper.run_test_cases(Solution().numberOfBeautifulIntegers, cases)

if __name__ == '__main__':
    pass
