#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import math
import os
import random
import re
import sys

# Complete the isValid function below.


def isValid(s):
    from collections import Counter
    c = Counter(s)
    items = c.most_common()
    _max = items[0][1]
    _min = items[-1][1]
    if _max == _min:
        return "YES"
    if (_min + 1) == _max and items[1][1] == _min:
        return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
