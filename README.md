# 📷 Steganografi ile Görsel Üzerinde Bilgi Gizleme

Bu projede, resim dosyalarının içerisine farklı tekniklerle bilgi gizleme (steganografi) yöntemleri uygulanmıştır.

## 🔍 Kullanılan Yöntemler

1. **LSB (Least Significant Bit):** Piksel renk bileşenlerinin son bitine mesaj gömülür.
2. **EXIF Metadata:** JPEG dosyasının metadata alanına mesaj yazılır.

## 🧰 Kullanılan Kütüphaneler

- `stegano`
- `piexif`
- `Pillow (PIL)`

## 📁 Klasör Yapısı

- `lsb/` – LSB tabanlı steganografi örnekleri
- `exif/` – EXIF metadata kullanımı

## 📌 Notlar

- LSB için `.png` önerilir; EXIF için `.jpg` zorunludur.

---

## 🔊 Steganografi ile Ses Dosyası Üzerinde Bilgi Gizleme

### 🔍 Kullanılan Yöntem:
- **LSB (Least Significant Bit):** Ses örneklerinin en düşük anlamlı bitine veri gömülür.

### ✨ Gerçekleştirilen İşlemler:
- **Metin Gömme:** Metin karakterleri bit dizisine çevrilerek ses dosyasına gömüldü.
- **Dosya Gömme:** Herhangi bir dosyanın binary içeriği ses dosyasına LSB yöntemiyle gömüldü ve geri çıkarıldı.

### 🧰 Kullanılan Kütüphaneler:
- `numpy`
- `scipy`

### 📁 Klasör Yapısı:
- `audio_stego/lsb/` – Metin mesajı için LSB uygulamaları
- `audio_stego/file/` – Herhangi bir dosyanın LSB ile gömülmesi ve çıkarılması

## 🎓 Geliştirici
Melisa İrem Çık  