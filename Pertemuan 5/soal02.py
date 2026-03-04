#Latihan 5.2
def cek_digit_belakang(a,b,c):
    digita = a % 10 
    digitb = b % 10
    digitc = c % 10
    if digita == digitb or digita == digitc or digitb == digitc:
        return True
    else:
        return False
    
a1 = int(input("Masukkan bilangan pertama: "))
a2 = int(input("Masukkan bilangan kedua: "))
a3 = int(input("Masukkan bilangan ketiga: "))

hasil = cek_digit_belakang(a1,a2,a3)
print ("Hasil:", hasil)