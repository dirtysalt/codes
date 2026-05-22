#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        def compress(s):
            last = s[0]
            count = 1
            res = []
            for c in s[1:]:
                if c == last:
                    count += 1
                else:
                    res.append((last, count))
                    last = c
                    count = 1
            return res

        a = compress(name)
        b = compress(typed)
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            (c0, v0) = a[i]
            (c1, v1) = b[i]
            if c0 != c1 or v0 > v1:
                return False
        return True


def test():
    cases = [
        ("alex", "aaleex", True),
        ('saeed', 'ssaaedd', False),
        ('leelee', 'lleeelee', True),
        ('laiden', 'laiden', True)
    ]
    sol = Solution()
    ok = True
    for c in cases:
        (a, b, exp) = c
        res = sol.isLongPressedName(a, b)
        if res != exp:
            print('case failed. {}, out = {}'.format(c, res))
            ok = False
    if ok:
        print('cases passed!!!')


if __name__ == '__main__':
    test()
