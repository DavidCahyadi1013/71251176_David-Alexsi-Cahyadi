def isi (nama):
    with open(nama, encoding='utf-8') as f:
         konten = f.readlines()
    return konten

def beda(teks1,teks2):
     isi1 = isi(teks1)
     isi2 = isi(teks2)
     total = max(len(isi1), len(isi2))
     print (f"File 1 : {len(isi1)} baris")
     print (f"File 2 : {len(isi2)} baris")
     ketemu= False
     for i in range (total):
          if i < len (isi1):
               baris1 = isi1[i].rstrip()
          else:
               baris1 = "Baris Tidak Ada"
          if i < len(isi2):
               baris2 = isi2[i].rstrip()
          else:
               baris2 = "Baris Tidak Ada"
          if baris1 != baris2:
               ketemu = True
               print(f"Baris {i+1} berbeda:")
               print(f" < {teks1}: {baris1}")
               print(f" > {teks2}: {baris2}")
               print()
     if not ketemu:
        print("Kedua file sama persis.")

if __name__ == "__main__":
    try:
         teks1 = input("Nama File pertama: ")
         teks2 = input("Nama File kedua: ")
         beda(teks1,teks2)
    except FileNotFoundError as e:
         print(f"File Tidak Ditemukan: {e}")
    
