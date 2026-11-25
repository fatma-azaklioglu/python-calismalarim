# Soru= Kullanıcıdan hava sıcaklığını alan ve sıcaklığına göre öneride bulunan bir Python programı yazınız.

sicaklik= int(input("Hava sıcaklığını giriniz: "))

if sicaklik >= 30:
    print("Hava çok sıcak, ince giyinin.")
elif sicaklik >= 20:
    print("Hava güzel, dışarı çıkabilirsiniz.")
elif sicaklik >= 10:
    print("Hava serin, ceket giyebilirsiniz.")
else:
    print("Hava soğuk, kalın giyinin.")