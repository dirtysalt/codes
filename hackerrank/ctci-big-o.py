#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

if __name__ == '__main__':
    p = int(input())

    for p_itr in range(p):
        n = int(input())
        if n == 1:
            print('Not prime')
            continue
        prime = True
        i = 2
        while (i * i <= n):
            if (n % i) == 0:
                prime = False
                break
            i += 1
        print(('Prime' if prime else 'Not prime'))

# if __name__ == '__main__':
#     p = int(input())

#     for p_itr in range(p):
#         n = int(input())
#         if n == 1:
#             print('Not prime')
#             continue
#         if n == 2:
#             print('Prime')
#             continue
#         thres = int(n ** 0.5) + 2
#         prime = True
#         for i in range(2, thres):
#             if (n % i) == 0:
#                 prime = False
#                 break
#         print('Prime' if prime else 'Not prime')
