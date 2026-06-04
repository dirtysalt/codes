#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import deque


class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """

        if start == end:
            return 0

        genes = []
        gene_set = set()

        gene_set.add(start)
        genes.append(start)

        for s in bank:
            if s not in gene_set:
                genes.append(s)
                gene_set.add(s)

        if end not in gene_set:
            # invalid gene.
            return -1

        gene_ids = dict()
        n = len(genes)
        for i in range(n):
            gene_ids[genes[i]] = i

        src = 0
        dest = gene_ids[end]

        def mutate(s):
            for i in range(8):
                for c in 'ATCG':
                    if c == s[i]: continue
                    yield s[:i] + c + s[i + 1:]

        adj = [[] for _ in range(n)]
        for i in range(n):
            s = genes[i]
            for s2 in mutate(s):
                j = gene_ids.get(s2)
                if j is not None:
                    adj[i].append(j)
                    adj[j].append(i)

        dist = [-1] * n
        queue = deque()
        queue.append(src)
        dist[src] = 0
        while queue:
            x = queue.popleft()
            if x == dest:
                break
            for y in adj[x]:
                if dist[y] == -1:
                    dist[y] = dist[x] + 1
                    queue.append(y)
        return dist[dest]
