#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import logging

logger = logging.getLogger('test_socketio')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter('[%(asctime)s][%(levelname)s]%(filename)s@%(lineno)d: %(msg)s'))
logger.addHandler(handler)
