#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import pandas
import pymongo

client = pymongo.MongoClient()
table = client.playfm.series

rs = table.find()
docs = []
for r in rs:
    tags = r.get('tags')
    if tags is None: continue
    doc = {'url': r['_id'], 'feed': r['feed'], 'home': r['home'], 'tags': '|'.join(tags)}
    docs.append(doc)

df = pandas.DataFrame.from_records(docs)
df.to_csv('playfm_series.csv', header=True, index=False, columns=['url', 'feed', 'home', 'tags'])
