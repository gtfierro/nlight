import sys
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Echo(DatagramProtocol):

    def datagramReceived(self, data, (host, port)):
        rawbytes = list(bytearray(data))
        hexstring = ''.join(["%02x" % x for x in rawbytes])
        print "received {0} from {1}:{2}".format(hexstring, host, port)
        return (rawbytes, hexstring)
        #self.transport.write(data, (host, port))


if __name__=='__main__':
    listen_port = int(sys.argv[1])
    reactor.listenUDP(listen_port, Echo())
    reactor.run()
