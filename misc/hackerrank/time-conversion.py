#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import os

#
# Complete the timeConversion function below.
#


def timeConversion(s):
    #
    # Write your code here.
    #

    hour = int(s[:2])
    if hour == 12:
        if s[-2:] == 'AM':
            hour -= 12
        else:
            pass
    else:
        if s[-2:] == 'PM':
            hour += 12

    ans = '%02d' % hour + s[2:-2]
    return ans


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
