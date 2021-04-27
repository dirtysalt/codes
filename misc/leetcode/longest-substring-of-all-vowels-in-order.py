#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        mapp = {'a':0, 'e':1, 'i': 2, 'o':3, 'u':4}
        nums = [mapp[x] for x in word]
        ans = 0

        sz = 1
        cnt = [0] * 5
        cnt[nums[0]] += 1
        for i in range(1, len(nums)):
            if nums[i] >= nums[i-1]:
                sz += 1
            else:
                if (all(x > 0 for x in cnt)):
                    ans = max(sz, ans)
                cnt = [0] * 5
                sz = 1
            cnt[nums[i]] += 1
        if (all(x > 0 for x in cnt)):
            ans = max(ans, sz)
        return ans

cases = [
    ("aeiaaioaaaaeiiiiouuuooaauuaeiu", 13),
    ("aeeeiiiioooauuuaeiou", 5),
    ("a", 0),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().longestBeautifulSubstring, cases)

if __name__ == '__main__':
    pass
