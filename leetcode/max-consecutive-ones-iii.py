#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List

"""
這題目之前想過使用類似二分的方法來查找可以cover的最大範圍。

但是使用二分方法的代碼會非常複雜，所以後面我考慮我是否有更加簡單的辦法。

使用滑动窗口算法就简单很多了。这个题目给我的启发就是，如果一个算法题目实现起来非常复杂的话，
那么很大概率是因为使用了错误的算法。
"""


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        res, cnt, j = 0, 0, 0
        for i in range(n):
            if A[i] == 1:
                cnt += 1
                res = max(res, cnt)
                continue

            K -= 1
            cnt += 1
            while K < 0:
                if A[j] == 0:
                    K += 1
                cnt -= 1
                j += 1
            res = max(res, cnt)
        return res


def test():
    cases = [
        ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6),
        ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3, 10),
    ]
    sol = Solution()
    ok = True
    for c in cases:
        (A, K, exp) = c
        res = sol.longestOnes(A, K)
        if res != exp:
            print('case failed. {}, out = {}'.format(c, res))
            ok = False
    if ok:
        print('cases passed!!!')


if __name__ == '__main__':
    test()
