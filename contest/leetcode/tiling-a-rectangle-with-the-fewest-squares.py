#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        import functools

        @functools.lru_cache(None)
        def fun(st):
            # print(st)
            assert len(st) == n

            start = None
            for i in range(n):
                if st[i] != m:
                    start = i
                    break
            if start is None:
                return 0

            ans = 1 << 30
            for sz in range(1, n - start + 1):
                new_st = list(st)
                ok = True
                for j in range(sz):
                    if (new_st[start + j] + sz) > m:
                        ok = False
                        break
                    new_st[start + j] += sz

                if ok:
                    res = 1 + fun(tuple(new_st))
                    ans = min(ans, res)

            # print(st, ans)
            return ans

        st = [0] * n
        ans = fun(tuple(st))
        return ans
