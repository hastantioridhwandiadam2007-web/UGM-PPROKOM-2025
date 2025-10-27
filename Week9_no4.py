import array as array
import numpy as np

nilai = [
    [85, 80, 90],
    [78, 82, 88],
    [92, 90, 94],
    [70, 68, 72],
    [88, 85, 84],
    [60, 75, 70],
    [95, 92, 98],
    [74, 70, 76],
    [81, 85, 83],
    [69, 72, 70],
    [90, 88, 92],
    [76, 80, 79],
    [84, 86, 90],
    [79, 82, 85],
    [67, 70, 68],
    [91, 94, 93],
    [73, 78, 75],
    [87, 84, 89],
    [65, 68, 70],
    [93, 90, 95],
    [77, 80, 78],
    [82, 84, 88],
    [89, 85, 90],
    [71, 74, 76]
]

#Tampilkan seluruh nilai dengan format berikut menggunakan nested loop
for i in range(len(nilai)):
    print(f"Mahasiswa ke-{i + 1} | ", end="")
    for j in range(1):
        print(f"Tugas:{nilai[i][0]} |", f"UTS:{nilai[i][1]} |", f"UAS:{nilai[i][2]}", sep= " ", end=" ")
    print()  # Pindah ke baris berikutnya setelah menampilkan semua nilai mahasiswa

#NumPy: Rata-rata, Nilai tertinggi, Nilai terendah
array_nilai = np.array(nilai)
rata_rata = np.mean(array_nilai)
nilai_tertinggi = np.max(array_nilai)
nilai_terendah = np.min(array_nilai)

print(f"\nRata-rata keseluruhan nilai: {rata_rata}")
print(f"Nilai tertinggi: {nilai_tertinggi}")
print(f"Nilai terendah: {nilai_terendah}")