kamus = dict()
file = input("Enter a file name: ")
try:
    buka = open(file)
except FileNotFoundError:
    print("File not found:", file)
    exit()

for i in buka:
    kata = i.split()
    if len(kata) < 2 or kata [0] != 'From':
        continue
    else:
        jam = kata[5].split(':')[0]
        if jam not in kamus:
            kamus[jam] = 1
        else:
            kamus[jam] += 1
ubah = list()
for k, v in list(kamus.items()):
    ubah.append((k, v))
ubah.sort()

for jam, jumlah in ubah:
    print(jam, jumlah)