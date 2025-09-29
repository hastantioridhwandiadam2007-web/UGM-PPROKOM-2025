print("\nDictionary Nilai Mahasiswa:")
nilai_mahasiswa = {
    "Aba" : 85,   #Kurang Koma
    "Abi" : 90,
    "Abu" : 78
}
print(nilai_mahasiswa)

print("\nMenambahkan Nilai Abe:")
nilai_mahasiswa["Abe"] = 88   # Kurang kurung Kurawal {}
print(nilai_mahasiswa)

print("\nMengupdate nilai Abu:")
nilai_mahasiswa["Abu"] = 87   # Salah posisi Key
print(nilai_mahasiswa)

print("\nMencetak semua Nilai:")
for nama, nilai in nilai_mahasiswa.items():   # Kurang .items()
    print(f"Nilai {nama} adalah {nilai}")

'''print("\nDictionary Nilai Mahasiswa:")
nilai_mahasiswa = {
    "Aba" : 85   #Kurang Koma
    "Abi" : 90,
    "Abu" : 78
}
print(nilai_mahasiswa)

print("\nMenambahkan Nilai Abe:")
nilai_mahasiswa.update("Abe": 88)   # Kurang kurung Kurawal {}
print(nilai_mahasiswa)

print("\nMengupdate nilai Abu:")
nilai_mahasiswa[0] = 87   # Salah posisi Key
print(nilai_mahasiswa)

print("\nMencetak semua Nilai:")
for nama, nilai in nilai_mahasiswa:   # Kurang .items()
    print(f"Nilai {nama} adalah {nilai}")'''