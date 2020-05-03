#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import Counter


class Solution:
    """
    @param nums: a list of integers
    @return: return a boolean
    """

    def isPossible(self, nums):
        # write your code here

        counter = Counter()
        for v in nums:
            counter[v] += 1

        def is_good_range(r):
            return (r[1] - r[0] + 1) >= 3

        def update_range(r, r2):
            if r is None:
                if not is_good_range(r2):
                    return False, None
                return True, r2

            s, e = r
            s2, e2 = r2
            assert s <= s2
            # not overlapped.
            if s2 > e:
                if not is_good_range(r2):
                    return False, None
                return True, r2

            # overlapped.
            assert e2 <= e
            if is_good_range((s, e2)) and is_good_range((s2, e)):
                return True, (s2, e)
            return False, None

        values = list(counter.keys())
        values.sort()
        prev_range = None
        for value in values:
            if counter[value] == 0:
                continue
            start = value
            stop = value
            while counter[stop] >= 1:
                counter[stop] -= 1
                stop += 1
            stop -= 1
            now_range = (start, stop)
            ok, prev_range = update_range(prev_range, now_range)
            if not ok:
                return False
        return True
