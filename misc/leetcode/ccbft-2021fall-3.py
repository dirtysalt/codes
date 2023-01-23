#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def metroRouteDesignI(self, lines: List[List[int]], start: int, end: int) -> List[int]:
        from collections import defaultdict
        coll = defaultdict(list)

        for ls in lines:
            for p in range(len(ls)):
                x = ls[p]
                for i in range(p + 1, len(ls)):
                    path = tuple(ls[p:i + 1])
                    if path:
                        coll[x].append(path)
                for i in range(p):
                    path = tuple(reversed(ls[i:p + 1]))
                    if path:
                        coll[x].append(path)

        for x, ps in coll.items():
            coll[x] = sorted(ps)
            # print(x, coll[x])

        backs = dict()
        import heapq
        hp = []
        hp.append((0, (start,)))

        while hp:
            (d, path) = heapq.heappop(hp)
            backs[path[-1]] = path
            if path[-1] == end:
                break

            visited = set(path)
            for p in coll[path[-1]]:
                last = p[-1]
                if last in backs: continue
                ok = True
                for x in p[1:]:
                    if x in visited:
                        ok = False
                        break
                if not ok: continue
                np = list(path) + list(p[1:])
                if len(set(np)) == len(np):
                    heapq.heappush(hp, (d + 1, np))

        ans = backs[end]
        return list(ans)


true, false, null = True, False, None
cases = [
    ([[1, 2, 3, 4, 5], [2, 10, 14, 15, 16], [10, 8, 12, 13], [7, 8, 4, 9, 11]], 1, 7, [1, 2, 3, 4, 8, 7]),
    ([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [12, 13, 2, 14, 8, 15], [16, 1, 17, 10, 18]], 9, 1,
     [9, 8, 7, 6, 5, 4, 3, 2, 1]),
    ([[1, 2, 3, 6, 5], [3, 4, 5]], 1, 5, [1, 2, 3, 6, 5],),
    ([[7851, 6448, 853, 9027, 970, 5600, 2269], [4614, 7539], [970, 4614, 2269, 9906],
      [7851, 970, 4614, 9906, 9027, 2269]], 9906, 853, [9906, 2269, 4614, 970, 9027, 853]),
    (
        [[4165, 8075, 3072, 6302, 3747, 3616, 1893], [7431, 3616, 3747, 1893, 8075, 3219], [3072, 6302, 3747],
         [3616, 3969],
         [7431, 3616]], 4165, 3219, [4165, 8075, 3219])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().metroRouteDesignI, cases)

if __name__ == '__main__':
    pass
