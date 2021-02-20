#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def validIPAddress(self, IP: str) -> str:
        import string
        # 1. . 和 :区分ipv4和ipv6
        # 2. IPv4: a) 4个部分 c)每个值返回值在0-255 d)只允许包含十进制 c)如果是leading0, 那么必须是0
        # 3. IPv6: a) 8个部分 b)十六进制 c)<=4字幕

        def to_int(x):
            if x[0] == '0' and len(x) != 1:
                return -1
            v = 0
            for c in x:
                if c in string.digits:
                    v = v * 10 + ord(c) - ord('0')
                else:
                    return -1
            return v

        def all_hex(x):
            if len(x) > 4:
                return False
            # if all((c == '0' for c in x)):
            #     return x == '0000' or x == '0'
            for c in x:
                if c not in string.hexdigits:
                    return False
            return True

        def is_ipv4(x):
            ss = x.split('.')
            if len(ss) != 4:
                return False
            ss = [s for s in ss if s]
            if len(ss) != 4:
                return False
            for s in ss:
                v = to_int(s)
                if v < 0 or v >= 256:
                    return False
            return True

        def is_ipv6(x):
            ss = x.split(':')
            if len(ss) != 8:
                return False
            ss = [s for s in ss if s]
            if len(ss) != 8:
                return False
            for s in ss:
                if not all_hex(s):
                    return False
            return True

        if '.' in IP and is_ipv4(IP):
            return "IPv4"
        elif ':' in IP and is_ipv6(IP):
            return "IPv6"
        return 'Neither'


cases = [
    ("172.16.254.1", "IPv4"),
    ("2001:0db8:85a3:0:0:8A2E:0370:7334", "IPv6"),
    ("256.256.256.256", "Neither"),
    ("01.01.01.01", "Neither"),
    ("192.0.0.1", "IPv4")
]

import aatest_helper

aatest_helper.run_test_cases(Solution().validIPAddress, cases)
