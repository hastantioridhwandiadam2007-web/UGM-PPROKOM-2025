A = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ], 
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
]
#Tampilkan elemen lapisan ke 1
print("Lapisan Pertama:", A[1])

#Tampilkan elemen kolom terakhir dari setiap baris dan lapisan
for i in range(len(A)):
    for j in range(len(A[i])):
        print(f"Lapisan {i},", "baris", j, "->", A[i][j][2])