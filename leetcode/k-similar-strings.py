#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """

        xs = list(A)
        ys = list(B)

        def encode(s):
            val = 0
            for c in s:
                x = ord(c) - ord('a')
                val = val << 3 | x
            return val

        cache = {}

        def walk(i):
            if i == len(xs):
                return 0

            key = encode(xs[i:])
            if key in cache:
                return cache[key]

            if xs[i] == ys[i]:
                res = walk(i + 1)
            else:
                res = 1 << 30
                for j in range(i + 1, len(xs)):
                    if xs[j] == ys[i]:
                        xs[i], xs[j] = xs[j], xs[i]
                        out = walk(i + 1)
                        if (out + 1) < res:
                            res = out + 1
                        xs[i], xs[j] = xs[j], xs[i]
            cache[key] = res
            return res

        res = walk(0)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.kSimilarity('abcdef', 'fcbeda'))
