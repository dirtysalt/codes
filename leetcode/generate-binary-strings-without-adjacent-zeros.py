#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []

        def dfs(i, now):
            if i == n:
                ans.append(''.join(now))
                return

            if not now or now[-1] == '1':
                now.append('0')
                dfs(i + 1, now)
                now.pop()

                now.append('1')
                dfs(i + 1, now)
                now.pop()

            else:
                now.append('1')
                dfs(i + 1, now)
                now.pop()

        dfs(0, [])
        return ans


if __name__ == '__main__':
    pass
