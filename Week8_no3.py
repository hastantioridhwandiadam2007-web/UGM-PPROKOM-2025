from array import array                      
arr_nilai = array('i', [60, 70, 80, 90, 100])
panjang = len(arr_nilai)
count = 0

print("Isi Array arr_nilai:")                 
for nilai in arr_nilai:
    print(nilai)
    count += nilai

print("Jumlah nilai:", panjang)               
print("Total semua nilai:", count)            
print("Rata-rata nilai:", count / panjang)    