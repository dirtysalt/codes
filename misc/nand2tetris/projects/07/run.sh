#!/usr/bin/env bash
# Copyright (C) dirlt

find . | grep "\.vm$" | xargs ./vmasm.py
