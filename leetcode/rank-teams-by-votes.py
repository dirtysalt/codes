#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        from collections import defaultdict
        ws = defaultdict(lambda: [0] * 26)
        ans = []

        # O(n)
        for vt in votes:
            for idx, c in enumerate(vt):
                ws[c][idx] -= 1

        # assume there are C characters
        # and possible ranks are D [0-25]
        # O(C * lgC * D)
        # D是用来比较每个字符的权重的
        hp = [(v, k) for k, v in ws.items()]
        import heapq
        heapq.heapify(hp)

        while hp:
            (v, k) = heapq.heappop(hp)
            ans.append(k)

        ans = ''.join(ans)
        return ans


cases = [
    (["ABC", "ACB", "ABC", "ACB", "ACB"], "ACB"),
    (["BCA", "CAB", "CBA", "ABC", "ACB", "BAC"], "ABC"),
    (["M", "M", "M", "M"], "M"),
    (["ZMNAGUEDSJYLBOPHRQICWFXTVK"], "ZMNAGUEDSJYLBOPHRQICWFXTVK"),
    (["WXYZ", "XYZW"], "XWYZ"),
    (["FVSHJIEMNGYPTQOURLWCZKAX", "AITFQORCEHPVJMXGKSLNZWUY", "OTERVXFZUMHNIYSCQAWGPKJL", "VMSERIJYLZNWCPQTOKFUHAXG",
      "VNHOZWKQCEFYPSGLAMXJIUTR", "ANPHQIJMXCWOSKTYGULFVERZ", "RFYUXJEWCKQOMGATHZVILNSP", "SCPYUMQJTVEXKRNLIOWGHAFZ",
      "VIKTSJCEYQGLOMPZWAHFXURN", "SVJICLXKHQZTFWNPYRGMEUAO", "JRCTHYKIGSXPOZLUQAVNEWFM", "NGMSWJITREHFZVQCUKXYAPOL",
      "WUXJOQKGNSYLHEZAFIPMRCVT", "PKYQIOLXFCRGHZNAMJVUTWES", "FERSGNMJVZXWAYLIKCPUQHTO", "HPLRIUQMTSGYJVAXWNOCZEKF",
      "JUVWPTEGCOFYSKXNRMHQALIZ", "MWPIAZCNSLEYRTHFKQXUOVGJ", "EZXLUNFVCMORSIWKTYHJAQPG", "HRQNLTKJFIEGMCSXAZPYOVUW",
      "LOHXVYGWRIJMCPSQENUAKTZF", "XKUTWPRGHOAQFLVYMJSNEIZC", "WTCRQMVKPHOSLGAXZUEFYNJI"],
     "VWFHSJARNPEMOXLTUKICZGYQ")
]
import aatest_helper

aatest_helper.run_test_cases(Solution().rankTeams, cases)
