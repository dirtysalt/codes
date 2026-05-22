#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8: return False
        if not any((c.isupper() for c in password)): return False
        if not any((c.islower() for c in password)): return False
        if not any((c.isdigit() for c in password)): return False
        if not any((c in "!@#$%^&*()-+" for c in password)): return False
        l = None
        for c in password:
            if c == l: return False
            l = c
        return True


if __name__ == '__main__':
    pass
