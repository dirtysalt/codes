#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import time
from collections import deque

import numpy as np


class State:
    def __init__(self, matrix, xy=None):
        if not isinstance(matrix, np.ndarray):
            matrix = np.array(matrix)
        self.matrix = matrix
        self.nm = matrix.shape
        self.xy = xy
        self.str_cache = None
        self.id_cache = None
        if xy is None:
            self.xy = self.find_zero()

    def find_zero(self):
        matrix = self.matrix
        n, m = self.nm
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    return i, j

    def next_states(self):
        matrix = self.matrix
        x, y = self.xy
        n, m = self.nm
        states = []
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            x2, y2 = x + dx, y + dy
            if 0 <= x2 < n and 0 <= y2 < m:
                matrix2 = np.copy(matrix)
                matrix2[x2][y2], matrix2[x][y] = matrix2[x][y], matrix2[x2][y2]
                state2 = State(matrix2, (x2, y2))
                states.append(state2)
        return states

    def __str__(self):
        return self.to_string()

    def is_equal(self, other):
        return self.xy == other.xy and self.identity() == other.identity()

    def identity(self):
        return self.matrix.tobytes()

    def to_string(self):
        if self.str_cache is not None:
            return self.str_cache
        self.str_cache = str(self.matrix)
        return self.str_cache


class StateBK:
    def __init__(self):
        self.map = {}
        self.seq = []

    def get_index(self, st: State):
        if st.identity() in self.map:
            return self.map[st.identity()]
        index = len(self.seq)
        self.map[st.identity()] = index
        self.seq.append(st)
        return index

    def query_index(self, st: State):
        return st.identity() in self.map

    def get_state(self, index):
        return self.seq[index]


def print_paths(paths):
    for p in paths:
        print('-----')
        print(p)


# naive BFS
def search_path_1(source: State, dest: State):
    bk = StateBK()
    parents = {}
    Q = deque()

    idx = bk.get_index(source)
    parents[idx] = -1
    Q.append(idx)

    paths = []
    found = False
    while len(Q):
        idx = Q.popleft()
        state = bk.get_state(idx)
        if state.is_equal(dest):
            found = True
            break
        next_states = state.next_states()
        for st in next_states:
            if bk.query_index(st):
                continue
            idx2 = bk.get_index(st)
            parents[idx2] = idx
            Q.append(idx2)

    if found:
        idx = bk.get_index(dest)
        while idx != -1:
            paths.append(bk.get_state(idx))
            idx = parents[idx]
        paths = paths[::-1]
    return paths


# bidirectional BFS
def search_path_2(source: State, dest: State):
    bk = [StateBK(), StateBK()]
    parents = [{}, {}]
    dists = [{}, {}]
    Q = [deque(), deque()]

    idx = bk[0].get_index(source)
    parents[0][idx] = -1
    dists[0][idx] = 0
    Q[0].append((idx, 0))

    idx = bk[1].get_index(dest)
    parents[1][idx] = -1
    dists[1][idx] = 0
    Q[1].append((idx, 0))

    depth = -1
    found = False

    # distance, pidx0, pidx1, direction
    opt = (1 << 30, None, None, 0)

    while True:
        depth += 1
        for i in range(2):
            while len(Q[i]):
                idx, d = Q[i].popleft()
                if d != depth:
                    Q[i].append((idx, d))
                    break

                state = bk[i].get_state(idx)
                if bk[1 - i].query_index(state):
                    pidx0 = idx
                    pidx1 = bk[1 - i].get_index(state)
                    dist = dists[i][pidx0] + dists[1 - i][pidx1]
                    if dist < opt[0]:
                        # print('min dist = {}, i = {}'.format(dist, i))
                        opt = (dist, pidx0, pidx1, i)
                        found = True
                        break

                next_states = state.next_states()
                for st in next_states:
                    if bk[i].query_index(st):
                        continue
                    idx2 = bk[i].get_index(st)
                    parents[i][idx2] = idx
                    dists[i][idx2] = d + 1
                    Q[i].append((idx2, d + 1))
            if found: break
        if found or not len(Q[0]) or not len(Q[1]):
            break

    if not found:
        return []

    dist, pidx0, pidx1, i = opt
    paths0 = []
    while pidx0 != -1:
        paths0.append(bk[i].get_state(pidx0))
        pidx0 = parents[i][pidx0]

    paths1 = []
    while pidx1 != -1:
        paths1.append(bk[1 - i].get_state(pidx1))
        pidx1 = parents[1 - i][pidx1]

    assert len(paths0) > 0
    assert len(paths1) > 0
    paths = paths0[::-1] + paths1[1:]
    if i: paths = paths[::-1]
    return paths


def test_case(source_matrix):
    print('==============================')
    print('source_matrix = {}'.format(source_matrix))
    dest_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    source = State(source_matrix)
    dest = State(dest_matrix)

    start = time.time()
    paths1 = search_path_1(source, dest)
    print('naive BFS ...')
    # print_paths(paths1)
    print('size = {}'.format(len(paths1)))
    end = time.time()
    print('timer = {}'.format(end - start))

    start = time.time()
    paths2 = search_path_2(source, dest)
    print('bidirectional BFS ...')
    # print_paths(paths2)
    print('size = {}'.format(len(paths2)))
    end = time.time()
    print('timer = {}'.format(end - start))

def main():
    # simple one
    source_matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    test_case(source_matrix)

    # http://w01fe.com/blog/2009/01/the-hardest-eight-puzzle-instances-take-31-moves-to-solve/
    # hard one.
    source_matrix = [[8, 6, 7], [2, 5, 4], [3, 0, 1]]
    test_case(source_matrix)

    source_matrix = [[6,4,7], [8,5,0],[3,2,1]]
    test_case(source_matrix)

if __name__ == '__main__':
    main()
