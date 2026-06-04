#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """

        pos = [[] for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, i + 1):
                if i % j == 0:
                    pos[i].append(j)
            for j in range(i + 1, N + 1):
                if j % i == 0:
                    pos[i].append(j)

        st = [-1] * (N + 1)

        def dfs(x):
            if x == (N + 1):
                return 1

            ans = 0
            for p in pos[x]:
                if st[p] == -1:
                    st[p] = x
                    ans += dfs(x + 1)
                    st[p] = -1
            return ans

        ans = dfs(1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.countArrangement(2))
    print(sol.countArrangement(10))
    print(sol.countArrangement(15))
