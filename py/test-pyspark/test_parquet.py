#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import sys

from pyspark.sql import SparkSession

spark_sc = SparkSession.builder.appName(__name__).getOrCreate()

input_file = sys.argv[1]
output_folder = sys.argv[2]

df = spark_sc.read.json(input_file)
df.printSchema()
df.write.parquet(output_folder)
