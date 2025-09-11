#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import cgi
import flask
from flask import request as AppRequest

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def handle_index():
    return """<html><head></head><body>
    <form method="POST" enctype="multipart/form-data" action="/upload">
    <input type="file" name="myfile" />
    <br/>
    <input type="submit" />
    </form>
    </body></html>"""


@app.route('/upload', methods=['POST'])
def handle_upload():
    s = ''
    args = AppRequest.args
    for k in list(args.keys()):
        s += '<li>%s = %s</li>' % (k, cgi.escape(str(args[k])))
    form_s = ''
    form = AppRequest.form
    for k in list(form.keys()):
        form_s += '<li>%s = %s</li>' % (k, cgi.escape(str(form[k])))
    headers_s = ''
    headers = AppRequest.headers
    for k in list(headers.keys()):
        headers_s += '<li>%s = %s</li>' % (k, cgi.escape(str(headers[k])))
    html = """<html><body><p>args<br/><ul>%s</ul></p>
    <p>form<br/><ul>%s</ul></p>
    <p>headers<br/><ul>%s</ul></p>
    </body></html>""" % (s, form_s, headers_s)
    return html


if __name__ == "__main__":
    app.run(port=9999, debug=True)
