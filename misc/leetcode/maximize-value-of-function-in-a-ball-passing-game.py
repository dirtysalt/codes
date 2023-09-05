#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        n = len(receiver)
        parent = [[] for _ in range(n)]
        for i in range(n):
            x = receiver[i]
            parent[x].append(i)

        def findRoot():
            root = []
            visited = set()
            for i in range(n):
                loop = set()
                while i not in visited:
                    visited.add(i)
                    loop.add(i)
                    i = receiver[i]
                if i in loop:
                    root.append(i)
            return root

        class State:
            def __init__(self, loop, k):
                self.loop = loop
                self.history = []

                rep = k // len(self.loop)
                rem = k % len(self.loop)
                self.value = sum(self.loop) * rep
                self.value += sum(self.loop[:rem])
                self.loopIdx = (k - 1 + len(self.loop)) % len(self.loop)
                self.loopK = k
                self.hisIdx = -1

            def push(self, x):
                self.history.append(x)
                saved = (self.loopIdx, self.loopK, self.hisIdx, self.value)

                self.value += x
                if self.hisIdx != -1:
                    self.value -= self.history[self.hisIdx]
                    self.hisIdx += 1
                else:
                    self.value -= self.loop[self.loopIdx]
                    self.loopIdx -= 1
                    self.loopK -= 1
                    if self.loopIdx < 0 and self.loopK > 0:
                        self.loopIdx += len(self.loop)
                    if self.loopK == 0:
                        self.hisIdx = 0
                return saved

            def pop(self, saved):
                self.loopIdx, self.loopK, self.hisIdx, self.value = saved
                self.history.pop()

        root = findRoot()
        ans = [-1] * n

        def visitRoot(r):
            loop = []
            visit = set()
            x = r
            while x not in visit:
                loop.append(x)
                visit.add(x)
                x = receiver[x]
            st = State(loop, k + 1)

            def dfs(r, st: State):
                ans[r] = st.value
                for p in parent[r]:
                    if ans[p] == -1:
                        saved = st.push(p)
                        dfs(p, st)
                        st.pop(saved)

            dfs(r, st)

        for r in root:
            visitRoot(r)
        # print(ans)
        return max(ans)


class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        n = len(receiver)
        N = 36

        f = [[-1] * N for _ in range(n)]
        w = [[-1] * N for _ in range(n)]
        for i in range(n):
            x = receiver[i]
            f[i][0] = x
            w[i][0] = x

        for j in range(1, N):
            for i in range(n):
                f[i][j] = f[f[i][j - 1]][j - 1]
                w[i][j] = w[i][j - 1] + w[f[i][j - 1]][j - 1]

        ans = 0
        for i in range(n):
            c = i
            x = i
            for j in range(N):
                if k & (1 << j):
                    y = f[x][j]
                    c += w[x][j]
                    x = y
            ans = max(ans, c)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([2, 0, 1], 4, 6),
    ([1, 1, 1, 2, 3], 3, 10),
    ([0, 0, 0], 1, 2),
]

aatest_helper.run_test_cases(Solution().getMaxFunctionValue, cases)

if __name__ == '__main__':
    pass
