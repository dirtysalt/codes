import aatest_helper
from typing import List


class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        arr = []
        for i in range(len(nums)):
            if nums[i] == 1:
                arr.append(i)

        if k == 1:
            return 0

        # initialize cost.
        half = mid = k // 2
        cost = 0
        for i in range(k):
            p0 = arr[mid]
            p1 = arr[i]
            cost += abs(p0 - p1)
        # note: move all around 1 to mid.
        saved = 0
        for i in range(mid):
            saved += (mid - i)
        for i in range(mid+1, k):
            saved += (i - mid)

        ans = cost
        for i in range(k, len(arr)):
            # mid -> mid + 1
            d = arr[mid+1] - arr[mid]
            cost += (half + 1) * d
            cost -= (k - half - 1) * d
            # remove (i-k-1) item.
            d = arr[mid+1] - arr[i-k]
            cost -= d
            d = arr[i] - arr[mid+1]
            cost += d
            ans = min(ans, cost)

        # adjust final cost.
        ans -= saved
        return ans


cases = [
    ([1, 0, 0, 1, 0, 1], 2, 1),
    ([1, 0, 0, 0, 0, 0, 1, 1], 3, 5),
    ([1, 1, 0, 1], 2, 0),
    ([1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1], 2, 0)
]

aatest_helper.run_test_cases(Solution().minMoves, cases)
