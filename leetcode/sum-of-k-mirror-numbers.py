#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def kMirror(self, k: int, n: int) -> int:

        def gen(k):
            arr = [0]
            size = 1
            pos = 0
            while True:
                while pos < size and arr[pos] == (k - 1):
                    pos += 1

                if pos == size:
                    size += 1
                    arr = [0] * size
                    arr[0] = 1
                    arr[-1] = 1
                    pos = size // 2
                else:
                    t = pos
                    f = size - 1 - pos
                    for i in range(f + 1, t):
                        arr[i] = 0

                    arr[f] += 1
                    if f != t:
                        arr[t] += 1
                    pos = size // 2

                yield arr

        def check(arr, k):
            tmp = 0
            for x in arr:
                tmp = tmp * 10 + x
            res = tmp

            st = []
            while tmp:
                st.append(tmp % k)
                tmp = tmp // k
            for i in range(len(st) // 2 + 1):
                if st[i] != st[-(1 + i)]:
                    return False, 0

            return True, res

        rs = gen(10)
        ans = 0
        while n:
            arr = next(rs)
            ok, res = check(arr, k)
            if ok:
                # print(arr, res)
                n -= 1
                ans += res
        return ans


true, false, null = True, False, None
cases = [
    (2, 5, 25),
    (3, 7, 499),
    (7, 17, 20379000),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().kMirror, cases)

if __name__ == '__main__':
    pass
