from scapy.all import *

#def sniff_icmp():
#    sniff(filter = "icmp", prn = handle_packet, store=0)
#
#def handle_packet(packet):
#    if ICMP in packet and packet[ICMP].type == 8:
#        print(f"Received ICMP acho request from {packet[IP].src}")
#        spoof_reply(packet)
#
#def spoof_reply(packet):
#    #crafting ICMP echo reply
#
#    spoofed_reply = IP(src=packed[IP].dst, dst=packet[IP].src)/ICMP(type=0,id=packet[ICMP].id)
#
#    #send spoofed reply
#    send(spoofed_reply, verbose=0)
#    print(f"Sent spoofed ICMP echo reply to {packet[IP].src}")
#
#if __name__ == "__main__":
#    print("Starting ICMP Sniff-and-spoof program...")
#    sniff_icmp()

def print_pkt(pkt):
    pkt.show()

capture = sniff(iface = 'br-c93733e9f913', count =5, filter = 'icmp', prn = print_pkt)
wrpcap("sniffed_packets.pcap", capture)

#ip = IP()
#ip.src = '192.168.1.100'
#ip.dst = '10.0.2.3'
#
#icmp = ICMP()
#
#packet = ip/icmp
#send(packet)

#def traceroute(destination, max_ttl):
#    ttl = 1
#    while ttl <= max_ttl:
#        packet = IP(dst=destination, ttl=ttl)/ICMP()
#
#        reply = sr1(packet, verbose=0, timeout=5)
#        if reply is None:
#            print(f"{ttl}>* Timeout")
#        elif reply.haslayer(ICMP):
#            if reply[ICMP].type ==11 and reply[ICMP].code == 0:
#                print(f"{ttl}.{reply.src}")
#            elif reply[ICMP].type ==0:
#                print(f"{ttl}.{reply.src}Destination reached. ")
#                break
#            else:
#                print(f"{ttl}. *ICMP Type: {reply[ICMP].type}, Code: {reply[ICMP].code}")
#        else:
#            print(f"{ttl}. * unknown response")
#        ttl += 1
#if __name__ == "__main__":
#    destination = "1.2.3.4"
#    max_ttl = 30
#
#    print(f"Traceroute to {destination}, max TTL {max_ttl}:")
#    traceroute(destination, max_ttl)