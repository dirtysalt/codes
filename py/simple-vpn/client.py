from __future__ import print_function
from __future__ import unicode_literals

import os
import sys
import time
import struct
import socket
from fcntl import ioctl
from select import select
from threading import Thread

PASSWORD = b'4fb88ca224e'

MTU = 1400
BUFFER_SIZE = 4096
KEEPALIVE = 10

TUNSETIFF = 0x400454ca
IFF_TUN   = 0x0001
IFF_TAP   = 0x0002

def createTunnel(tunName='tun%d',tunMode=IFF_TUN):
    tunfd = os.open("/dev/net/tun", os.O_RDWR)
    ifn = ioctl(tunfd, TUNSETIFF, struct.pack(b"16sH", tunName.encode(), tunMode))
    tunName = ifn[:16].decode().strip("\x00")
    return tunfd,tunName
    
def startTunnel(tunName, localIP, peerIP):
    os.popen('ifconfig %s %s dstaddr %s mtu %s up' % 
            (tunName, localIP, peerIP, MTU)).read()


class Client():
    def __init__(self):
        self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp.settimeout(5)
        self.to = SERVER_ADDRESS

    def keepalive(self):
        def _keepalive(udp, to):
            while True:
                time.sleep(KEEPALIVE)
                udp.sendto(b'\x00', to)
        k = Thread(target=_keepalive, args=(self.udp, self.to), name='keepalive')
        k.setDaemon(True)
        k.start()

    def login(self):
        self.udp.sendto(PASSWORD,self.to)
        try:
            data,addr = self.udp.recvfrom(BUFFER_SIZE)
            tunfd,tunName = createTunnel()
            localIP,peerIP = data.decode().split(';')
            print('Local ip: %s\tPeer ip: %s' % (localIP,peerIP))
            startTunnel(tunName,localIP,peerIP)
            return tunfd
        except socket.timeout:
            return False

    def run_forever(self):
        print('Start connect to server...')
        tunfd = self.login()
        if not tunfd:
            print("Connect failed!")
            sys.exit(0)
        print('Connect to server successful')
        self.keepalive()
        readables = [self.udp, tunfd]
        while True:
            try:
                readab = select(readables, [], [], 10)[0]
            except KeyboardInterrupt:
                self.udp.sendto(b'e', self.to)
                raise KeyboardInterrupt
            for r in readab:
                if r == self.udp:
                    data, addr = self.udp.recvfrom(BUFFER_SIZE)
                    try:
                        os.write(tunfd, data)
                    except OSError:
                        if data == b'r':
                            os.close(tunfd)
                            readables.remove(tunfd)
                            print('Reconnecting...')
                            tunfd = self.login()
                            readables.append(tunfd)
                        continue
                else:
                    data = os.read(tunfd, BUFFER_SIZE)
                    self.udp.sendto(data, self.to)

if __name__ == '__main__':
    try:
        SERVER_ADDRESS = (sys.argv[1], int(sys.argv[2]))
        Client().run_forever()
    except IndexError:
        print('Usage: %s [remote_ip] [remote_port]' % sys.argv[0])
    except KeyboardInterrupt:
        print('Closing vpn client ...')