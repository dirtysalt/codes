#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import string


class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """

    def validWordAbbreviation(self, word, abbr):
        # write your code here

        widx, aidx = 0, 0
        while widx < len(word) and aidx < len(abbr):

            if abbr[aidx] in '123456789':  # '0' can not preceed.
                val = 0
                while aidx < len(abbr) and abbr[aidx] in string.digits:
                    val = val * 10 + ord(abbr[aidx]) - ord('0')
                    aidx += 1
                if (widx + val) > len(word):
                    return False
                widx += val
            else:
                if abbr[aidx] == word[widx]:
                    aidx += 1
                    widx += 1
                else:
                    return False
        return widx == len(word) and aidx == len(abbr)
