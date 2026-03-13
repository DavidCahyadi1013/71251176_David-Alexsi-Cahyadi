#Latihan 6.3
matkullu = int(input("Berapa jumlah mata kuliah? "))
bobot = 0
sks = 3
tb = 0

for i in range(1, matkullu +1):
    nilai =  input(f"Nilai MK {i}: ").upper()
    if nilai == "A":
        bobot = 4
    elif nilai == "B":
        bobot = 3
    elif nilai == "C":
        bobot = 2
    elif nilai == "D":
        bobot = 1
    else:
        bobot = 0

    tb += bobot * sks

ts = matkullu * sks
ips = tb / ts

print(f"Nilai IPS anda smester ini {ips:.2f}")
