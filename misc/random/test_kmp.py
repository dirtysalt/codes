#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def build_backoff(t):
    n = len(t)
    backoff = [-1] * n
    j = -1
    for i in range(1, n):
        # backoff[i] = j+1 means t[..i-1] == t[..j], but t[i] may not be equal to t[j+1]

        # so if t[..i] not match s[..k] but t[..i-1] matches s[..k-1]
        # t[..i-1] == t[..j] == s[..k-1], try t[..j+1] matches s[..k]
        # since t[i] may not be euqal to t[j+1], so t[j+1] maybe equal to s[k]
        while j >= 0 and t[i - 1] != t[j]:
            j = backoff[j]
        backoff[i] = j + 1
        j += 1
    return backoff


class KMP:
    def __init__(self, t):
        self.t = t
        self.backoff = build_backoff(t)

    def search(self, s):
        backoff = self.backoff
        t = self.t
        j = 0
        for i in range(len(s)):
            while j >= 0 and s[i] != t[j]:
                j = backoff[j]
            j += 1
            if j == len(t):
                return i - len(t) + 1
        return -1


if __name__ == '__main__':
    kmp = KMP('000001')
    print(kmp.t)
    print(kmp.backoff)

    s = '000000000000000000001'
    print(kmp.search(s), s.find(kmp.t))
    s = '0000000000000002'
    print(kmp.search(s), s.find(kmp.t))
    s = '000001'
    print(kmp.search(s), s.find(kmp.t))
    s = '00001'
    print(kmp.search(s), s.find(kmp.t))
