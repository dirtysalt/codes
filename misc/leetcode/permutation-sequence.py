#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k = k - 1
        seqs = list(range(1, n + 1))
        bases = [1]
        for i in range(2, n):
            bases.append(bases[-1] * i)

        res = []
        for i in range(n - 2, -1, -1):
            idx = k / bases[i]
            k = k % bases[i]
            res.append(seqs[idx])
            seqs.remove(seqs[idx])
        res.append(seqs[0])
        return ''.join(map(str, res))


if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation(3, 3))
