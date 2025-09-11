#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        def ok(s):
            from collections import Counter
            cnt = Counter()
            for c in s:
                if c not in 'aeiou':
                    return False
                cnt[c] += 1
            for c in 'aeiou':
                if cnt[c] == 0:
                    return False
            return True

        ans = 0
        for i in range(len(word)):
            for j in range(i, len(word)):
                s = word[i:j + 1]
                if ok(s):
                    ans += 1

        return ans


if __name__ == '__main__':
    pass
