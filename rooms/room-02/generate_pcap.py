import sys
from scapy.all import *

password = sys.argv[1]
output = sys.argv[2]

# Create some dummy traffic
packets = [
    IP(dst="192.168.1.100", src="192.168.1.50")/TCP(sport=12345, dport=21)/Raw(load="USER sysadmin\r\n"),
    IP(dst="192.168.1.50", src="192.168.1.100")/TCP(sport=21, dport=12345)/Raw(load="331 Please specify the password.\r\n"),
    IP(dst="192.168.1.100", src="192.168.1.50")/TCP(sport=12345, dport=21)/Raw(load=f"PASS {password}\r\n"),
    IP(dst="192.168.1.50", src="192.168.1.100")/TCP(sport=21, dport=12345)/Raw(load="230 Login successful.\r\n"),
    IP(dst="192.168.1.100", src="192.168.1.50")/TCP(sport=12345, dport=21)/Raw(load="SYST\r\n")
]

wrpcap(output, packets)
