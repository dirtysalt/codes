#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0': return '0'

        num1 = num1[::-1]
        num2 = num2[::-1]
        adds = []
        for i in range(0, len(num1)):
            a = int(num1[i])
            bits_n = i + len(num2)
            adds.extend([0] * (bits_n - len(adds)))
            for j in range(0, len(num2)):
                b = int(num2[j])
                adds[i + j] += a * b

        flag = 0
        for i in range(len(adds)):
            v = flag + adds[i]
            adds[i] = str(v % 10)
            flag = v / 10

        while flag:
            adds.append(str(flag % 10))
            flag /= 10

        return ''.join(reversed(adds))


if __name__ == '__main__':
    s = Solution()
    print(s.multiply('123', '456'), 123 * 456)
    print(s.multiply('1236789', '456123'), 1236789 * 456123)
