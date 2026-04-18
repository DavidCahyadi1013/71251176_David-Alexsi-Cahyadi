import re
from datetime import datetime

t = input("Masukkan teks: ")
tgl = re.findall (r'\d{4}-\d{2}-\d{2}', t)

sekarang = datetime.now()
for i in tgl:
    tg = datetime.strptime(i, '%Y-%m-%d')
    selisih = abs((sekarang - tg).days)
    print(f"{tg} selisih {selisih} hari")