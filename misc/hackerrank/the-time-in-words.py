#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

import os

digits_to_nineteen = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                      'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']


def hour_word(h):
    return digits_to_nineteen[h]


def minute_word(m):
    if m < 20:
        return digits_to_nineteen[m]
    elif m == 20:
        return 'twenty'
    else:
        return 'twenty {}'.format(digits_to_nineteen[m - 20])


# Complete the timeInWords function below.
def timeInWords(h, m):
    hw = hour_word(h)
    h2 = h + 1
    if h2 > 12:
        h2 -= 12
    hw2 = hour_word(h2)
    if m == 0:
        return "{} o' clock".format(hw)
    elif m == 30:
        return 'half past {}'.format(hw)
    elif m == 15:
        return 'quarter past {}'.format(hw)
    elif m == 45:
        return 'quarter to {}'.format(hw2)
    elif m < 30:
        mw = minute_word(m)
        return '{} minute{} past {}'.format(mw, 's' if m != 1 else '', hw)
    else:
        m = 60 - m
        mw = minute_word(m)
        return '{} minute{} to {}'.format(mw, 's' if m != 1 else '', hw2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
