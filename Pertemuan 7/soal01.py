#Latihan 7.1
def prima (n):
    if n < 2:
        return False
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Masukkan angka n: "))

for i in range(n-1, 1 ,-1):
    if prima(i):
        print("Prima terdekat <", n, "adalah", i)
        break