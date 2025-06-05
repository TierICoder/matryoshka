import os
from scapy.all import sniff, TCP, IP
from collections import defaultdict
import time
import threading
from datetime import datetime

# SYN Flood sayaçları
syn_counter = defaultdict(int)
scan_threshold = 100

# Log dosyası masaüstüne yazılacak
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "ids_alerts.log")

def log_alert(message):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} {message}\n")

def detect_syn_flood(packet):
    if packet.haslayer(TCP) and packet[TCP].flags == "S":
        src_ip = packet[IP].src
        syn_counter[src_ip] += 1

        if syn_counter[src_ip] > scan_threshold:
            alert_msg = f"[ALERT] Olası SYN Flood saldırısı! Kaynak IP: {src_ip}"
            print(alert_msg, flush=True)  # Burada flush eklendi
            log_alert(alert_msg)

def reset_counters():
    while True:
        time.sleep(10)
        syn_counter.clear()

def main():
    print("IDS çalışıyor... Ctrl+C ile durdurabilirsiniz.", flush=True)
    print(f"Log dosyası: {LOG_FILE}", flush=True)

    reset_thread = threading.Thread(target=reset_counters, daemon=True)
    reset_thread.start()

    sniff(iface="lo", prn=detect_syn_flood, store=False)

if __name__ == "__main__":
    main()
