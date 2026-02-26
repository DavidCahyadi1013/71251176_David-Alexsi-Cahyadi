input1 = input ("Masukkan sisi 1: ")
input2 = input ("Masukkan sisi 2: ")
input3 = input ("Masukkan sisi 3: ")

try:
 sisi1 = int (input1)
 sisi2 = int (input2)
 sisi3 = int (input3)

 if sisi1 == sisi2 and sisi2 == sisi3:
    print("Ketiga sisi sama")
 elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
    print("Kedua sisi sama")
 else:
    print("Tidak ada sisi yang sama")

except:
    print("Input yang diberikan tidak valid")