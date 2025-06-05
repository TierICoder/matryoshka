import socket
from datetime import datetime
import os
import ipaddress

# Masaüstü log dosyası yolu
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
log_file = os.path.join(desktop_path, "port_taramasi_log.txt")

# IP doğrulama fonksiyonu
def ip_kontrol(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

# Loglama fonksiyonu
def log_yaz(line):
    print(line)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(line + "\n")

# Port tarama fonksiyonu
def port_taramasi(ip, start, end):
    log_yaz("=== Port Taraması Logu ===")
    log_yaz(f"Hedef: {ip}")
    log_yaz(f"Zaman: {datetime.now()}")
    log_yaz(f"Port aralığı: {start}-{end}\n")
    log_yaz(f"[*] Tarama başlatıldı...\n")

    for port in range(start, end + 1):
        try:
            soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soket.settimeout(1.5)  # biraz daha uzun timeout
            sonuc = soket.connect_ex((ip, port))
            if sonuc == 0:
                log_yaz(f"[+] Port {port} AÇIK")
            elif sonuc == 10061:  # Windows sistemlerde connection refused
                log_yaz(f"[-] Port {port} KAPALI (bağlantı reddedildi)")
            else:
                log_yaz(f"[~] Port {port} yanıtsız (timeout veya filtrelenmiş)")
            soket.close()
        except Exception as e:
            log_yaz(f"[!] Port {port} taranırken hata: {e}")
            continue

    log_yaz(f"\n[✓] Tarama tamamlandı. Sonuçlar masaüstüne kaydedildi: {log_file}")

# Ana çalıştırma
if __name__ == "__main__":
    hedef_ip = input("Hedef IP adresini girin (örnek: 192.168.1.1): ").strip()

    if not ip_kontrol(hedef_ip):
        print("Hatalı IP adresi girdiniz. Program kapatılıyor.")
        exit()

    baslangic_port = 1
    bitis_port = 100

    # Log dosyasını temizle ve başlat
    with open(log_file, "w", encoding="utf-8") as f:
        f.write("")  # eski veriyi sil

    port_taramasi(hedef_ip, baslangic_port, bitis_port)
