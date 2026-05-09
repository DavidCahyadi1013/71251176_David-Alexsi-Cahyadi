d = {}
n = int (input("Jumlah data : "))

for i in range(n):
    k = int(input(f"Key ke-{i+1} : "))
    v = int(input(f"Value ke-{i+1} : "))
    d[k] = v

print(f"{'key':<8}{'value':<12}{'item'}")

for i,(k,v) in enumerate(d.items(), start=1):
    print(f"{k:<8}{v:<12}{i}")