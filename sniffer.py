from scapy.all import sniff
from analyzer import analyze_packet

def packet_callback(packet):
    print(packet.summary())  # Print a quick summary
    analyze_packet(packet)   # Pass packet for analysis

def start_sniffing(interface="eth0"):
    print(f"Starting packet capture on {interface}...")
    sniff(iface=interface, prn=packet_callback, store=False)

if __name__ == "__main__":
    interface = input("Enter the network interface (e.g., eth0, wlan0): ")
    start_sniffing(interface)
