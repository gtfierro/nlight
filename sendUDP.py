import sys
import socket

# destinarion IP address
IPADDR = '192.168.1.4'
# destination PORT number
PORTNUM = 5551
# hex encoded data for the packet
PACKETDATA = 'a5007782a8fffffff1222d0e096a0021302870620000005900006851f0052210554d'.decode('hex')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
s.connect((IPADDR, PORTNUM))
s.send(PACKETDATA)
s.close()

def send_line(line):
    s.send(line)

def send_file(filename):
    with open(filename) as f:
        for line in f.read().split('\n'):
            s.send(line)
