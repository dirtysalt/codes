#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:

        def argmax(arr, k):
            i = 0
            for j in range(1, k):
                if arr[j] > arr[i]:
                    i = j
            return i

        A = A[::]
        k = len(A)
        # print('before A = {}, k = {}'.format(A, k))
        res = []
        while k > 1:
            j = argmax(A, k)
            if j != (k - 1):
                res.append(j)
                res.append(k - 1)
                A[0: j + 1] = A[0:j + 1][::-1]
                A[0:k] = A[0:k][::-1]
            k = k - 1
        # print('after A = {}', format(A))
        return [x + 1 for x in res]


def test():
    cases = [
        [3, 2, 4, 1],
    ]
    sol = Solution()
    ok = True
    for c in cases:
        A = c
        res = sol.pancakeSort(A)
        print(res)


if __name__ == '__main__':
    test()
