#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """

        edges = []
        for v in range(N):
            edges.append([])

        for (u, v, w) in times:
            edges[u - 1].append((v - 1, w))

        INT_MAX = 1 << 31
        sd = [INT_MAX] * N
        K = K - 1
        sd[K] = 0
        nodes = set(range(0, N))
        for (v, w) in edges[K]:
            sd[v] = sd[K] + w
        nodes.remove(K)

        for i in range(1, N):
            # find mininum
            min_idx = -1
            min_value = INT_MAX
            for v in nodes:
                if sd[v] < min_value:
                    min_value = sd[v]
                    min_idx = v;
            if min_idx == -1:
                break
            for (v, w) in edges[min_idx]:
                sd[v] = min(sd[v], sd[min_idx] + w)
            nodes.remove(min_idx)

        max_sd = max(sd)
        if max_sd == INT_MAX:
            return -1
        return max_sd


if __name__ == '__main__':
    s = Solution()
    # print(s.networkDelayTime([[1,2,1]], 2, 2))
    print((s.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)))
