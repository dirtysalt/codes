#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


# def solve(n, xs, k):
#     s, e = 0, n - 1
#     while s != e:
#         pivot = xs[s]
#         a, b = s, e
#         while True:
#             while a < b and xs[b] > pivot:
#                 b -= 1
#             if a == b:
#                 break
#             xs[a] = xs[b]
#             a += 1
#             while a < b and xs[a] < pivot:
#                 a += 1
#             if a == b:
#                 break
#             xs[b] = xs[a]
#             b -= 1
#             if a == b:
#                 break
#         assert a == b
#         xs[a] = pivot
#         # print(xs, a)
#         if a == k:
#             return pivot
#         elif a > k:
#             e = a - 1
#         else:
#             s = a + 1
#         pass
#     return xs[s]


# def solve(n, xs, k):
#     s, e = 0, n - 1
#     while s != e:
#         pivot = xs[e]
#         index = s
#         for i in range(s, e):
#             if xs[i] < pivot:
#                 xs[index], xs[i] = xs[i], xs[index]
#                 index += 1
#         xs[index], xs[e] = xs[e], xs[index]
#         if index == k:
#             return pivot
#         elif index > k:
#             e = index - 1
#         else:
#             s = index + 1
#     return xs[s]

from queue import PriorityQueue


class Value:
    def __init__(self, v):
        self.v = v

    def __lt__(self, other):
        return self.v > other.v


def solve(n, xs, k):
    kidx = k + 1
    pq = PriorityQueue()
    for i in range(kidx):
        pq.put(Value(xs[i]))
    for i in range(kidx, n):
        v = xs[i]
        max_v = pq.get()
        pq.put(Value(min(max_v.v, v)))
    return pq.get().v


t = int(input())
for _ in range(t):
    n = int(input())
    xs = [int(x) for x in input().rstrip().split()]
    k = int(input())
    print(solve(n, xs, k - 1))
