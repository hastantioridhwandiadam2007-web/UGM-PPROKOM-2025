list_nama = []

for i in range (5):
    nama = str(input(f"Masukkan nama orang ke-{i+1}: "))
    list_nama.append(nama)

print("\nDaftar nama yang telah dimasukkan:")
for indeks, nama in enumerate(list_nama):
    print(f"{indeks+1}. {nama}")

ganti = int(input("Mau ganti nama teman nomor berapa?:")) #Tanya Asdos: Berulang atau sekali?
nama_baru = str(input("Masukkan nama baru: "))
list_nama[ganti-1] = nama_baru

print("\nDaftar nama terbaru:")
for indeks, nama in enumerate (list_nama):
    print(f"{indeks+1}. {nama}")