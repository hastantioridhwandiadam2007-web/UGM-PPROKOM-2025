buah_buahan = {
    "Apel": 15000,
    "Jeruk": 10000,
    "Anggur": 25000
    }
print("Dictionary buah_buahan awal:", buah_buahan)

# 1) Tampilkan harga jeruk.
print("\nHarga Jeruk adalah Rp", buah_buahan['Jeruk'])

# Tambahkan mangga dengan harga Rp12.000.
buah_buahan['Mangga'] = 12000
print("\nDictionary buah_buahan terbaru:", buah_buahan)

# Perbarui harga anggur menjadi Rp20.000.
buah_buahan['Anggur'] = 20000
print("\nDictionary buah_buahan terbaru:", buah_buahan)

# Hapus buah jeruk.
del buah_buahan['Jeruk']
print("\nDictionary buah_buahan terbaru:", buah_buahan)

