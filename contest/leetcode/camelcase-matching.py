#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def decompose(s):
            res = []
            last = '$'
            for c in s:
                if c.isupper():
                    res.append(last)
                    last = c
                else:
                    last = last + c
            res.append(last)
            res = [x for x in res if x]
            return res

        def is_matched(a, b):
            if len(a) != len(b):
                return False
            for k in range(len(a)):
                if a[k][0] != b[k][0]:
                    return False

                i, j = 1, 1
                while i < len(a[k]) and j < len(b[k]):
                    if a[k][i] == b[k][j]:
                        i += 1
                        j += 1
                    else:
                        j += 1
                if i != len(a[k]):
                    return False
            return True

        res = []
        ps = decompose(pattern)
        for q in queries:
            qs = decompose(q)
            v = is_matched(ps, qs)
            # print(ps, qs, v)
            res.append(v)
        return res


def test():
    true = True
    false = False
    cases = [
        (["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], "FB", [true, false, true, true, false]),
        (
            ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], "FoBa",
            [true, false, true, false, false]),
        (["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], "FoBaT",
         [false, true, false, false, false]),
        (["aksvbjLiknuTzqon", "ksvjLimflkpnTzqn", "mmkasvjLiknTxzqn", "ksvjLiurknTzzqbn", "ksvsjLctikgnTzqn",
          "knzsvzjLiknTszqn"],
         "ksvjLiknTzqn", [true, true, true, true, true, true])
    ]
    sol = Solution()
    ok = True
    for c in cases:
        (queries, pattern, exp) = c
        res = sol.camelMatch(queries, pattern)
        if res != exp:
            print('case failed. {}, out = {}'.format(c, res))
            ok = False
    if ok:
        print('cases passed!!!')


if __name__ == '__main__':
    test()
