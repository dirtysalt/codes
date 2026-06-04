#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        from collections import deque
        left = deque([0])
        right = 0

        while right < len(nums):
            diff = nums[right] - nums[0]
            if k >= diff:
                right += 1
                k -= diff
            else:
                break

        assert (k >= 0)
        ans = right - left[0]
        for i in range(1, len(nums)):
            move = nums[i] - nums[i - 1]
            k -= len(left) * move
            k += move * (right - i)

            # balance left and right
            while right < len(nums) and left:
                r = nums[right] - nums[i]
                l = nums[i] - nums[left[0]]
                if r <= l:
                    k += l
                    k -= r
                    left.popleft()
                    right += 1
                else:
                    break

            # check k is sastified.
            while k < 0:
                l, r = -1, -1
                if left:
                    l = nums[i] - nums[left[0]]
                if right > i:
                    r = nums[right - 1] - nums[i]
                if (l, r) == (-1, -1): break
                if l >= r:
                    k += l
                    left.popleft()
                else:
                    k += r
                    right -= 1
            assert (k >= 0)

            while k >= 0:
                INF = 1 << 63
                l, r = INF, INF

                idx = i - 1
                if left:
                    idx = left[0] - 1
                if idx >= 0:
                    l = nums[i] - nums[idx]
                if right < len(nums):
                    r = nums[right] - nums[i]
                if (l, r) == (INF, INF): break
                if k < min(l, r): break
                if l >= r:
                    k -= r
                    right += 1
                else:
                    k -= l
                    left.appendleft(idx)

            assert (k >= 0)
            left.append(i)
            size = right - left[0]
            ans = max(ans, size)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 6, 4], 3, 3),
    ([1, 4, 4, 2, 4], 0, 3),
]

aatest_helper.run_test_cases(Solution().maxFrequencyScore, cases)

if __name__ == '__main__':
    pass
