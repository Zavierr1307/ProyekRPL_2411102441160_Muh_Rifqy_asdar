def tampilkan_menu():
    """Menampilkan pilihan operasi ke user."""
    print("\nPilih operasi:")
    print("1. Tambah (+)")
    print("2. Kurang (-)")
    print("3. Kali (*)")
    print("4. Bagi (/)")


def hitung(angka1, angka2, pilihan):
    """Melakukan perhitungan berdasarkan pilihan user."""
    if pilihan == "1":
        return angka1 + angka2
    elif pilihan == "2":
        return angka1 - angka2
    elif pilihan == "3":
        return angka1 * angka2
    elif pilihan == "4":
        if angka2 == 0:
            return None
        return angka1 / angka2
    else:
        return "invalid"


def main():
    """Fungsi utama untuk menjalankan kalkulator."""
    while True:
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
        except ValueError:
            print("Input harus berupa angka!")
            continue

        tampilkan_menu()
        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        hasil = hitung(angka1, angka2, pilihan)

        if hasil == "invalid":
            print("Pilihan tidak valid!")
        elif hasil is None:
            print("Error: Tidak bisa membagi dengan nol!")
        else:
            print("Hasil:", hasil)

        ulang = input("Mau hitung lagi? (y/n): ").lower()
        if ulang != "y":
            print("Program selesai.")
            break


# Menjalankan program
main()