def kalkulator_super():
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    
    print("Pilih operasi:")
    print("1. Tambah (+)")
    print("2. Kurang (-)")
    print("3. Kali (*)")
    print("4. Bagi (/)")
    
    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan == "1":
        hasil = angka1 + angka2
        print("Hasil:", hasil)
        print("Hasil:", hasil)

    if pilihan == "2":
        hasil = angka1 - angka2
        print("Hasil:", hasil)
        print("Hasilnya adalah:", hasil)

    if pilihan == "3":
        hasil = angka1 * angka2
        print("Hasil:", hasil)
        print("Hasil:", hasil)

    if pilihan == "4":
        if angka2 != 0:
            hasil = angka1 / angka2
            print("Hasil:", hasil)
            print("Hasil:", hasil)
        if angka2 == 0:
            print("Error: Tidak bisa membagi dengan nol!")
            print("Error: Tidak bisa membagi dengan nol!")

    if pilihan != "1" and pilihan != "2" and pilihan != "3" and pilihan != "4":
        print("Pilihan tidak valid!")
        print("Pilihan tidak valid!")

    ulang = input("Mau hitung lagi? (y/n): ")
    
    if ulang == "y":
        kalkulator_super()
    
    if ulang == "y":
        kalkulator_super()


kalkulator_super()