while True:
    print("Pilih program")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

    pilihan = int(input("Masukkan pilihan : "))

    if pilihan == 5:
        print("Terima kasih telah menggunakan kalkulator Putri Dwi Aprilia")
        break
    elif 1 <= pilihan <= 4:
        nilai1 = float(input("Masukkan nilai pertama : "))
        nilai2 = float(input("Masukkan nilai kedua : "))

        if pilihan == 1:
            hasil = nilai1 + nilai2
            print("Hasil penjumlahan : ", hasil)
        elif pilihan == 2:
            hasil = nilai1 - nilai2
            print("Hasil pengurangan : ", hasil)
        elif pilihan == 3:
            hasil = nilai1 * nilai2
            print("Hasil perkalian : ", hasil)
        elif pilihan == 4:
            hasil = nilai1 / nilai2
            print("Hasil pembagian : ", hasil)
    else:
        print("Error: Pembagian oleh nol tidak diperbolehkan")