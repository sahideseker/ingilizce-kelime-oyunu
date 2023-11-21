import random

kelime_anlam = {}

with open("tek_sayfa.txt", "r", encoding="utf-8") as dosya:
    for satir in dosya:
        kelime, anlam = satir.strip().split(":")
        kelime_anlam[kelime] = anlam

dogru_tahminler = {}
yanlis_tahminler = {}

kalan_kelimeler = list(kelime_anlam.keys())

print("Doğru bildiyseniz tahmininizi yazın, çıkmak için 'exit' yazın")

while kalan_kelimeler:
    rastgele_kelime = random.choice(kalan_kelimeler)
    turkce_anlam = kelime_anlam[rastgele_kelime]

    tahmin = input(f"'{rastgele_kelime}' kelimesinin anlamını tahmin edin:")

    if tahmin.lower() == "exit":
        break

    if tahmin.lower() == turkce_anlam.lower():
        print("Doğru tahmin! Tebrikler!")
        dogru_tahminler[rastgele_kelime] = turkce_anlam
    else:
        print("Yanlış tahmin. Doğru cevap:", turkce_anlam)
        yanlis_tahminler[rastgele_kelime] = turkce_anlam

    kalan_kelimeler.remove(rastgele_kelime)

print("\nTüm kelimeler tamamlandı! İşte istatistikler:")
print("\nDoğru Tahminler:")
for kelime, anlam in dogru_tahminler.items():
    print(f"{kelime}: {anlam}")

print("\nYanlış Tahminler:")
for kelime, anlam in yanlis_tahminler.items():
    print(f"{kelime}: {anlam}")
