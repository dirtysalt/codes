#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        res = []
        for c in S:
            if c == '-':
                continue
            res.append(c)
        total = len(res)
        first = total % K
        if first == 0:
            first = K

        res2 = []
        res2.append(''.join(res[:first]))
        while first < len(res):
            res2.append('-')
            res2.append(''.join(res[first:first + K]))
            first += K

        s = ''.join(res2).upper()
        return s


def test():
    cases = [
        ("abc", 4, "ABC"),
        ("5F3Z-2e-9-w", 4, "5F3Z-2E9W"),
        ("2-5g-3-J", 2, "2-5G-3J"),
    ]
    sol = Solution()
    ok = True
    for c in cases:
        (s, k, exp) = c
        res = sol.licenseKeyFormatting(s, k)
        if res != exp:
            print('case failed. {}, out = {}'.format(c, res))
            ok = False
    if ok:
        print('cases passed!!!')


if __name__ == '__main__':
    test()
