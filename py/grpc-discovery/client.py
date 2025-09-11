#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import grpc

import helloworld_pb2_grpc
from helloworld_pb2 import HelloRequest


def run():
    for i in range(10):
        channel = grpc.insecure_channel('localhost:50051')
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        request = HelloRequest()
        request.name = "yan"
        resp = stub.SayHello(request)
        print(resp.message)
        channel.close()


if __name__ == '__main__':
    run()
