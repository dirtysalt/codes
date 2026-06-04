#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        rs = set()
        for w in words:
            code = ''
            for c in w:
                code += codes[ord(c) - ord('a')]
            rs.add(code)
        return len(rs)
