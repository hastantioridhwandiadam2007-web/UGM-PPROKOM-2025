n = int(input("Jumlah nilai yang akan dihitung: "))
daftar_nilai = []

for i in range (0, n):
    x = float(input(f"Masukkan nilai ke-{i+1}: "))
    daftar_nilai.append(x)

nilai = sum(daftar_nilai)/n
print(f"Rata-rata nilai: {nilai}")