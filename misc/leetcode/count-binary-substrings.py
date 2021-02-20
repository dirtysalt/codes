#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        i = 0
        n = len(s)
        exp = '0'
        ans = 0

        while True:
            count = 0
            while i < n and s[i] == exp:
                i += 1
                count += 1
            if i == n:
                break

            next_position = i

            exp = '1' if exp == '0' else '0'
            depth = count
            while i < n and depth > 0 and s[i] == exp:
                i += 1
                depth -= 1

            pairs = (count - depth)
            ans += pairs

            i = next_position

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.countBinarySubstrings('00110011'))
    print(sol.countBinarySubstrings('110011'))
    print(sol.countBinarySubstrings('10111110'))

