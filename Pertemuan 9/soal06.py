import re
import random
import string

print("Berikut adalah daftar email dan nama pengguna dari mailing list: ")

lines = []
while True:
    baris = input()
    if baris == "":
        break
    lines.append(baris)

t= "\n".join(lines)
email = re.findall(r'[a-zA-Z0-9._]+@[a-zA-Z0-9]+(?:\.[a-zA-Z]+)+', t)

def pw():
    ch= string.ascii_letters + string.digits
    return ''.join(random.choice(ch) for _ in range(8))

for i in email:
    nama = i.split('@')[0]
    sandi= pw()
    print(f"{i} username: {nama}, password: {sandi}")