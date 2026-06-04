#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        # arr[0] = pref[0]
        # arr[1]^arr[0] = pref[1] => arr[1] = pref[1] ^ pref[0]
        # arr[2]^arr[1]^arr[0] = pref[2] => arr[2] = pref[2] ^ pref[1]
        n = len(pref)
        ans = [pref[0]]
        for i in range(1, n):
            ans.append(pref[i - 1] ^ pref[i])
        return ans


if __name__ == '__main__':
    pass
