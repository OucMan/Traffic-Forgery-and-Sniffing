from scapy.all import *

def handle_pkt(pkt):
    print('got a packet')
    pkt.show2()
    #hexdump(pkt)
    sys.stdout.flush()

def main():
    iface = 'eth0'
    print('sniffing on %s' % iface)
    sniff(iface=iface, prn=lambda x: handle_pkt(x))

if __name__ == '__main__':
    main()
