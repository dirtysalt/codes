#!/usr/bin/env python
#coding:utf-8
#Copyright (C) dirlt

from test_pye import *
assert(add(1,2) == 3)

items = ItemArray()

item = Item(20)
assert(item.x == 20)
assert(item.y == 10)
item.echo()
item.echo("???")
items.append(item)

item = Item(10, 30)
assert(item.x == 10)
assert(item.y == 30)
items.append(item)

assert(len(items) == 2)

items2 = [items[0], items[1]]
handle_item_array(items2)

op = items[0].get_opaque()
print op

# test copy ctor or operator =
print item.x, item.y
a = item
a.x += 10
a.y += 20
print item.x, item.y
