#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from bs4 import BeautifulSoup

def fmt(input_path):
    output_path = input_path.replace('.html', '.txt')
    data = open(input_path).read()
    bs = BeautifulSoup(data, "lxml")
    xs = bs.select('.noteText')
    xs = [x.text.replace(' ', '') for x in xs]
    with open(output_path, 'w') as fh:
        for x in xs:
            fh.write(x)
            fh.write('\n\n')

import sys
fmt(sys.argv[1])
