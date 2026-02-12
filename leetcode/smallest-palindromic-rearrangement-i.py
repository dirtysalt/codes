#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1

        ans = ''
        for i in range(26):
            if cnt[i] % 2 == 1:
                ans += chr(i + ord('a'))
                cnt[i] -= 1
                break

        for i in reversed(range(26)):
            prefix = chr(i + ord('a')) * (cnt[i] // 2)
            ans = prefix + ans + prefix
        return ans


if __name__ == '__main__':
    pass
