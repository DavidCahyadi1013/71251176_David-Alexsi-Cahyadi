data = eval(input("Masukkan Data: "))
print("Data:", data)
print()

na,ni,al = data
print("NIM :",ni)
print("NAMA :",na)
print("ALAMAT :",al)
print()

tni= tuple(ni)
print("NIM:", tni)
print()

nama = tuple(na.split()[0][1:])
print("NAMA DEPAN:", nama)
print()

aman = tuple(na.split()[::-1])
print("NAMA TERBALIK:", aman)
