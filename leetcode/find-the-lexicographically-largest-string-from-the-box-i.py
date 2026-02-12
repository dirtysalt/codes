#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1: return word
        n = len(word)
        ans = ""
        for i in range(n):
            # 一共需要确保前后必须有numfriends-1个字符串
            # 前面去掉了i个字符串
            tail = max(numFriends - 1 - i, 0)
            # 从剩余长度切掉tail
            maxsz = n - i - tail
            if maxsz < 0: break
            s = word[i:i + maxsz]
            ans = max(ans, s)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ("dbca", 2, "dbc"),
    ("gggg", 4, "g"),
    ("gh", 1, "gh"),
    ("bif", 2, "if"),
]

aatest_helper.run_test_cases(Solution().answerString, cases)

if __name__ == '__main__':
    pass
