#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        n = len(S)

        INT_MAX = (1 << 31) - 1

        def find(a, b, s):
            res = []
            ok = False
            v = 0

            for i in range(s, n):
                v = v * 10 + ord(S[i]) - ord('0')
                if v > INT_MAX or v > (a + b):
                    break

                if v == (a + b):
                    res.append(v)
                    a, b = (b, v)
                    v = 0
                    if (i + 1) == n:
                        ok = True

                elif v == 0:
                    break

            # print(a, b, S[s:])
            return ok, res

        a = 0
        ans = []
        for i in range(n):
            a = a * 10 + ord(S[i]) - ord('0')
            if a > INT_MAX: break
            b = 0
            for j in range(i + 1, n):
                b = b * 10 + ord(S[j]) - ord('0')
                if b > INT_MAX: break
                ok, res = find(a, b, j + 1)
                if ok:
                    ans = [a, b]
                    ans.extend(res)
                    break
                if b == 0: break

            if ans:
                break
            if a == 0: break

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.splitIntoFibonacci("11235813"))
    print(sol.splitIntoFibonacci("1101111"))
    print(sol.splitIntoFibonacci(
        "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"))
    print(sol.splitIntoFibonacci(
        "417420815174208193484163452262453871040871393665402264706273658371675923077949581449611550452755"))
