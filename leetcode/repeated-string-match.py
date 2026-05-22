#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        n, m = len(A), len(B)
        count = (m + n - 1) // n
        C = A * count
        for i in range(n):
            if (i + len(B)) > len(C):
                count += 1
                C = C + A
            if C[i:i + len(B)] == B:
                return count
        return -1


def test():
    cases = [
        ("abcd", "cdabcdab", 3)
    ]
    sol = Solution()
    ok = True
    for c in cases:
        (A, B, exp) = c
        res = sol.repeatedStringMatch(A, B)
        if res != exp:
            print('case failed. {}, out = {}'.format(c, res))
            ok = False
    if ok:
        print('cases passed!!!')


if __name__ == '__main__':
    test()
