kalimat = input("Masukkan kalimat: ")
kata = input("Masukkan kata yang dicari: ")

kalimat = kalimat.lower()
kata = kata.lower()

kalimat = kalimat.replace(".","")

pecah = kalimat.split()
jumlah = pecah.count(kata)
print(f"\n{kata} ada {jumlah} buah")