# Program Persyaratan SIM
umur = int(input("Masukkan umur Anda = "))
nilai = int(input("Masukkan nilai tes Anda = "))
lulus = "Selamat anda berhak mendapatkan SIM anda"
gagal = "Maaf, anda tidak berhak mendapatkan SIM anda\nSilakan coba lagi bulan atau tahun depan"
if umur >= 17:
    if (nilai < 60):
        print()
        print(gagal)
    else:
        print()
        print(lulus)
else:
    print()
    print(gagal)

