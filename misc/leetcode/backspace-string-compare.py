#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        n = len(S)
        m = len(T)
        i, j = n - 1, m - 1

        def back(s, i):
            cnt = 0
            while i >= 0:
                if s[i] == '#':
                    cnt += 1
                elif cnt == 0:
                    break
                else:
                    cnt -= 1
                i -= 1
            return i

        while True:
            i = back(S, i)
            j = back(T, j)

            if i >= 0 and j >= 0 and S[i] == T[j]:
                i -= 1
                j -= 1
            elif i < 0 and j < 0:
                break
            else:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.backspaceCompare('ab#c', 'ad#c'))
