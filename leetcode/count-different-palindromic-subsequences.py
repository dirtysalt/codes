#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:

        dp = {}
        P = 10 ** 9 + 7
        n = len(S)

        use_binary_search = False
        if use_binary_search:
            pos = [[] for _ in range(4)]
            for i, c in enumerate(S):
                x = ord(c) - ord('a')
                pos[x].append(i)

            def search_right(p, c):
                ps = pos[c]
                s, e = 0, len(ps) - 1
                while s <= e:
                    m = (s + e) // 2
                    if ps[m] == p:
                        return p
                    elif ps[m] > p:
                        e = m - 1
                    else:
                        s = m + 1
                return ps[s] if 0 <= s < len(ps) else n

            def search_left(p, c):
                ps = pos[c]
                s, e = 0, len(ps) - 1
                while s <= e:
                    m = (s + e) // 2
                    if ps[m] == p:
                        return p
                    elif ps[m] > p:
                        e = m - 1
                    else:
                        s = m + 1
                return ps[e] if 0 <= e < len(ps) else -1

        use_array_index = True

        if use_array_index:
            most_right = [n] * 4
            right = [[n] * 4 for _ in range(n)]
            for i in reversed(range(n)):
                x = ord(S[i]) - ord('a')
                most_right[x] = i
                right[i] = most_right.copy()

            most_left = [-1] * 4
            left = [[-1] * 4 for _ in range(n)]
            for i in range(n):
                x = ord(S[i]) - ord('a')
                most_left[x] = i
                left[i] = most_left.copy()

            def search_right(p, c):
                return right[p][c]

            def search_left(p, c):
                return left[p][c]

        def fun(s, e, c):
            if s > e:
                return 0

            key = (s, e, c)
            if key in dp:
                return dp[key]

            # print(s, e, c)
            s = search_right(s, c)
            e = search_left(e, c)
            # print(s, e)
            if s > e:
                ans = 0
            elif s == e:
                ans = 1
            else:
                ans = 2  # 'xx or x'
                for x in range(4):
                    ans += fun(s + 1, e - 1, x)
                    ans = ans % P
            dp[key] = ans
            return ans

        ans = 0
        for c in range(4):
            ans += fun(0, len(S) - 1, c)
            ans = ans % P
        # print(dp)
        return ans


cases = [
    ('bccb', 6),
    ('abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba', 104860361)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countPalindromicSubsequences, cases)
