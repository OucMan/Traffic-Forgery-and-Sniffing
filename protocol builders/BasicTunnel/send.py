from scapy.all import *
from my_tunnel_header import MyTunnel

def main():
    iface = 'eth0'
    dst_id = '2'
    print('sending on interface %s to %s' % (iface, dst_id))
    pkt = Ether(src=get_if_hwaddr(iface), dst='ff:ff:ff:ff:ff:ff')
    pkt = pkt / MyTunnel(dst_id=dst_id) / IP(dst='127.0.0.1') / TCP(dport=1234, sport=random.randint(49152, 65535)) / 'hello'
    pkt.show2()
    sendp(pkt, iface=iface, verbose=False)

if __name__ == '__main__':
    main()
