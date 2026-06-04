#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        mark = [-1] * 26
        for i, c in enumerate(s):
            idx = ord(c) - ord('a')
            if mark[idx] == -2:  # dup
                continue
            elif mark[idx] == -1:
                mark[idx] = i
            else:
                mark[idx] = -2
        rs = [x for x in mark if x >= 0]
        if not rs:
            return -1
        return min(rs)


def test():
    cases = [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("llcc", -1)
    ]
    sol = Solution()
    ok = True
    for c in cases:
        (s, exp) = c
        res = sol.firstUniqChar(s)
        if res != exp:
            print('case failed. {}, out = {}'.format(c, res))
            ok = False
    if ok:
        print('cases passed!!!')


if __name__ == '__main__':
    test()
