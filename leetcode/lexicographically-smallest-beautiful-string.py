#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        CH = [ord(x) - ord('a') for x in s]
        n = len(CH)

        P = -1
        for i in reversed(range(n)):
            a, b, c = CH[i], CH[i - 1] if i - 1 >= 0 else -1, CH[i - 2] if i - 2 >= 0 else -1
            for j in range(1, k):
                a = CH[i] + j
                if a < k and a != b and a != c:
                    CH[i] = a
                    P = i
                    break
                if a >= k: break
            if P != -1: break

        if P == -1: return ""
        # print(CH, ''.join([chr(x + ord('a')) for x in CH]))

        for i in range(P + 1, n):
            a, b = CH[i - 2] if i - 2 >= 0 else -1, CH[i - 1] if i - 1 >= 0 else -1
            for j in range(k):
                if j != a and j != b:
                    CH[i] = j
                    break
        ans = ''.join([chr(x + ord('a')) for x in CH])
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ("abcz", 26, "abda"),
    ("dc", 4, ""),
    ("ced", 6, "cef")
]

aatest_helper.run_test_cases(Solution().smallestBeautifulString, cases)

if __name__ == '__main__':
    pass
