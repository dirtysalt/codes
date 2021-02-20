#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class State:
    def __init__(self, n, m, data):
        self.n = n
        self.m = m
        self.data = data
        self.sign = None

    def copy(self):
        st = State(self.n, self.m, self.data.copy())
        return st

    def get_sign(self):
        if self.sign is None:
            self.sign = hash(tuple(self.data))
        return self.sign

    def __str__(self):
        return str(self.data)

    def __lt__(self, other):
        # 对象之间没有必要比较
        # 为了实现A*算法实现的
        return True

    @classmethod
    def create(cls, board):
        n = len(board)
        m = len(board[0])
        data = [0] * (n * m)
        for i in range(n):
            for j in range(m):
                data[i * m + j] = board[i][j]
        return State(n, m, data)

    def next_states(self):
        x, y = 0, 0
        n, m = self.n, self.m
        st = self.data

        for i in range(n * m):
            if st[i] == 0:
                x, y = i // m, i % m
                break

        ans = []
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            x2, y2 = x + dx, y + dy
            if 0 <= x2 < n and 0 <= y2 < m:
                st2 = self.copy()
                st2.data[x * m + y] = st2.data[x2 * m + y2]
                st2.data[x2 * m + y2] = 0
                ans.append(st2)

        return ans

    def heap_item(self, now):
        return self.cost() + now, now, self

    def is_final(self):
        if self.data[-1] != 0:
            return False
        n, m = self.n, self.m
        for i in range(n * m - 1):
            if self.data[i] != (i + 1):
                return False
        return True

    def cost(self):
        ans = 0
        n, m = self.n, self.m
        for i in range(n * m):
            dx, dy = i // m, i % m
            if self.data[i] == 0:
                ans += abs(n - 1 - dx) + abs(m - 1 - dy)
            else:
                x, y = (self.data[i] - 1) // m, (self.data[i] - 1) % m
                ans += abs(x - dx) + abs(y - dy)
        return ans


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        st = State.create(board)
        visited = set()

        import heapq
        hp = []
        hp.append(st.heap_item(0))
        visited.add(st.get_sign())

        ans = -1
        while hp:
            (cost, now, st) = heapq.heappop(hp)
            # print(st)
            if st.is_final():
                ans = now
                break

            xs = st.next_states()
            for x in xs:
                sign = x.get_sign()
                if sign in visited:
                    continue
                visited.add(x.get_sign())
                heapq.heappush(hp, x.heap_item(now + 1))

        return ans


cases = [
    ([[1, 2, 3], [4, 0, 5]], 1),
    ([[1, 2, 3], [5, 4, 0]], -1),
    ([[4, 1, 2], [5, 0, 3]], 5),
    ([[3, 2, 4], [1, 5, 0]], 14),
]
import aatest_helper

aatest_helper.run_test_cases(Solution().slidingPuzzle, cases)
