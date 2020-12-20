#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        def make_counter(s):
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord('a')] += 1
            return counter

        counter1 = make_counter(ransomNote)
        counter2 = make_counter(magazine)
        for idx in range(26):
            if counter1[idx] > counter2[idx]:
                return False
        return True
