#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tokens = {}
        self.ttl = timeToLive


    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime


    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.tokens:
            return

        now = self.tokens[tokenId]
        if (now + self.ttl) <= currentTime:
            return
        self.tokens[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        ans = 0
        for _, t in self.tokens.items():
            if (t + self.ttl) <= currentTime:
                continue
            ans += 1
        return ans



# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)

if __name__ == '__main__':
    pass
