#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        import itertools

        def ok(seq):
            for i in range(1, len(seq)):
                if pattern[i - 1] == 'I' and seq[i - 1] >= seq[i]:
                    return False
                if pattern[i - 1] == 'D' and seq[i] >= seq[i - 1]:
                    return False
            return True

        for seq in itertools.permutations(list(range(1, 10)), len(pattern) + 1):
            if ok(seq):
                return ''.join([chr(x + ord('0')) for x in seq])
        return None


if __name__ == '__main__':
    pass
