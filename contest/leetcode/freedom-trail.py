#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """

        n = len(ring)
        m = len(key)
        dp = [[0] * n, [0] * n]
        now = 0
        for i in range(n):
            dp[now][i] = i

        for i in range(m):
            for j in range(n):
                res = 1 << 30
                match = False

                for step in range(0, n):
                    k = (j + step) % n
                    if ring[k] == key[i]:
                        match = True
                    if match:
                        res = min(res, dp[now][k] + step)

                match = False
                for step in range(0, n):
                    k = (j + n - step) % n
                    if ring[k] == key[i]:
                        match = True
                    if match:
                        res = min(res, dp[now][k] + step)

                dp[1 - now][j] = res
            now = 1 - now

        ans = min(dp[now]) + m
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.findRotateSteps('godding', 'gd'))
    print(sol.findRotateSteps(
        "sqlfcudiojjzmdmvbqgtkudggbazwtqgzrbxlooxcfnvzkvyvrroakdhnwcfyzyefiuatefegiragiqdrggictalanfupkuvjyid",
        "jogduakfgovnolkbjwelatfgfunqgvajvwtrzguyydiqaucqrzzcuhxcpkilfebqyytaxikigemzatzgmcdbodriddnrvgffsriv"))
