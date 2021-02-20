#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def to_norm(w):
            s = ''
            for c in w.lower():
                if c in 'aeoiu':
                    c = '0'
                s += c
            return s

        d = set(wordlist)

        d2 = {}
        for w in wordlist:
            w2 = w.lower()
            if w2 not in d2:
                d2[w2] = w

        d3 = {}
        for w in wordlist:
            s = to_norm(w)
            if s not in d3:
                d3[s] = w

                # print(d, d2)
        ans = []
        for q in queries:
            if q in d:
                ans.append(q)
                continue

            q2 = q.lower()
            if q2 in d2:
                ans.append(d2[q2])
                continue

            q3 = to_norm(q)
            if q3 in d3:
                ans.append(d3[q3])
                continue

            ans.append('')
        return ans
