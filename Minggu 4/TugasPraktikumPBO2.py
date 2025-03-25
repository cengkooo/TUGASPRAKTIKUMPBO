def tambah_tugas(daftar_tugas):
    tugas = input("Masukkan tugas yang ingin ditambahkan: ").strip()
    
    if not tugas:
        raise ValueError("Error: Tugas tidak boleh kosong.")
    
    daftar_tugas.append(tugas)
    print("\nTugas berhasil ditambahkan!\n")


def hapus_tugas(daftar_tugas):
    if not daftar_tugas:
        raise IndexError("Error: Daftar tugas kosong, tidak ada yang bisa dihapus.")

    try:
        nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        
        if nomor < 1 or nomor > len(daftar_tugas):
            raise IndexError(f"Error: Tugas dengan nomor {nomor} tidak ditemukan.")
        
        tugas_dihapus = daftar_tugas.pop(nomor - 1)
        print(f"\nTugas '{tugas_dihapus}' berhasil dihapus!\n")
    
    except ValueError:
        print("Error: Masukkan angka yang valid.\n")


def tampilkan_tugas(daftar_tugas):
    if not daftar_tugas:
        print("\nDaftar tugas kosong.\n")
    else:
        print("\nDaftar Tugas:")
        for i, tugas in enumerate(daftar_tugas, start=1):
            print(f"{i}. {tugas}")
        print()


def main():
    daftar_tugas = []

    while True:
        print("Pilih aksi:")
        print("1. Tambah tugas")
        print("2. Hapus tugas")
        print("3. Tampilkan daftar tugas")
        print("4. Keluar")

        pilihan = input("\nMasukkan pilihan (1/2/3/4): ").strip()

        try:
            if pilihan == "1":
                tambah_tugas(daftar_tugas)
            elif pilihan == "2":
                hapus_tugas(daftar_tugas)
            elif pilihan == "3":
                tampilkan_tugas(daftar_tugas)
            elif pilihan == "4":
                print("Keluar dari program.")
                break
            else:
                raise ValueError("Error: Pilihan tidak valid. Masukkan angka 1-4.")
        
        except Exception as e:
            print(e, "\n")


if __name__ == "__main__":
    main()
