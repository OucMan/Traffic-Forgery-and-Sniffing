from scapy.all import *
from calc_header import Calc

def main():
    iface = 'eth0'
    dst_id = '2'
    oper = '+'
    num1 = 3
    num2 = 5
    print('sending on interface %s to %s' % (iface, dst_id))
    pkt = Ether(src=get_if_hwaddr(iface), dst='ff:ff:ff:ff:ff:ff')
    pkt = pkt / Calc(op=oper, operand_a=int(num1), operand_b=int(num2))
    pkt.show2()
    sendp(pkt, iface=iface, verbose=False)

if __name__ == '__main__':
    main()




