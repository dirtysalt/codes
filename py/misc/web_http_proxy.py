#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import flask
from flask import stream_with_context, Response, request
import requests
import urllib.parse

app = flask.Flask(__name__)


@app.route('/stream', methods=['HEAD', 'OPTIONS', 'GET'])
def do_stream():
    url = request.args.get('u', None)
    headers = dict(request.headers)
    print(headers)
    r = urllib.parse.urlparse(url)
    host = r.netloc
    headers['Host'] = host
    r = requests.request(url=url, method=request.method, headers=headers, stream=True)
    resp = Response(response=stream_with_context(r.iter_content()), headers=dict(r.headers), status=r.status_code)
    return resp


if __name__ == '__main__':
    app.run('0.0.0.0', 10004, debug=True)
