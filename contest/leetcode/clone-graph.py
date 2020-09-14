#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        seen = {}
        if not node: return node

        def cp(n):
            x = n.label
            if x in seen: return seen[x]
            n2 = UndirectedGraphNode(x)
            seen[x] = n2
            nns = []
            for nn in n.neighbors:
                nns.append(cp(nn))
            n2.neighbors = nns
            return n2

        return cp(node)
