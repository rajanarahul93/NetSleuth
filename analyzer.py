from scapy.all import IP, TCP, UDP
from collections import defaultdict
import pandas as pd

# To store packet statistics
packet_stats = defaultdict(int)

def analyze_packet(packet):
    global packet_stats
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        packet_stats["total_packets"] += 1
        
        if TCP in packet or UDP in packet:
            packet_stats["total_data_packets"] += 1
            packet_stats[f"{src_ip}->{dst_ip}"] += 1
        
        if len(packet) > 1500:
            packet_stats["large_packets"] += 1  # Large packets

        save_stats()

def save_stats():
    df = pd.DataFrame(packet_stats.items(), columns=["Metric", "Count"])
    df.to_csv("packet_analysis.csv", index=False)
    print("Stats updated: packet_analysis.csv")
