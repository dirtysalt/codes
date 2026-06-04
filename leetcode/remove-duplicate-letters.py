#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    """
    @param s: a string
    @return: return a string
    """

    def removeDuplicateLetters(self, s):
        # write your code here

        def ch2idx(ch):
            return ord(ch) - ord('a')

        n = len(s)
        dp = [0] * n
        acc = 0
        for si in range(n - 1, -1, -1):
            idx = ch2idx(s[si])
            acc |= (1 << idx)
            dp[si] = acc

        # print(dp)
        res = []
        start = 0
        exp = acc
        while exp:
            next_ch = None
            next_start = None
            for i in range(start, n):
                if ((dp[i] & exp) == exp) and (exp & (1 << ch2idx(s[i]))):
                    ch = s[i]
                    if next_ch is None or ch < next_ch:
                        next_ch = ch
                        next_start = i + 1
            res.append(next_ch)
            start = next_start
            exp -= (1 << ch2idx(next_ch))
        return ''.join(res)


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicateLetters('bcabc'))
    print(sol.removeDuplicateLetters('cbacdcbc'))
    print(sol.removeDuplicateLetters('rpktzsxnwceqrfdtaxxhamsumcutnqmjgmjdnhkwekpoenpezt'))
