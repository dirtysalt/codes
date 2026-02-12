#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        ss = sentence.split()
        n = len(ss)
        for i in range(n):
            j = (i + 1) % n
            if ss[i][-1] != ss[j][0]:
                return False
        return True


if __name__ == '__main__':
    pass
