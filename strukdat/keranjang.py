import csv
from data import keranjang_beli

def tampilkan_keranjang(nama_file='output_keranjang.csv'):
    if not keranjang_beli:
        print("\nBelum ada pembelian.")
        return

    print("\n--- Daftar Belanja Semua Pembeli ---")
    with open(nama_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nama Pembeli', 'Kode Ikan', 'Nama Ikan', 'Jumlah (kg)', 'Harga/kg', 'Subtotal'])

        for pembeli in keranjang_beli:
            print(f"\nPembeli: {pembeli['nama']}")
            total = 0
            for item in pembeli['belanja']:
                subtotal = item['jumlah'] * item['harga']
                print(f"  - {item['nama']} {item['jumlah']} kg x Rp{item['harga']} = Rp{subtotal}")
                writer.writerow([
                    pembeli['nama'],
                    item['kode'],
                    item['nama'],
                    item['jumlah'],
                    item['harga'],
                    subtotal
                ])
                total += subtotal
            print(f"  Total: Rp{total}")
