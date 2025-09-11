#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = []
        from collections import Counter
        cnt = Counter()
        for x in cpdomains:
            rep, domain = x.split()
            rep = int(rep)
            ss = domain.split('.')
            for i in range(len(ss)):
                s = '.'.join(ss[i:])
                cnt[s] += rep

        for s, c in cnt.items():
            ans.append("%d %s" % (c, s))
        return ans


if __name__ == '__main__':
    pass
