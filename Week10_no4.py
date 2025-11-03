def identitas(nama="", nim=""):
    #FUNGSI INPUT NAMA DAN NIM
    print("=== PROGRAM KALKULATOR SEDERHANA ===")
    print("Silahkan masukkan identitas Anda:")
    nama = str(input("Masukkan nama Anda: "))
    nim = input("Masukkan NIM Anda: ")
    print(f"\nSelamat datang, {nama} (NIM: {nim})!")

def penjumlahan(a, b):
    #FUNGSI PENJUMLAHAN
    return a + b

def pengurangan(a, b):
    #FUNGSI PENGURANGAN
    return a - b

def perkalian(a, b):
    #FUNGSI PERKALIAN
    return a * b

def pembagian(a, b):
    #FUNGSI PEMBAGIAN
    if b != 0:
        return a / b
    else:
        return "Error: Tidak bisa membagi dengan nol!"

def pangkat(a, b):
    #FUNGSI PANGKAT
    return a ** b

def akar_kuadrat(a):
    #FUNGSI AKAR KUADRAT
    if a >= 0:
        return a ** 0.5
    else:
        return "Error: Angka harus positif!"

def main():
    #FUNGSI UTAMA
    identitas()
    while True:
        print("\n=== Kalkulator Sederhana ===")
        print("Pilih operasi:")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Pangkat")
        print("6. Akar Kuadrat")
        print("7. Keluar")
        pilihan = int(input("Masukkan pilihan (1-7): "))

        if pilihan == 1:
            a = float(input("Masukkan angka pertama: "))
            b = float(input("Masukkan angka kedua: "))
            print(f"Hasil: {penjumlahan(a, b)}")
        
        elif pilihan == 2:
            a = float(input("Masukkan angka pertama: "))
            b = float(input("Masukkan angka kedua: "))
            print(f"Hasil: {pengurangan(a, b)}")
        
        elif pilihan == 3:
            a = float(input("Masukkan angka pertama: "))
            b = float(input("Masukkan angka kedua: "))
            print(f"Hasil: {perkalian(a, b)}")
        
        elif pilihan == 4:
            a = float(input("Masukkan angka pertama: "))
            b = float(input("Masukkan angka kedua: "))
            print(f"Hasil: {pembagian(a, b)}")
        
        elif pilihan == 5:
            a = float(input("Masukkan angka dasar: "))
            b = float(input("Masukkan pangkat: "))
            print(f"Hasil: {pangkat(a, b)}")
        
        elif pilihan == 6:
            a = float(input("Masukkan angka: "))
            print(f"Hasil: {akar_kuadrat(a)}")

        elif pilihan == 7:
            print("Terima kasih telah menggunakan kalkulator.")
            break

        elif pilihan == 6:
            num = float(input("Masukkan angka: "))
            print(f"Hasil: {akar_kuadrat(num)}")

        else:
            print("Pilihan tidak valid, silakan coba lagi.")

while True:
    main()