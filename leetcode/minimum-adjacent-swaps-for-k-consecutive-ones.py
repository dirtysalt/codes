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

        # 这题首先要证明往中间靠是最优解
        # 之后采用类似滑动窗口办法
        # mid = (k-1) / 2 是最优解

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
        # print(cost)
        for i in range(k, len(arr)):
            # mid -> mid + 1
            it = arr[mid+1] - arr[mid]
            a = (half + 1) * it
            b = (k - half - 1) * it
            # remove (i-k-1) item.
            c = arr[mid+1] - arr[i-k]
            # add (i) item
            d = arr[i] - arr[mid+1]
            cost += (a - b - c + d)
            # print(it, a, b, c, d, cost)
            ans = min(ans, cost)
            mid = mid + 1
        # adjust final cost.
        ans -= saved
        return ans


cases = [
    ([1, 0, 0, 1, 0, 1], 2, 1),
    ([1, 0, 0, 0, 0, 0, 1, 1], 3, 5),
    ([1, 1, 0, 1], 2, 0),
    ([1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1], 2, 0),
    ([0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0], 7, 4)
]

aatest_helper.run_test_cases(Solution().minMoves, cases)
