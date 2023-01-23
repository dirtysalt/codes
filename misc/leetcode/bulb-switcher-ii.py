#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

"""
这题目可以通过枚举状态来完成. 另外操作是有交换律和结合律的，也就是14 = 41
另外141 = 411 = 4. 分别考虑0, 1, 2 > 2这几种可能的状态

m = 0 ，状态只有0(表示不变)
m = 1, 状态有1,2,3,4
m = 2, 在状态1,2,3,4上结合
    1  2  3  4
1   0  3 2   14
2      0  1  24
3        0   34
4            0
可以看到有 0, 1, 2, 3, 14, 24, 34(最后面3个状态没有办法简化)

m =3 在这个m=2上继续，可以看到只有状态4增加了。并且可以确认之后不会增加更多的状态了。

然后我们枚举所有这几种可能的变换，看最终有多少个状态
"""


class Solution:
    def flipLights(self, n: int, m: int) -> int:
        def m0(st):
            return tuple(st)

        def m1(st):
            return tuple((1 - x for x in st))

        def m2(st):
            return tuple((1 - x if i % 2 == 0 else x for (i, x) in enumerate(st)))

        def m3(st):
            return tuple((1 - x if i % 2 == 1 else x for (i, x) in enumerate(st)))

        def m4(st):
            return tuple((1 - x if i % 3 == 0 else x for (i, x) in enumerate(st)))

        def m14(st):
            return m1(m4(st))

        def m24(st):
            return m2(m4(st))

        def m34(st):
            return m3(m4(st))

        if m == 0:
            actions = [m0]
        elif m == 1:
            actions = [m1, m2, m3, m4]
        elif m == 2:
            actions = [m0, m1, m2, m3, m14, m24, m34]
        else:
            actions = [m0, m1, m2, m3, m4, m14, m24, m34]

        st = tuple([1] * n)
        res = set()
        for action in actions:
            st2 = action(st)
            res.add(st2)

        print(res)
        return len(res)


def test():
    cases = [
        (1, 1, 2),
        (3, 1, 4),
        (3, 2, 7),
        (30, 2, 7),
        (1000, 1000, 8)
    ]
    sol = Solution()
    ok = True
    for c in cases:
        (n, m, exp) = c
        res = sol.flipLights(n, m)
        if res != exp:
            print('case failed. {}, out = {}'.format(c, res))
            ok = False
    if ok:
        print('cases passed!!!')


if __name__ == '__main__':
    test()
