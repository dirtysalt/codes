#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# RES = {(1, 1): 9, (1, 2): 4, (1, 3): 3, (1, 4): 2, (1, 5): 1, (1, 6): 1, (1, 7): 1, (1, 8): 1, (1, 9): 1, (2, 1): 9,
#        (2, 2): 4, (2, 3): 3, (2, 4): 2, (2, 5): 1, (2, 6): 1, (2, 7): 1, (2, 8): 1, (2, 9): 1, (3, 1): 243, (3, 2): 108,
#        (3, 3): 69, (3, 4): 54, (3, 5): 27, (3, 6): 30, (3, 7): 33, (3, 8): 27, (3, 9): 23, (4, 1): 252, (4, 2): 172,
#        (4, 3): 84, (4, 4): 98, (4, 5): 52, (4, 6): 58, (4, 7): 76, (4, 8): 52, (4, 9): 28, (5, 1): 10935, (5, 2): 7400,
#        (5, 3): 3573, (5, 4): 4208, (5, 5): 2231, (5, 6): 2468, (5, 7): 2665, (5, 8): 2231, (5, 9): 1191, (6, 1): 10944,
#        (6, 2): 9064, (6, 3): 3744, (6, 4): 6992, (6, 5): 3256, (6, 6): 3109, (6, 7): 3044, (6, 8): 5221, (6, 9): 1248,
#        (7, 1): 617463, (7, 2): 509248, (7, 3): 206217, (7, 4): 393948, (7, 5): 182335, (7, 6): 170176, (7, 7): 377610,
#        (7, 8): 292692, (7, 9): 68739, (8, 1): 617472, (8, 2): 563392, (8, 3): 207840, (8, 4): 494818, (8, 5): 237112,
#        (8, 6): 188945, (8, 7): 506388, (8, 8): 460048, (8, 9): 69280, (9, 1): 41457015, (9, 2): 37728000,
#        (9, 3): 13726509, (9, 4): 33175696, (9, 5): 15814071, (9, 6): 12476696, (9, 7): 36789447, (9, 8): 30771543,
#        (9, 9): 4623119, (10, 1): 41457024, (10, 2): 39718144, (10, 3): 13831104, (10, 4): 37326452, (10, 5): 19284856,
#        (10, 6): 13249798, (10, 7): 40242031, (10, 8): 35755906, (10, 9): 4610368}
#
#
# class Solution:
#     def countGoodIntegers(self, n: int, k: int) -> int:
#         return RES[(n, k)]


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        ans = 0

        import functools
        @functools.cache
        def C(n, m):
            if m == 0: return 1
            if n == m: return 1
            return C(n - 1, m - 1) + C(n - 1, m)

        def check(cnt):
            ans = 1
            base = n
            if cnt[0] != 0:
                ans *= C(base - 1, cnt[0])
                base -= cnt[0]

            for c in cnt[1:]:
                if c != 0:
                    ans *= C(base, c)
                    base -= c
            return ans

        dup = set()

        def dfs(i, now, cnt):
            nonlocal ans
            j = n - 1 - i
            if j < i:
                if now % k == 0:
                    cnt = tuple(cnt)
                    if cnt not in dup:
                        dup.add(cnt)
                        ans += check(cnt)
                return

            start = 1 if i == 0 else 0
            bi, bj = 10 ** i, 10 ** j
            for d in range(start, 10):
                if i != j:
                    d2 = now + d * bi + d * bj
                    cnt[d] += 2
                    dfs(i + 1, d2, cnt)
                    cnt[d] -= 2
                else:
                    d2 = now + d * bi
                    cnt[d] += 1
                    dfs(i + 1, d2, cnt)
                    cnt[d] -= 1
            return

        dfs(0, 0, [0] * 10)
        return ans


# res = {}
# for n in range(1, 10 + 1):
#     for k in range(1, 10):
#         r = Solution().countGoodIntegers(n, k)
#         res[(n, k)] = r
# print(res)

true, false, null = True, False, None
import aatest_helper

cases = [
    (3, 5, 27),
    (1, 4, 2),
    (5, 6, 2468),
    (10, 9, 4610368),
]

aatest_helper.run_test_cases(Solution().countGoodIntegers, cases)

if __name__ == '__main__':
    pass
