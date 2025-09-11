#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class KMP:
    @staticmethod
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

    def __init__(self, t):
        self.t = t
        self.backoff = self.build_backoff(t)

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


class KMP2:
    @staticmethod
    def build_max_match(t):
        n = len(t)
        match = [0] * n
        c = 0
        for i in range(1, n):
            v = t[i]
            while c and t[c] != v:
                c = match[c - 1]
            if t[c] == v:
                c += 1
            match[i] = c
        return match

    def __init__(self, t):
        self.t = t
        self.max_match = self.build_max_match(t)

    def search(self, s):
        match = self.max_match
        t = self.t
        c = 0
        for i, v in enumerate(s):
            while c and t[c] != v:
                c = match[c - 1]
            if t[c] == v:
                c += 1
            if c == len(t):
                return i - len(t) + 1
        return -1


def RunTest(cls):
    pattern = '000001'
    texts = [
        '000000000000000000001',
        '0000000000000002',
        '000001',
        '00001']
    kmp = cls(pattern)
    for s in texts:
        a = kmp.search(s)
        b = s.find(pattern)
        assert (a == b)


if __name__ == '__main__':
    RunTest(KMP)
    RunTest(KMP2)
