from transaksi import transaksi_pembeli
from keranjang import tampilkan_keranjang
from data import tambah_ikan, hapus_ikan, update_harga_ikan

while True:
    print("\n=== Menu Jual Beli Ikan ===")
    print("1. Pelanggan membeli ikan")
    print("2. Lihat hasil semua pembelian")
    print("3. Kelola daftar ikan (tambah/hapus/update)")
    print("0. Keluar")

    pilihan = input("Pilih menu: ")
    if pilihan == '1':
        transaksi_pembeli()
    elif pilihan == '2':
        tampilkan_keranjang()
    elif pilihan == '3':
        print("\n--- Kelola Daftar Ikan ---")
        print("1. Tambah ikan baru")
        print("2. Hapus ikan dari daftar")
        print("3. Update harga ikan")
        sub_pilihan = input("Pilih aksi: ")

        if sub_pilihan == '1':
            tambah_ikan()
        elif sub_pilihan == '2':
            hapus_ikan()
        elif sub_pilihan == '3':
            update_harga_ikan()
        else:
            print("Pilihan tidak valid di submenu.")
    elif pilihan == '0':
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.")
