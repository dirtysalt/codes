#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        # sort by alphabetical order
        nums.sort()
        n = len(nums)

        # how many digits are there in state
        digits = [0] * (1 << n)
        for i in range((1 << n)):
            for j in range(n):
                if i & (1 << j):
                    digits[i] = len(str(nums[j])) + digits[i ^ (1 << j)]
                    break

        # pow(10, x) % k
        total_digit = digits[-1]
        pow10 = [0] * (1 + total_digit)
        x = 1
        for i in range(len(pow10)):
            pow10[i] = x
            x = (x * 10) % k

        # print(digits, pow10)
        def iter_bit_positions_fast(n):
            """Yield positions of set bits using bit tricks."""
            while n:
                lsb = n & -n
                yield lsb.bit_length() - 1
                n &= n - 1  # 清除最低的1-bit

        import functools
        @functools.cache
        def search(st, rem):
            if st == 0:
                return [] if rem == 0 else None
            for i in iter_bit_positions_fast(st):
                d = digits[st ^ (1 << i)]
                rem2 = (rem + nums[i] * pow10[d]) % k
                tail = search(st ^ (1 << i), rem2)
                if tail is None: continue
                r = [nums[i]] + tail
                return r

        ans = search((1 << n) - 1, 0)
        if ans is None: ans = []
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([3, 12, 45], 5, [3, 12, 45]),
    ([10, 5], 10, [5, 10]),
    ([1, 2, 3], 5, []),
    ([2286, 1889, 3134, 3377, 4611, 4959, 143, 374, 1180, 3994], 6,
     [143, 374, 1180, 1889, 2286, 3134, 3377, 4611, 4959, 3994]),
    ([25900, 39695, 2584, 18305, 75986, 79563, 56939, 36282, 89720, 16517, 28547, 24732], 57, []),
]

aatest_helper.run_test_cases(Solution().concatenatedDivisibility, cases)

if __name__ == '__main__':
    pass
