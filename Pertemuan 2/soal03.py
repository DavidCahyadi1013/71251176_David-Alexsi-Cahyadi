#Latihan 2.3
def hitung_pendapatan(gaji_per_jam, jam_per_minggu):
    pendapatan_kotor = gaji_per_jam * jam_per_minggu * 5
    pajak = 0.14 * pendapatan_kotor
    pendapatan_bersih = pendapatan_kotor - pajak
    baju_aksesoris = 0.10 * pendapatan_bersih
    alat_tulis = 0.01 * pendapatan_bersih
    sisa_uang = pendapatan_bersih - (baju_aksesoris + alat_tulis)
    sedekah = 0.25 * sisa_uang
    anak_yatim = 0.30 * sedekah
    kaum_dhuafa = 0.70 * sedekah
    return(pendapatan_kotor,pendapatan_bersih,baju_aksesoris,alat_tulis,sedekah,anak_yatim,kaum_dhuafa)

gaji = float(input("Masukkan gaji per jam: "))
jam = int(input("Masukkan jam kerja per minggu: "))

(kotor,bersih,baju,alat_tulis,sedekah,yatim,dhuafa) = hitung_pendapatan(gaji, jam)

print("Pendapatan sebelum pajak        : Rp", kotor)
print("Pendapatan setelah pajak        : Rp", bersih)
print("Pengeluaran baju & aksesoris    : Rp", baju)
print("Pengeluaran alat tulis          : Rp", alat_tulis)
print("Jumlah sedekah                  : Rp", sedekah)
print("Sedekah untuk anak yatim        : Rp", yatim)
print("Sedekah untuk kaum dhuafa       : Rp", dhuafa)