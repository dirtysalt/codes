#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        groups = ('qwertyuiop', 'asdffghjkl', 'zxcvbnm')

        mapping = [0] * 26
        for i in range(len(groups)):
            for c in groups[i]:
                mapping[ord(c) - ord('a')] = i

        def ok_to_type(s):
            s = s.lower()
            row = None
            for c in s:
                idx = ord(c) - ord('a')
                value = mapping[idx]
                if row is not None and row != value:
                    return False
                row = value
            return True

        res = [s for s in words if ok_to_type(s)]
        return res


def test():
    cases = [
        (["Hello", "Alaska", "Dad", "Peace"], ["Alaska", "Dad"])
    ]
    sol = Solution()
    ok = True
    for c in cases:
        (words, exp) = c
        res = sol.findWords(words)
        if res != exp:
            print('case failed. {}, out = {}'.format(c, res))
            ok = False
    if ok:
        print('cases passed!!!')


if __name__ == '__main__':
    test()
