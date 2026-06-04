#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1

        ans = ''
        for i in range(26):
            if cnt[i] % 2 == 1:
                ans = chr(i + ord('a'))
                cnt[i] -= 1
            cnt[i] //= 2

        def comb_count(n: int, m: int):
            m = min(m, n - m)
            res = 1
            for i in range(1, m + 1):
                res = res * (n - i + 1) // i
                if res >= k: break
            return res

        def perm_count(sz):
            res = 1
            for i in range(26):
                if cnt[i] == 0: continue
                res *= comb_count(sz, cnt[i])
                if res >= k:
                    break
                sz -= cnt[i]
            return res

        st = []
        for _ in range(sum(cnt)):
            res = 0
            sz = sum(cnt)
            ok = False
            for i in range(26):
                if cnt[i] == 0: continue
                cnt[i] -= 1
                r = perm_count(sz - 1)
                if k <= (res + r):
                    st.append(chr(i + ord('a')))
                    k -= res
                    ok = True
                    break
                res += r
                cnt[i] += 1
            if not ok: return ""
        ans = ''.join(st) + ans + ''.join(reversed(st))
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ("abba", 2, "baab"),
    ("aa", 2, ""),
    ("bacab", 1, "abcba"),
    ("smxggxms", 17, "sxgmmgxs")
]

aatest_helper.run_test_cases(Solution().smallestPalindrome, cases)

if __name__ == '__main__':
    pass
