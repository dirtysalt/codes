#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        bucket = [0] * batchSize
        for g in groups:
            bucket[g % batchSize] += 1

        ans = 0

        # 快速地计算某些可以匹配的组
        ans += bucket[0]
        bucket[0] = 0

        i, j = 1, batchSize - 1
        while i < j:
            x = min(bucket[i], bucket[j])
            bucket[i] -= x
            bucket[j] -= x
            i += 1
            j -= 1
            ans += x

        if batchSize % 2 == 0:
            mid = batchSize // 2
            x = bucket[mid] // 2
            ans += x
            bucket[mid] -= 2 * x


        import functools
        @functools.lru_cache(maxsize = None)
        def query(x, index, st):
            if x != batchSize and index == bucket[x]:
                x += 1
                while x < batchSize and bucket[x] == 0:
                    x += 1
                index = 0

            if x == batchSize:
                ans = st[0]
                # 如果最后面多出的话，是需要额外计算一组的
                for i in range(1, batchSize):
                    if st[i] != 0:
                        ans += 1
                        break
                return ans

            ans = 0
            for i in range(1, batchSize):
                if st[i] > 0:
                    y = (i + x) % batchSize
                    st2 = list(st)
                    st2[y] += 1
                    st2[i] -= 1
                    res = query(x, index + 1, tuple(st2))
                    ans = max(ans, res)

            st2 = list(st)
            st2[x] += 1
            res = query(x, index + 1, tuple(st2))
            ans = max(ans, res)
            return ans

        # print(ans, bucket)
        st = [0] * batchSize
        res = query(1, 0, tuple(st))
        ans += res
        return ans

cases = [
    (3, [1,2,3,4,5,6], 4),
    (4, [1,3,2,5,2,2,1,6], 4),
    (1,
[909925048,861425549,820096754,67760437,273878288,126614243,531969375,817077202,482637353,507069465,699642631,407608742,846885254,225437260,100780964,523832097,30437867,959191866,897395949],19),
(2,
[652231582,818492002,823729239,2261354,747144855,478230860,285970257,774747712,860954510,245631565,634746161,109765576,967900367,340837477,32845752,23968185],12)
]

import aatest_helper
aatest_helper.run_test_cases(Solution().maxHappyGroups, cases)




if __name__ == '__main__':
    pass
