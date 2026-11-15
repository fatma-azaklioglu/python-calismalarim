"""
Soru= Kullanıcıdan toplam dakika bilgisini ve bunun kaç saat, kaç dakika ettiğini hesaplayıp ekrana yazdıran programı yazınız.

Denemek için örnek girdi: 135 -> Çıktı: 2 saat 15 dakika
"""

toplam_dakika= int(input("Toplam dakikayı giriniz: "))
saat= toplam_dakika // 60
dakika= toplam_dakika % 60

print(f"{saat} saat {dakika} dakika")

