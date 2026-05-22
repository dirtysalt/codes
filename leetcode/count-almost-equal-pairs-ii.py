#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countPairs(self, nums: List[int]) -> int:
        def swap1(x):
            res = set()
            res.add(x)
            x = list(str(x))
            for i in range(len(x)):
                for j in range(i + 1, len(x)):
                    x[i], x[j] = x[j], x[i]
                    res.add(int(''.join(x)))
                    x[i], x[j] = x[j], x[i]
            return res

        def swap2(swp):
            res = set()
            for x in swp:
                res.update(swap1(x))
            return res

        nums.sort(key=lambda x: len(str(x)))

        from collections import defaultdict
        cnt = defaultdict(set)
        cnt2 = defaultdict(set)

        ans = 0
        for i in range(len(nums)):
            x = nums[i]
            res = swap1(x)
            match = set()
            for r in res:
                match.update(cnt[r])
            for r in res:
                cnt[r].add(i)

            res = swap2(res)
            for r in res:
                match.update(cnt2[r])
            cnt2[x].add(i)

            ans += len(match)

        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1023, 2310, 2130, 213], 4),
    ([1, 10, 100], 3),
    ([7440, 9721, 9233, 65, 560, 3386, 6383, 9721, 9844, 3836, 9217, 560, 6392, 650, 9721, 9721, 6833, 6932, 8336, 6005,
      560, 8336, 650, 506, 4948, 65, 3386, 3638, 4539, 9712, 6500, 650, 605, 506, 650, 3836, 6005, 560, 1571], 173),
]

aatest_helper.run_test_cases(Solution().countPairs, cases)

if __name__ == '__main__':
    pass
