#Latihan 7.2
import math

n = int(input("Masukkan angka n: "))

for i in range (n, 0, -1):
    faktor =  math.factorial(i)

    print(faktor, end=" ")

    for j in range(i, 0, -1):
        print(j, end=" ")
    print()