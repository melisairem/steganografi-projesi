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

## 🎓 Geliştirici

Melisa İrem ÇIK 