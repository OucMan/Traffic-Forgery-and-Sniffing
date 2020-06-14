from scapy.all import *
from SourceRoute import SourceRoute


def main():
    iface = 'eth0'
    print('sending on interface %s' % iface)
    addr = '127.0.0.1'
    while True:
        print
        s = input('Type space separated port nums (example: "2 3 2 2 1") ')

        i = 0
        pkt = Ether(src=get_if_hwaddr(iface), dst='ff:ff:ff:ff:ff:ff');
        for p in s.split(" "):
            try:
                pkt = pkt / SourceRoute(bos=0, port=int(p))
                i = i+1
            except ValueError:
                pass
        if pkt.haslayer(SourceRoute):
            pkt.getlayer(SourceRoute, i).bos = 1

        pkt = pkt / IP(dst=addr) / UDP(dport=4321, sport=1234)
        pkt.show2()
        sendp(pkt, iface=iface, verbose=False)

if __name__ == '__main__':
    main()
