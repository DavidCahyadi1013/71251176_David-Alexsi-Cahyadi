#Latihan 5.1
def cek_angka(a,b,c):
    berbeda = (a != b) and (a != c) and (b != c)
    sama = (a +b == c) or (a + c == b) or (b + c == a )
    return berbeda and sama


#Tempat tes input
print(cek_angka(2,3,5))
print(cek_angka(4,4,8))
print(cek_angka(1,2,4))
print(cek_angka(5,2,3))