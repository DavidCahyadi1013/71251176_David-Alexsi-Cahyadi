k1 = input("Masukkan kata pertama: ")
k2 = input("Masukkan kata kedua: ")

k1 = k1.lower()
k2 = k2.lower()

urut1 = sorted(k1)
urut2 = sorted(k2)

if urut1 == urut2:
    print (f"\n'{k1}' dan '{k2}' ADALAH anagram!")
else:
    print (f"\n'{k1}' dan '{k2}' BUKAN anagram!")