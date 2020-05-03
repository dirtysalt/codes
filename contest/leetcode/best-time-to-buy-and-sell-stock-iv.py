#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# note(yan): 这个题目的测试样例可以n可以到达10^4. 所以如果时间复杂度是O(n^2)的话还是有问题的，虽然下面算法可以正常运行
#  dp[i][j]表示到ith位置上完成j次交易的最大值。j % 2==0表示本次操作是买入(max)，j % 2 ==0表示本次操作是卖出(min)

class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        n = len(prices)
        k = min(k, n // 2)
        dp = []
        for i in range(n + 1):
            dp.append([None] * (2 * k + 1))
        dp[0][0] = 0

        def update(i, j, v, fn):
            if v is None:
                return

            if dp[i][j] is None:
                dp[i][j] = v

            dp[i][j] = max(dp[i][j], v)

        for i in range(1, n + 1):
            p = prices[i - 1]

            # dp[i][j]: dp[i-1][j], dp[i-1][j-1]
            for j in range(0, min(i + 1, 2 * k + 1)):
                fn = max if j % 2 == 0 else min

                update(i, j, dp[i - 1][j], fn)

                if j > 0 and dp[i - 1][j - 1] is not None:
                    x = dp[i - 1][j - 1]
                    if j % 2 == 0:
                        x = x + p
                    else:
                        x = x - p
                    update(i, j, x, fn)

        # for x in dp:
        #     print(x)
        ans = 0
        for v in dp[n]:
            if v is not None:
                ans = max(ans, v)
        return ans


cases = [
    (2, [2, 4, 1], 2,),
    (2, [3, 2, 6, 5, 0, 3], 7),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxProfit, cases)
