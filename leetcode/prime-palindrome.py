#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def is_palindrome(x):
    s = str(x)
    return s == s[::-1]


def next_palindrome(x):
    def _find(x):
        while True:
            if is_palindrome(x):
                return x
            ds = list(str(x))
            n = len(ds)
            s, e = 0, n - 1
            carry = 0
            while s <= e:
                if ds[s] > ds[e]:
                    ds[e] = ds[s]
                elif ds[s] < ds[e]:
                    carry = ord('9') - ord(ds[e]) + 1
                    carry *= (10 ** s)
                    break
                s += 1
                e -= 1
            x = int(''.join(ds))
            x += carry

    if is_palindrome(x):
        x = _find(x + 1)
    else:
        x = _find(x)
    return x


def prime_upper_bound(n):
    return min(n - 1, round(n ** 0.5) + 2)


def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    ub = prime_upper_bound(n)
    for i in range(2, ub):
        if n % i == 0:
            return False
    return True


class Solution:
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        n = N - 1
        while True:
            n = next_palindrome(n)
            if is_prime(n):
                return n


if __name__ == '__main__':
    s = Solution()
    print(s.primePalindrome(20))
    print(s.primePalindrome(23))
    print(s.primePalindrome(33))
    print(s.primePalindrome(99))
    print(s.primePalindrome(9933))
    print(s.primePalindrome(9999))
    print(next_palindrome(85709140))
    print(s.primePalindrome(85709140))
    print(s.primePalindrome(10 ** 8))
