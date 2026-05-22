#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def test2(s, k):
            op = 0
            cnt = 0
            val = s[0]
            for i in range(len(s)):
                if s[i] != val:
                    val = s[i]
                    cnt = 1
                    continue
                cnt += 1
                if cnt > k:
                    op += 1
                    cnt = 1
                    if (i + 1) < len(s):
                        val = 1 - s[i + 1]
            return op <= numOps

        def test1(s):
            op = 0
            val = s[0]
            for i in range(1, len(s)):
                exp = 1 - val
                if s[i] != exp:
                    op += 1
                val = exp
            if op <= numOps: return True

            val = 1 - s[0]
            op = 1
            for i in range(1, len(s)):
                exp = 1 - val
                if s[i] != exp:
                    op += 1
                val = exp
            if op <= numOps: return True
            return False

        def test(s, k):
            if k >= 2:
                return test2(s, k)
            return test1(s)

        nums = [int(x) for x in s]
        s, e = 1, len(nums)
        while s <= e:
            m = (s + e) // 2
            ok = test(nums, m)
            if ok:
                e = m - 1
            else:
                s = m + 1
        return s


if __name__ == '__main__':
    pass
