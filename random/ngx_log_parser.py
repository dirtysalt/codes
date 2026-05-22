#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import re
import string


class NginxLogParser:
    def __init__(self, log_formats):
        self.log_formats = log_formats
        self.patterns = [re.compile(NginxLogParser.build_regex_pattern(x)) for x in log_formats]
        self.pattern_size = len(self.patterns)

    @staticmethod
    def build_regex_pattern(log_format):
        buf = '^'
        var_name = ''
        var_mode = False
        for c in log_format:
            if c == '$':
                var_mode = True
            elif c in string.ascii_letters or c in string.digits or c in '_-':
                if var_mode:
                    var_name += c
                else:
                    buf += '\{}'.format(c)
            else:
                if var_mode:
                    buf += '(?P<{}>[^{}]*)\{}'.format(var_name, c, c)
                    var_mode = False
                    var_name = ''
                else:
                    buf += '\{}'.format(c)
        if var_mode:
            buf += '(?P<{}>[^$]*)'.format(var_name)
            var_mode = False
            var_name = ''
        buf += '$'
        # print(buf)
        return buf

    def match(self, s):
        match_idx = None
        match_obj = None
        for idx, p in enumerate(self.patterns):
            match_obj = p.match(s)
            if match_obj:
                match_idx = idx
                break
        if match_obj and match_idx != 0:
            # adjust orders, bring matched regex to first.
            seqs = self.patterns[match_idx:match_idx + 1] + \
                   self.patterns[:match_idx] + \
                   self.patterns[match_idx + 1:]
            self.patterns = seqs
        return match_obj


def test():
    logs = """
172.31.25.233 - - [07/Jan/2019:00:03:02 +0000] "GET /ping HTTP/1.1" 200 50 "-" "okhttp/3.10.0" "174.207.53.50"
172.31.14.173 - - [07/Jan/2019:00:03:02 +0000] "GET /ping HTTP/1.1" 200 50 "-" "okhttp/3.10.0" "174.207.53.50"
172.31.14.173 - - [07/Jan/2019:00:03:02 +0000] "GET /ping HTTP/1.1" 200 50 "-" "okhttp/3.10.0" "66.87.153.54"
172.31.25.233 - - [07/Jan/2019:00:03:02 +0000] "GET /ping HTTP/1.1" 200 50 "-" "okhttp/3.10.0" "66.87.153.54"
172.31.25.233 - - [07/Jan/2019:00:03:02 +0000] "GET /ping HTTP/1.1" f622494b9b8fbe421855056e60ab70a4 200 50 "-" "okhttp/3.10.0" "174.207.53.50"
172.31.14.173 - - [07/Jan/2019:00:03:02 +0000] "GET /ping HTTP/1.1" 81c1f0fc31650afae026e0803e762cf7 200 50 "-" "okhttp/3.10.0" "174.207.53.50"
172.31.14.173 - - [07/Jan/2019:00:03:02 +0000] "GET /ping HTTP/1.1" a1ea547d40a6858d3b08e430ca83e6b7 200 50 "-" "okhttp/3.10.0" "66.87.153.54"
172.31.25.233 - - [07/Jan/2019:00:03:02 +0000] "GET /ping HTTP/1.1" aa7b028ab7b2f5a74b65726feca37896 200 50 "-" "okhttp/3.10.0" "66.87.153.54"
""".split('\n')

    log_formats = [
        '$remote_addr - $remote_user [$time_local] "$request" $request_id $status $body_bytes_sent "$http_referer" "$http_user_agent" "$http_x_forwarded_for"',
        '$remote_addr - $remote_user [$time_local] "$request" $status $body_bytes_sent "$http_referer" "$http_user_agent" "$http_x_forwarded_for"',
    ]

    parser = NginxLogParser(log_formats=log_formats)
    for log in logs:
        log = log.strip()
        if not log: continue
        match_obj = parser.match(log)
        print(match_obj.groupdict())


if __name__ == '__main__':
    test()
