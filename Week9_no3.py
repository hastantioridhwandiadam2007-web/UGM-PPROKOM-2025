import array as array
import numpy as np
A = [
 [2, 4, 6],
 [1, 3, 5]
]
B = [
 [1, 1, 1],
 [2, 2, 2]
]
#Penjumlahan dan pengurangan Matriks A dan B menggunakan NumPy
array_A = np.array(A)
array_B = np.array(B)
penjumlahan = array_A + array_B
pengurangan = array_A - array_B
print("Hasil Penjumlahan Matriks A dan B:")
print(penjumlahan)
print("Hasil Pengurangan Matriks A dan B:")
print(pengurangan)

#Hitung perkalian matriks A × Bᵀ
perkalian = array_A.dot(array_B.T)
print("Hasil Perkalian Matriks A dan Bᵀ:")
print(perkalian)