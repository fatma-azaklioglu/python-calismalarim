# Soru: Haftanın günleri 0 (Pazartesi) ile 6 (Pazar) arasında numaralandırılmıştır. Kullanıcıdan kargonun yola çıktığı günü (0-6), saatini (0-23) ve yolculuğun kaç saat süreceğini alarak, kargonun haftanın kaçıncı günü ve saat kaçta teslim edileceğini hesaplayan program yazınız.

# Denemek için örnek girdi: 5, 18, 35 -> Çıktı: 0. gün, Saat 05:00

gün= int(input("Başlangıç günü: "))
saat= int(input("Başlangıç saati: "))
süre= int(input("Yolculuk kaç saat sürüyor ? "))

toplam_saat= gün * 24 + saat + süre
teslim_gün=(toplam_saat // 24) % 7
teslim_saat= toplam_saat % 24
print(f"Teslimat zamanı: {teslim_gün}. gün, Saat {teslim_saat:02d}:00")
