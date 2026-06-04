#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class LRUCache:

    def __init__(self, capacity: int):
        self.kv = {}
        from collections import deque, Counter
        self.dq = deque()
        self.delay = Counter()
        self.cap = capacity

    def push(self, k):
        self.dq.append(k)
        self.delay[k] += 1

    def pop(self):
        while self.dq:
            x = self.dq.popleft()
            self.delay[x] -= 1
            if self.delay[x] == 0:
                break
        del self.kv[x]

    def get(self, key: int) -> int:
        if key in self.kv:
            self.push(key)
            return self.kv[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.kv[key] = value
        self.push(key)
        if len(self.kv) == (self.cap + 1):
            self.pop()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
