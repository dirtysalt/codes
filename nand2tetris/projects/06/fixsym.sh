#!/usr/bin/env bash
# Copyright (C) dirlt

find . | grep "\.asm$" | xargs ./asm.py --fixsym --ext ".txt"
