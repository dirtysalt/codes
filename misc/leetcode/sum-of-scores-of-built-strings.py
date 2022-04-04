#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class StringHashBuilder:
    BASE = 13131
    MOD = 151217133020331712151
    # OFFSET = ord('a')
    OFFSET = 96

    def __init__(self, s):
        n = len(s)
        self.hash = [0] * (n + 1)
        self.base = [0] * (n + 1)
        self.base[0] = b = 1
        self.hash[0] = h = 0
        for i in range(n):
            h = (h * self.BASE + ord(s[i]) - self.OFFSET) % self.MOD
            b = (b * self.BASE) % self.MOD
            self.hash[i + 1] = h
            self.base[i + 1] = b

    def getHash(self, left, right):
        upper = self.hash[right]
        lower = (self.hash[left] * self.base[right - left]) % self.MOD
        return (upper - lower + self.MOD) % self.MOD


class Solution:
    def sumScores(self, s: str) -> int:
        sb = StringHashBuilder(s)

        def test(size):
            i = len(s) - size
            if s[i] != s[0]:
                return 0

            l, r = 1, size
            while l <= r:
                m = (l + r) // 2
                a = sb.getHash(0, m)
                b = sb.getHash(i, i + m)
                if a == b:  # and (m > 32 or s[:m] == s[i:i + m]):
                    l = m + 1
                else:
                    r = m - 1

            return r

        ans = 0
        for size in range(1, len(s) + 1):
            c = test(size)
            ans += c
        return ans


true, false, null = True, False, None
cases = [
    ("babab", 9),
    ("azbazbzaz", 14),
    (
        "nskmiwknpiclnptttlihicvixtqyxzdyrkulgqpfeckxssnlekuxiwvmxhyfzsptcjdqxvuavtakihlizitoozcnnubaafdsadfrvxnadgfshkpfqpcfrtcjsydkjbaupsflzgyumyggutzjcicbqmeghncnsgjkwqwksyahxsykyjnqvofkmpxmeaqqhtddflkwvpbpqzkxzyzkdcrctmopmiipaewlw",
        235),
    ('p' * 1000, 500500),
    ('bv' * 10000, 100010000),
    ("alvhjwigezdvgnyjyiplzxggzjbdtualvhjwigezdvgnyjyiplzxggzjbdtuaaremrmxffewjrf", 108),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().sumScores, cases)

if __name__ == '__main__':
    pass
