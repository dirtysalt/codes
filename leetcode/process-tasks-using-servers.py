#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        import heapq
        ev = []

        for i in range(len(servers)):
            ev.append((0, 0, i))

        for i in range(len(tasks)):
            ev.append((i, 1, i))

        heapq.heapify(ev)

        from collections import deque
        srv = []
        Q = deque()

        ans = [-1] * len(tasks)
        todo = len(tasks)

        while ev and todo:
            # print('ev', ev)
            ct = ev[0][0]

            while ev and ev[0][0] == ct:
                (t, type, idx) = heapq.heappop(ev)
                if type == 0:
                    # server avail
                    heapq.heappush(srv, (servers[idx], idx))
                elif type == 1:
                    # task avail
                    Q.append(idx)

            # print(srv, Q)
            while Q and srv:
                _, srvidx = heapq.heappop(srv)
                tidx = Q.popleft()
                ans[tidx] = srvidx
                todo -= 1
                heapq.heappush(ev, (ct + tasks[tidx], 0, srvidx))
        return ans


if __name__ == '__main__':
    pass
