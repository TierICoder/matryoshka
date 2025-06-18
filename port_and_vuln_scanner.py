import nmap
import requests
import re

# İsteğe bağlı: NVD API Key'in varsa buraya gir
NVD_API_KEY = ""  # "apikey-buraya"

def scan_ports(target_ip, scan_type="tcp"):
    nm = nmap.PortScanner()
    if scan_type == "tcp":
        nm.scan(target_ip, arguments="-sV -T4")
    elif scan_type == "udp":
        nm.scan(target_ip, arguments="-sU -sV")
    else:
        raise ValueError("Desteklenmeyen tarama türü")

    results = []
    for proto in nm[target_ip].all_protocols():
        ports = nm[target_ip][proto].keys()
        for port in ports:
            serv = nm[target_ip][proto][port]
            results.append({
                "port": port,
                "proto": proto,
                "name": serv.get("name", ""),
                "product": serv.get("product", ""),
                "version": serv.get("version", ""),
                "cpe": serv.get("cpe", "")
            })
    return results

def query_nvd_cves(product, version):
    if not product or not version:
        return []

    # Basit formatlama
    keyword = f"{product} {version}"
    print(f"🔍 NVD üzerinde aranıyor: {keyword}")

    headers = {}
    if NVD_API_KEY:
        headers["apiKey"] = NVD_API_KEY

    try:
        url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={keyword}&resultsPerPage=5"
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            data = response.json()
            return [{
                "cve_id": item["id"],
                "desc": item.get("descriptions", [{}])[0].get("value", ""),
                "severity": item.get("metrics", {}).get("cvssMetricV31", [{}])[0].get("cvssData", {}).get("baseSeverity", "UNKNOWN")
            } for item in data.get("vulnerabilities", [])]
        else:
            return []
    except Exception as e:
        print(f"Hata (NVD isteği): {e}")
        return []

def main():
    target = input("🎯 Hedef IP girin: ").strip()
    scan_type = input("📡 Tarama tipi [tcp/udp]: ").strip().lower()

    print(f"\n🚀 {scan_type.upper()} port taraması başlatılıyor: {target}")
    results = scan_ports(target, scan_type)

    if not results:
        print("Hiçbir açık port bulunamadı.")
        return

    print("\n📊 Açık Portlar ve Servisler:")
    for r in results:
        print(f"[{r['proto'].upper()}] {r['port']}: {r['product']} {r['version']}")

    print("\n🛡️ CVE Eşleştirmeleri:")
    for r in results:
        cves = query_nvd_cves(r['product'], r['version'])
        if cves:
            print(f"\n[{r['port']}] {r['product']} {r['version']}:")
            for cve in cves:
                print(f"  🔴 {cve['cve_id']} - {cve['severity']}\n      {cve['desc'][:80]}...")
        else:
            print(f"[{r['port']}] {r['product']} {r['version']} için CVE bulunamadı.")

if __name__ == "__main__":
    main()
