#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0: return 0
        n -= 1
        if n <= 1: return 0
        if n == 2: return 1

        primes = [1] * (n + 1)
        for i in range(2, int(round(n ** 0.5)) + 2):
            for j in range(i, n // i + 1):
                primes[i * j] = 0

        count = 1
        for i in range(3, n + 1):
            if primes[i] == 1:
                count += 1
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.countPrimes(1500000))
