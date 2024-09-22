#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        ban = set(bannedWords)
        cnt = 0
        for x in message:
            if x in ban:
                cnt += 1
                if cnt == 2: return True
        return False


if __name__ == '__main__':
    pass
