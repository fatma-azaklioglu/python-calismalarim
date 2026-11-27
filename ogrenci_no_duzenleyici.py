# Soru= Kullanıcı öğrenci numarasını " az260981 " gibi yazsın. 
# Başındaki ve sonundaki boşlukları temizleyip büyük harfe çevirin; bölüm kodunu ve uzunluğu yazdırın.

ogrenci_no= input("Öğrenci numarasını girin: ")
duzenli_no= ogrenci_no.strip().upper()
bolum_kodu= duzenli_no[:2]
uzunluk= len(duzenli_no)

print("Düzenlenmiş numara:", duzenli_no)
print("Bölüm kodu:", bolum_kodu)
print("Uzunluk:", uzunluk)