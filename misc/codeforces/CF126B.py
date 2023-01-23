#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class HelperHandler:
    import sys, os
    stdin = sys.stdin
    debug = False
    if os.path.exists('../leetcode/tmp.in'):
        stdin = open('../leetcode/tmp.in')
        debug = True

    def readInt(self):
        return int(self.stdin.readline())

    def readIntArray(self, sep=None):
        return [int(x) for x in self.stdin.readline().split(sep)]

    def readStringArray(self, sep=None):
        return [x.strip() for x in self.stdin.readline().split(sep)]

    def D(self, *args):
        if self.debug:
            print(*args)


# this is codeforces main function
def main():
    hh = HelperHandler()

    # helper.isDebug = False
    def func(s):
        n = len(s)
        z = [0] * len(s)
        l, r = 0, 0
        for i in range(1, n):
            if i <= r and z[i - l] < (r - i + 1):
                z[i] = z[i - l]
            else:
                z[i] = max(0, r - i + 1)
                while (i + z[i]) < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
            if (i + z[i] - 1) > r:
                l, r = i, i + z[i] - 1

        hh.D(z)

        left = [0] * n
        for i in range(1, n):
            left[i] = max(left[i - 1], z[i])

        size = 0
        for j in reversed(range(1, n)):
            if j + z[j] != n:
                continue
            if z[j] > left[j - 1]:
                break
            size = max(size, z[j])

        if size == 0:
            print('Just a legend')
        else:
            print(s[:size])

    for s in hh.stdin:
        s = s.strip()
        hh.D('>>>', s)
        func(s)


if __name__ == '__main__':
    main()
