#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnt = [0] * 26
        for c in word:
            cnt[ord(c) - ord('a')] += 1

        def ok(cnt):
            t = 0
            for x in cnt:
                if x > 0:
                    if t == 0:
                        t = x
                    elif t != x:
                        return False
            return True

        for i in range(26):
            if cnt[i] > 0:
                cnt[i] -= 1
                if ok(cnt):
                    return True
                cnt[i] += 1
        return False


if __name__ == '__main__':
    pass
