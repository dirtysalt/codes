#!/usr/bin/env bash
# Copyright (C) dirlt

find . | grep "\.jack$" | xargs ./parser.py
