#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


import sys

print(sys.path)

import platform

print(platform.python_version())

from pyspark.sql import SparkSession

spark_sc = SparkSession.builder.appName(__name__).getOrCreate()

# use packages.
import share

share.echo('import share OK')
