#Menggunakan Nested List Comprehension untuk membuat matriks identitas
baris, kolom = 4, 4
array2D = [[1 if i == j else 0 for i in range(kolom)] for j in range(baris)]
for t in array2D:
    print(t)

#Tambahkan variabel input n, agar pengguna bisa menentukan ukuran matriks identitas dan menampilkan matriks yang baru
n = int(input("Masukkan ukuran matriks baru (n x n): "))
matriks_baru = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
print(f"Matriks Identitas {n}x{n}:")
for baris in matriks_baru:
    print(baris)