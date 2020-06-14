from scapy.all import *

def main():
    iface = 'eth0'
    print('sending on interface %s' % iface)
    pkt = Ether(src=get_if_hwaddr(iface), dst='ff:ff:ff:ff:ff:ff')
    pkt = pkt / IP(dst='127.0.0.1') / TCP(dport=1234, sport=random.randint(49152, 65535)) / 'hello'
    pkt.show2()
    sendp(pkt, iface=iface, verbose=False)

if __name__ == '__main__':
    main()


