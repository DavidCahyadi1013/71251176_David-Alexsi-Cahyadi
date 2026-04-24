file = input("nama file: ")
handle = open(file)
for line in handle:
    line = line.strip()
    bagian = line.split("||")
    soal = bagian[0].strip()
    kunci = bagian[1].strip()
    print(soal)
    jawab = input("Jawab: ")
    if jawab.lower() == kunci.lower():
        print("Jawaban benar!")
    else:
        print("Jawaban salah!")
handle.close()