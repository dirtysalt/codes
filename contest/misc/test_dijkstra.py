#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


# https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-using-priority_queue-stl/
from queue import PriorityQueue


def addEdge(adj, source, dest, weight):
    adj[source].append((dest, weight))
    adj[dest].append((source, weight))


class Distance:
    def __init__(self, node, value):
        self.node = node
        self.value = value

    def __lt__(self, other):
        return self.value < other.value


INFINITY = 1 << 31


def shortestPath(adj, V, source):
    dist = [INFINITY] * V
    dist[source] = 0
    pq = PriorityQueue()
    pq.put(Distance(source, 0))
    while not pq.empty():
        d = pq.get()
        node = d.node
        for v, w in adj[node]:
            if dist[v] > (dist[node] + w):
                dist[v] = dist[node] + w
                pq.put(Distance(v, dist[v]))
    print('source = {}'.format(source))
    for v in range(V):
        print('-> {} = {}'.format(v, dist[v]))


def main():
    V = 9
    adj = []
    for i in range(V):
        adj.append([])
    addEdge(adj, 0, 1, 4)
    addEdge(adj, 0, 7, 8)
    addEdge(adj, 1, 2, 8)
    addEdge(adj, 1, 7, 11)
    addEdge(adj, 2, 3, 7)
    addEdge(adj, 2, 8, 2)
    addEdge(adj, 2, 5, 4)
    addEdge(adj, 3, 4, 9)
    addEdge(adj, 3, 5, 14)
    addEdge(adj, 4, 5, 10)
    addEdge(adj, 5, 6, 2)
    addEdge(adj, 6, 7, 1)
    addEdge(adj, 6, 8, 6)
    addEdge(adj, 7, 8, 7)
    shortestPath(adj, V, 0)


if __name__ == '__main__':
    main()
