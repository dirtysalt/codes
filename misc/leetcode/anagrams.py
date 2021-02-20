#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ss = [(''.join(sorted(x)), x) for x in strs]
        ss.sort(key=lambda x: x[0])

        res = []
        g = []
        ptag = None
        for (tag, s) in ss:
            if ptag is None: ptag = tag
            if ptag != tag:
                res.append(g)
                g = []
                ptag = tag
            g.append(s)
        if g: res.append(g)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
