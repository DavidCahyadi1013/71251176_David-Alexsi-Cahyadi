import re
def ku (file):
    with open(file, "r", encoding="utf-8") as f:
        isi = f.read()
    
    semua = re.findall(r'\b\w+\b', isi.lower())
    ku = list(dict.fromkeys(semua))
    return isi, ku
file = input ("Masukkan nama file artikel/berita (.txt): ")
isi, hasil = ku(file)

print(f"\n======= ISI BERITA '{file}' =======")
print(isi)
print(f"\n======= KATA UNIK =======")
print(hasil)
print(f"\nTotal kata unik: {len(hasil)}")
