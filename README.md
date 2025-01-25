# **NetSleuth: Real-Time Packet Sniffer and Analyzer**

NetSleuth is a Python-based application designed to capture, analyze, and visualize live network traffic. Leveraging powerful libraries like `Scapy`, it provides detailed insights into network activity, highlights anomalies, and generates comprehensive analysis reports.

---

## **Features**

- **Live Packet Capture**: Monitors and captures real-time network traffic on specified interfaces.
- **Protocol Analysis**: Identifies protocols like TCP, UDP, HTTP, and more.
- **Anomaly Detection**: Detects unusual traffic patterns or potential attacks.
- **Data Logging**: Saves packet details to CSV for further analysis.
- **Visual Reports**: Generates graphical representations of captured data.

---

## **Installation**

### Prerequisites
- Python 3.x
- Administrator/root privileges (required for packet sniffing)
- Npcap (Windows) or libpcap (Linux/Mac)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/rajanarahul93/netsleuth.git
   cd netsleuth
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install packet capture library:
   - **Windows**: [Download Npcap](https://npcap.com/)
   - **Linux**: Install libpcap:
     ```bash
     sudo apt-get install libpcap-dev
     ```
   - **Mac**: Install libpcap using Homebrew:
     ```bash
     brew install libpcap
     ```

---

## **Usage**

### Step 1: Start Packet Sniffing
Run the sniffer script to capture live network packets:
```bash
python sniffer.py
```
- Enter the network interface when prompted (e.g., `eth0`, `wlan0`, `Wi-Fi`).

### Step 2: Analyze Captured Data
After capturing packets, generate an analysis report:
```bash
python report_generator.py
```

### Outputs:
- `packet_analysis.csv`: Contains raw packet details.
- `analysis_report.png`: Graphical report of analyzed data.

---

## **File Structure**

```plaintext
NetSleuth/
├── sniffer.py             # Captures live network packets
├── analyzer.py            # Processes and analyzes captured packets
├── report_generator.py    # Generates visual analysis reports
├── requirements.txt       # Dependencies
├── packet_analysis.csv    # Raw packet data (auto-generated)
├── analysis_report.png    # Graphical analysis report (auto-generated)
└── README.md              # Project documentation
```

---

## **Examples**

1. **Live Packet Capture**:
   ```
   Enter the network interface (e.g., eth0, wlan0): wlan0
   Capturing packets... Press Ctrl+C to stop.
   IP / TCP 192.168.1.5:443 > 192.168.1.2:50233 S
   IP / UDP 192.168.1.10:123 > 192.168.1.1:123
   ```


---

## **Troubleshooting**

1. **`No libpcap provider available! pcap won't be used`**:
   - Install Npcap (Windows) or libpcap (Linux/Mac) as explained above.

2. **Permission Denied**:
   - Use `sudo` (Linux/Mac) or run the terminal as Administrator (Windows).

3. **Interface Not Found**:
   - Use `ifconfig` (Linux/Mac) or `ipconfig` (Windows) to identify active interfaces.

---

## **Contributing**

Contributions are welcome! Please fork the repository, create a branch, and submit a pull request with your changes.

---

## **Acknowledgments**

- Developed using [Scapy](https://scapy.net/)
- Inspired by real-world challenges in network security and analysis.

---
