#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

import os


# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    def fun(year):
        if 1700 <= year <= 1917:  # julian calendar
            if year % 4 == 0:
                return '12.09'
            else:
                return '13.09'
        elif year > 1918:
            if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
                return '12.09'
            else:
                return '13.09'
        else:
            return '26.09'

    ans = fun(year)
    ans = ans + '.%04d' % year
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
