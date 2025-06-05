# 🎃 Matryoshka: Modüler Ağ Güvenliği ve Analiz Aracı

> **“İç içe geçmiş modüllerle, derinlemesine ağ güvenliği ve analiz.”**

---

## 👥 Takım Üyeleri

- **Emin Samet Bozkurt** – `2320191062`  
- **Rıfat Bıyıklı** – `2320191076`  

---

## 🧩 Genel Bakış

**Matryoshka**, çok katmanlı yapısı ve modüler mimarisiyle gelişmiş bir **ağ güvenliği ve analiz aracıdır**.  
Siber güvenlik öğrencilerinin, ağ yöneticilerinin ve güvenlik araştırmacılarının gerçek dünya senaryolarında ihtiyaç duyabileceği tüm temel analiz yeteneklerini entegre şekilde sunar.

Projeye ismini veren “matruşka” felsefesi, her modülün birbiriyle uyumlu çalışabildiği iç içe geçmiş katmanlı yapıyı simgeler.

---

## 🚀 Temel Özellikler

### 📡 Gerçek Zamanlı Ağ Trafiği İzleme
- Scapy ile düşük seviye ağ paketlerinin canlı olarak yakalanması.
- Protokol bazlı trafik sınıflandırması ve özet istatistik üretimi.
- Ağ trafiğinde yoğunluk ve anormalliklerin tespiti.

### 🔍 Port Tarama ve Zafiyet Eşleştirme
- Entegre Nmap modülü ile TCP/UDP port taraması.
- Tespit edilen servislerin versiyonlarına göre CVE (Common Vulnerabilities and Exposures) veritabanı ile eşleştirme.
- Hedef sistemlerde temel zafiyet analizleri.

### 🌐 DNS Trafik Analizi
- DNS sorgularının analiz edilmesi.
- DNS üzerinden veri sızdırma (exfiltration) veya tünelleme (tunneling) gibi kötü niyetli aktivitelerin tespiti.
- Şüpheli domain gruplama ve sınıflandırma.

### 🛡️ IDS (Intrusion Detection System) Yetenekleri
- Temel imza tabanlı saldırı tespiti (örneğin: SYN flood, port scan, DNS amplification).
- Trafik örüntülerine göre anomali tespiti ve alarm üretimi.
- Geliştirilebilir imza sistemi ile esnek tehdit modellemesi.

### 📊 Etkileşimli Görselleştirme
- Canlı veri akışı üzerinden oluşturulan grafikler.
- Plotly destekli etkileşimli trafik haritaları ve zaman serileri.
- Modül bazlı görsel raporlama desteği.

### 🧱 Modüler ve Genişletilebilir Yapı
- Her modül bağımsız çalışabilir, ihtiyaç duyulan fonksiyonlar dinamik olarak yüklenebilir.
- Yeni analiz araçları, dedike Python modülleri şeklinde sisteme kolayca entegre edilebilir.
- Belirli kullanıcı rollerine göre (öğrenci, araştırmacı, uzman) özelleştirilebilir yapı.

---

## 🛠️ Kullanılan Teknolojiler

| Teknoloji | Rolü |
|----------|------|
| **Python** | Projenin ana dili |
| **Scapy** | Paket işleme ve analiz |
| **Nmap** | Ağ taraması ve servis keşfi |
| **Requests** | API ve dış veri kaynaklarına erişim |
| **Matplotlib / Plotly** | Görselleştirme ve grafik üretimi |

---

## 🎯 Neden Matryoshka?

- **Gerçek dünya senaryolarına yakın deneyim** sunar.
- Öğrenmeye açık olanlar için rehber niteliğinde; uzmanlar için yapılandırılabilir derinlikte.
- Akademik projelerden sızma testlerine, laboratuvar simülasyonlarından staj dosyalarına kadar geniş kullanım alanı.
- Tamamen açık kaynak ve geliştirici dostudur.

---

## 📸 Ekran Görüntüleri *(Opsiyonel)*

> Ekran çıktılarınızı bu bölüme ekleyerek projenizin arayüzünü sergileyebilirsiniz.

---

## 🤝 Katkıda Bulunmak

Bu projeye katkı sunmak isteyen geliştiriciler için temel rehber:

1. Depoyu **fork**'layın 🍴  
2. Yeni bir **dal (branch)** oluşturun (`feature/yenilik`)  
3. Değişikliklerinizi yapın ✅  
4. Pull request gönderin 🔁

Kod standartlarına ve modüler yapıya uygun kalmak önemlidir.

---

## 📄 Lisans

Bu proje **MIT Lisansı** ile lisanslanmıştır. Ayrıntılar için `LICENSE` dosyasına göz atabilirsiniz.

---

## ⭐ Destek Ol

Projeyi beğendiyseniz, GitHub’da ⭐ vererek daha fazla geliştiriciye ulaşmamıza yardımcı olabilirsiniz!
