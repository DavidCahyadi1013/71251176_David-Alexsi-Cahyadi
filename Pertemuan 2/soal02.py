#Latihan 2.2
def fungsi_x(x: int):
    return (2 * x**3 + 2 * x + (15 / x))

x = int(input("Input nilai x: "))
hasil = fungsi_x(x)
print("Hasil dari f(X):", hasil)