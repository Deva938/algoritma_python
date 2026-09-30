# a) Data awal minimal 3 kontak (Dictionary)
buku_kontak = {
    "Andi": "081234567890",
    "Budi": "088765432109",
    "Citra": "085123456789"
}

# c) Gunakan while loop untuk menu berulang
while True:
    print("\n=== MENU BUKU KONTAK ===")
    print("1. Lihat semua kontak")
    print("2. Cari kontak by nama")
    print("3. Tambah kontak baru")
    print("4. Hapus kontak")
    print("5. Keluar")
    
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == '1':
        # Lihat semua kontak
        print("\n--- Daftar Kontak ---")
        if not buku_kontak:
            print("Buku kontak masih kosong.")
        else:
            for nama, hp in buku_kontak.items():
                print(f"- {nama} : {hp}")

    elif pilihan == '2':
        # b) & d) Cari kontak menggunakan .get()
        nama_cari = input("\nMasukkan nama kontak yang dicari: ")
        hasil = buku_kontak.get(nama_cari)
        
        if hasil:
            print(f"Nomor HP {nama_cari}: {hasil}")
        else:
            print(f"Kontak atas nama '{nama_cari}' tidak ditemukan.")

    elif pilihan == '3':
        # Tambah kontak baru
        nama_baru = input("\nMasukkan nama kontak baru: ")
        hp_baru = input("Masukkan nomor HP: ")
        buku_kontak[nama_baru] = hp_baru
        print(f"Kontak '{nama_baru}' berhasil ditambahkan!")

    elif pilihan == '4':
        # Hapus kontak
        nama_hapus = input("\nMasukkan nama kontak yang ingin dihapus: ")
        if nama_hapus in buku_kontak:
            del buku_kontak[nama_hapus]
            print(f"Kontak '{nama_hapus}' berhasil dihapus.")
        else:
            print(f"Kontak atas nama '{nama_hapus}' tidak ditemukan.")

    elif pilihan == '5':
        # Keluar dari program
        print("\nTerima kasih telah menggunakan program Buku Kontak!")
        break

    else:
        print("\nPilihan tidak valid! Silakan masukkan angka 1-5.")