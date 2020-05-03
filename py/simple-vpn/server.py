#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import os
import sys
import time
import struct
import socket
from fcntl import ioctl
from select import select
from threading import Thread
from ipaddress import ip_network

DEBUG = True
PASSWORD = b'4fb88ca224e'

BIND_ADDRESS = '0.0.0.0',2003
NETWORK = '10.0.0.0/24'
BUFFER_SIZE = 4096
MTU = 1400

IPRANGE = list(map(str,ip_network(NETWORK)))[1:]
LOCAL_IP = IPRANGE.pop(0)

TUNSETIFF = 0x400454ca
IFF_TUN   = 0x0001
IFF_TAP   = 0x0002

def createTunnel(tunName='tun%d',tunMode=IFF_TUN):
    tunfd = os.open("/dev/net/tun", os.O_RDWR)
    ifn = ioctl(tunfd, TUNSETIFF, struct.pack(b"16sH", tunName.encode(), tunMode))
    tunName = ifn[:16].decode().strip("\x00")
    return tunfd,tunName
    
def startTunnel(tunName,peerIP):
    os.popen('ifconfig %s %s dstaddr %s mtu %s up' % 
                (tunName, LOCAL_IP, peerIP, MTU)).read()
    
now = lambda :time.strftime('[%Y/%m/%d %H:%M:%S] ')

class Server():
    def __init__(self):
        self.sessions = []
        self.readables = []
        self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp.bind(BIND_ADDRESS)
        self.readables.append(self.udp)
        self.tunInfo = {
            'tunName':None, 'tunfd':None,
            'addr':None, 'tunAddr':None, 'lastTime':None
            }
        print('Server listen on %s:%s...' % BIND_ADDRESS)

    def getTunByAddr(self, addr):
        for i in self.sessions:
            if i['addr'] == addr: return i['tunfd']
        return -1

    def getAddrByTun(self,tunfd):
        for i in self.sessions:
            if i['tunfd'] == tunfd: return i['addr']
        return -1

    def createSession(self, addr):
        tunfd,tunName = createTunnel()
        tunAddr = IPRANGE.pop(0)
        startTunnel(tunName,tunAddr)
        self.sessions.append(
            {
                'tunName':tunName, 'tunfd':tunfd, 'addr':addr,
                'tunAddr':tunAddr, 'lastTime':time.time()
            }
        )
        self.readables.append(tunfd)
        reply = '%s;%s' % (tunAddr,LOCAL_IP)
        self.udp.sendto(reply.encode(), addr)

    def delSessionByTun(self, tunfd):
        if tunfd == -1: return False
        for i in self.sessions:
            if i['tunfd'] == tunfd:
                self.sessions.remove(i)
                IPRANGE.append(i['tunAddr'])
        self.readables.remove(tunfd)
        os.close(tunfd)
        return True

    def updateLastTime(self, tunfd):
        for i in self.sessions:
            if i['tunfd'] == tunfd:
                i['lastTime'] = time.time()

    def cleanExpireTun(self):
        while True:
            for i in self.sessions:
                if (time.time() - i['lastTime']) > 60:
                    self.delSessionByTun(i['tunfd'])
                    if DEBUG: print('Session: %s:%s expired!' % i['addr'])
            time.sleep(1)

    def auth(self,addr,data,tunfd):
        if data == b'\x00':
            if tunfd == -1:
                self.udp.sendto(b'r', addr)
            else:
                self.updateLastTime(tunfd)
            return False
        if data == b'e':
            if self.delSessionByTun(tunfd):
                if DEBUG: print("Client %s:%s is disconnect" % addr)
            return False
        if data == PASSWORD:
            return True
        else:
            if DEBUG: print('Clinet %s:%s connect failed' % addr)
            return False

    def run_forever(self):
        cleanThread = Thread(target=self.cleanExpireTun)
        cleanThread.setDaemon(True)
        cleanThread.start()
        while True:
            readab = select(self.readables, [], [], 1)[0]
            for r in readab:
                if r == self.udp:
                    data, addr = self.udp.recvfrom(BUFFER_SIZE)
                    if DEBUG: print(now()+'from    (%s:%s)' % addr, data[:10])
                    try:
                        tunfd = self.getTunByAddr(addr)
                        try:
                            os.write(tunfd,data)
                        except OSError:
                            if not self.auth(addr,data,tunfd):continue
                            self.createSession(addr)
                            if DEBUG: print('Clinet %s:%s connect successful' % addr)
                    except OSError: continue
                else:
                    try:
                        addr = self.getAddrByTun(r)
                        data = os.read(r, BUFFER_SIZE)
                        self.udp.sendto(data,addr)
                        if DEBUG: print(now()+'to      (%s:%s)' % addr, data[:10])
                    except Exception:
                        continue

if __name__ == '__main__':
    try:
        Server().run_forever()
    except KeyboardInterrupt:
        print('Closing vpn server ...')
