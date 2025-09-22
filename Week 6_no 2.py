nilai = set({3,6,9,2,5,7})
tambahan = {1,4,8,10}
kurangi = {1,3,4,5,7,8,10}
#Proses Penambahan
nilai.update(tambahan)
print(nilai)
#Proses Pengurangan
nilai.symmetric_difference_update(kurangi)
print(nilai)