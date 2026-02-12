#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> \
            List[str]:
        n = len(watchedVideos)
        visited = [0] * n
        from collections import Counter, deque
        cnt = Counter()
        dq = deque()
        dq.append((id, 0))
        visited[id] = 1

        while dq:
            x, d = dq.popleft()
            if d == level:
                for v in watchedVideos[x]:
                    cnt[v] += 1
                continue

            for f in friends[x]:
                if visited[f]:
                    continue
                visited[f] = 1
                dq.append((f, d + 1))

        items = list(cnt.items())
        items.sort(key=lambda x: (x[1], x[0]))
        ans = [x[0] for x in items]
        return ans
