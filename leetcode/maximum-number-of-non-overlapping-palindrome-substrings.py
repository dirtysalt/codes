#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # O(n^2)
        from collections import defaultdict
        ok = defaultdict(list)

        for i in range(n):
            sz = 0
            while (i - sz) >= 0 and (i + sz) < n:
                if s[i - sz] == s[i + sz]:
                    if (2 * sz + 1) >= k:
                        ok[i - sz].append(i + sz)
                    sz += 1
                else:
                    break

            sz = 0
            while (i - sz) >= 0 and (i + 1 + sz) < n:
                if s[i - sz] == s[i + 1 + sz]:
                    if (2 * sz + 2) >= k:
                        ok[i - sz].append(i + sz + 1)
                    sz += 1
                else:
                    break

        dp = [0] * (n + 1)
        dp[-1] = 0
        for i in range(n):
            dp[i] = max(dp[i], dp[i - 1])
            for j in ok[i]:
                dp[j] = max(dp[j], dp[i - 1] + 1)
        ans = dp[n - 1]
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ("fttfjofpnpfydwdwdnns", 2, 4),
]

aatest_helper.run_test_cases(Solution().maxPalindromes, cases)

if __name__ == '__main__':
    pass
