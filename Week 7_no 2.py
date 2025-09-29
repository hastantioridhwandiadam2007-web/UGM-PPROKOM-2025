stok_buku = {
    "Harry Potter" : 10,
    "Laskar Pelangi" : 15,
    "Bumi Manusia" : 7,
    "Dilan 1990": 20
}
print("Stok buku saat ini:")
for judul, stok in stok_buku.items():
    print(f"Buku: {judul} - Stok: {stok}")

a = str(input("\nTambahkan judul buku:"))
b = int(input("Tambahkan stok buku:"))
stok_buku[a] = b
print(f"Buku {a} berhasil ditambahkan dengan stok {b}")

print("\nStok buku terbaru:")
for judul, stok in stok_buku.items():
    print(f"Buku: {judul} - Stok: {stok}")
