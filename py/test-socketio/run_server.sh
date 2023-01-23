#!/usr/bin/env bash
# Copyright (C) dirlt

# pip install gevent gevent-websocket
gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 --bind 0.0.0.0:8080 server:app
