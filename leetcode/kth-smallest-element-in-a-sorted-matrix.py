#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    """
    @param matrix: List[List[int]]
    @param k: a integer
    @return: return a integer
    """

    def kthSmallest(self, matrix, k):
        # write your code here

        n = len(matrix)
        m = len(matrix[0])

        def find_order(r, c):
            low = c
            high = low

            for i in range(r + 1, n):
                if matrix[r][c] < matrix[i][0]:
                    break
                a = locate_le(matrix[i], matrix[r][c])
                b = locate_ge(matrix[i], matrix[r][c])
                low += a
                high += b
            for i in range(r - 1, -1, -1):
                if matrix[r][c] > matrix[i][-1]:
                    delta = (i + 1) * m
                    low += delta
                    high += delta
                    break
                a = locate_le(matrix[i], matrix[r][c])
                b = locate_ge(matrix[i], matrix[r][c])
                low += a
                high += b
            return low, high

        def locate_le(xs, a):
            s, e = 0, len(xs) - 1
            while s <= e:
                m = (s + e) // 2
                if xs[m] >= a:
                    e = m - 1
                else:
                    s = m + 1
            return e + 1

        def locate_ge(xs, a):
            s, e = 0, len(xs) - 1
            while s <= e:
                m = (s + e) // 2
                if xs[m] > a:
                    e = m - 1
                else:
                    s = m + 1
            return s

        r, c = 0, m - 1
        while True:
            low, high = find_order(r, c)
            low += 1
            high += 1
            print(r, c, matrix[r][c], low, high)
            if low <= k <= high:
                return matrix[r][c]
            elif k > high:
                r = r + 1
            else:
                c = c - 1
        return None
