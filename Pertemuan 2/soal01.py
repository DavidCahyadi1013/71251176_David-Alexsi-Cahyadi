#Latihan 2.1
def hitung_berat_badan(bmi: float, tinggi: float):
    return (bmi * (tinggi**2))
bmi= float(input("BMI yang diinginkan:"))
tinggi = float(input("Tinggi Badan (meter):"))
hasil = hitung_berat_badan (bmi,tinggi)
print ("Berat badan yang dibutuhkan:", hasil,"Kg")