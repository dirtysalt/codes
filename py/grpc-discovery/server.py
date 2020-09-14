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

import gevent.monkey

gevent.monkey.patch_all()

import grpc._cython.cygrpc

grpc._cython.cygrpc.init_grpc_gevent()

# from gevent.threadpool import ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor

import multiprocessing
import time

import os

import helloworld_pb2_grpc
from helloworld_pb2 import HelloReply


class HelloServicer(helloworld_pb2_grpc.GreeterServicer):
    def __init__(self):
        pass

    def SayHello(self, request, context):
        name = request.name
        message = "Hello {}. pid = {}".format(name, os.getpid())
        reply = HelloReply()
        reply.message = message
        return reply


def serve():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(
        HelloServicer(), server)
    address = '[::]:50051'
    print('listen on {}'.format(address))
    server.add_insecure_port(address)

    def run(server):
        print('create process pid = {}'.format(os.getpid()))
        server.start()
        while True:
            try:
                time.sleep(3600)
            except KeyboardInterrupt:
                break
        server.stop(0)

    print('master pid = {}'.format(os.getpid()))
    ts = []
    for i in range(4):
        t = multiprocessing.Process(target=run, args=(server,))
        t.start()
        ts.append(t)

    # see also https://github.com/grpc/grpc/issues/10084
    # otherwise you be caught error
    # E1128 13:49:24.647594000 4728202688 server.cc:1330]
    # assertion failed: gpr_atm_acq_load(&server->shutdown_flag) || !server->listeners

    server.start()
    server.stop(0)

    for t in ts:
        t.join()

    print('exit')


if __name__ == '__main__':
    serve()
