#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import time

import copy


def sudoku_solve(grid, number=0, fast=False):
    # xs[i]表示i行上面可以填写的数字
    N = 9
    xs, ys, rs, ps = [], [], [], []
    for i in range(N):
        mark = [0] * (N + 1)
        for j in range(N):
            mark[grid[i][j]] = 1
        cs = 0
        for k in range(1, N + 1):
            if mark[k] == 0:
                cs |= (1 << k)
        xs.append(cs)

    # ys[i]表示i列上可以填写的数字
    for j in range(N):
        mark = [0] * (N + 1)
        for i in range(N):
            mark[grid[i][j]] = 1
        cs = 0
        for k in range(1, N + 1):
            if mark[k] == 0:
                cs |= (1 << k)
        ys.append(cs)

    # rs[i]表示i块上可以填写的数字
    for i in range(3):
        for j in range(3):
            mark = [0] * (N + 1)
            for k in range(3):
                for l in range(3):
                    v = grid[3 * i + k][3 * j + l]
                    mark[v] = 1
            cs = 0
            for k in range(1, N + 1):
                if mark[k] == 0:
                    cs |= (1 << k)
            rs.append(cs)

    # ps表示所有可能的位置
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                ps.append((i, j))

    ans = []

    # 当前ps[idx]点可以填写的values.
    def choices(idx):
        x, y = ps[idx]
        r = (x // 3) * 3 + (y // 3)
        cs = xs[x] & ys[y] & rs[r]
        values = []
        for v in range(1, 10):
            if (cs >> v) & 0x1:
                values.append(v)
        return values

    # 在ps[idx]上面使用value和取消使用value.
    def use_value(idx, v):
        x, y = ps[idx]
        r = (x // 3) * 3 + (y // 3)
        unmask = ~(1 << v)
        grid[x][y] = v
        xs[x] &= unmask
        ys[y] &= unmask
        rs[r] &= unmask

    def unuse_value(idx, v):
        mask = (1 << v)
        x, y = ps[idx]
        r = (x // 3) * 3 + (y // 3)
        grid[x][y] = 0
        xs[x] |= mask
        ys[y] |= mask
        rs[r] |= mask

    # 简单策略：直接考虑下一个可选点
    class SimpleNextStrategy:
        def __init__(self, ps):
            self.ps_size = len(ps)

        def select_next(self, idx):
            v = idx + 1
            return v

        def should_stop(self, idx):
            return idx == self.ps_size

        def use(self, idx):
            pass

        def unuse(self, idx):
            pass

    # 限制策略：考虑可选数值最少的点
    class RestrictedNextStrategy:
        def __init__(self, ps):
            self.possible_idxs = set(range(len(ps)))

        def select_next(self, idx):
            min_choices = 10
            min_choice_idx = None
            for idx in self.possible_idxs:
                values = choices(idx)
                count = len(values)
                if count < min_choices:
                    min_choices = count
                    min_choice_idx = idx
            return min_choice_idx

        def should_stop(self, idx):
            return idx is None

        def use(self, idx):
            if idx is not None:
                self.possible_idxs.remove(idx)

        def unuse(self, idx):
            if idx is not None:
                self.possible_idxs.add(idx)

    if fast:
        st = RestrictedNextStrategy(ps)
    else:
        st = SimpleNextStrategy(ps)

    def dfs(idx):
        if st.should_stop(idx):
            ans.append(copy.deepcopy(grid))
            return

        values = choices(idx)
        for v in values:
            use_value(idx, v)
            next_idx = st.select_next(idx)
            st.use(next_idx)
            dfs(next_idx)
            st.unuse(next_idx)
            unuse_value(idx, v)

            if ans and len(ans) == number:
                return

    next_idx = st.select_next(-1)
    st.use(next_idx)
    dfs(next_idx)
    st.unuse(next_idx)

    return ans


def find_solution(grid, number=0, fast=False):
    """

    :param grid: 初始布局
    :param number: 希望找到多少个解，0表示所有解
    :param fast:
    :return:
    """
    start = time.time()
    ans = sudoku_solve(grid, number=number, fast=fast)
    stop = time.time()
    print('===== answer(timer: %.2f, total: %s) =====' % (stop - start, len(ans)))
    for arr in ans:
        print('>' * 20)
        for i in range(len(arr)):
            print(arr[i])
        print('<' * 20)


def main():
    number = 0
    grid = [
        [7, 0, 0, 8, 3, 0, 0, 0, 5],
        [0, 2, 5, 0, 6, 0, 3, 0, 0],
        [0, 1, 0, 0, 7, 0, 9, 0, 2],
        [1, 0, 2, 5, 0, 3, 0, 7, 0],
        [5, 0, 8, 0, 0, 6, 4, 0, 0],
        [0, 3, 0, 9, 0, 0, 5, 0, 6],
        [9, 0, 6, 0, 1, 0, 0, 5, 0],
        [0, 0, 4, 0, 9, 0, 6, 1, 0],
        [3, 0, 0, 0, 5, 8, 0, 0, 4]
    ]
    # grid = [
    #     [8, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 3, 6, 0, 0, 0, 0, 0],
    #     [0, 7, 0, 0, 9, 0, 2, 0, 0],
    #     [0, 5, 0, 0, 0, 7, 0, 0, 0],
    #     [0, 0, 0, 0, 4, 0, 7, 0, 0],
    #     [0, 0, 0, 1, 0, 5, 0, 3, 0],
    #     [0, 0, 1, 0, 0, 0, 0, 6, 8],
    #     [0, 0, 8, 5, 0, 0, 0, 1, 0],
    #     [0, 9, 0, 0, 0, 0, 4, 0, 0]
    # ]

    grid = [
        [0, 0, 0, 0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 3, 5, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 7, 0],
        [7, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 4, 0, 0, 8, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 2, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 4, 0],
        [0, 5, 0, 0, 0, 0, 6, 0, 0],
    ]
    number = 1

    # 复杂度比较高的棋盘，来自《算法设计指南》第7章
    # 需要更好的剪枝策略。花费了27s，作者花费了40多分钟
    # 看到我的CPU比他当时写作情况时候好多了，我这个算法
    # 没有很好地选择idx位置。
    """
➜  misc git:(master) ✗ time python sudoku.py
===== answer(27.35, 1) =====
>>>>>>>>>>>>>>>>>>>>
[6, 7, 3, 8, 9, 4, 5, 1, 2]
[9, 1, 2, 7, 3, 5, 4, 8, 6]
[8, 4, 5, 6, 1, 2, 9, 7, 3]
[7, 9, 8, 2, 6, 1, 3, 5, 4]
[5, 2, 6, 4, 7, 3, 8, 9, 1]
[1, 3, 4, 5, 8, 9, 2, 6, 7]
[4, 6, 9, 1, 2, 8, 7, 3, 5]
[2, 8, 7, 3, 5, 6, 1, 4, 9]
[3, 5, 1, 9, 4, 7, 6, 2, 8]
<<<<<<<<<<<<<<<<<<<<
python sudoku.py  26.89s user 0.13s system 98% cpu 27.416 total // 这个是使用SimpleNextStrategy的时间
python sudoku.py  0.97s user 0.04s system 95% cpu 1.059 total // 这个是使用RestrictedNextStrategy的时间
"""

    find_solution(grid, number, fast=True)


if __name__ == '__main__':
    main()
