from datetime import datetime
from data import ikan_list, keranjang_beli, antrian_transaksi, penghasilan_harian

def transaksi_pembeli():
    if not ikan_list:
        print("Daftar ikan kosong. Silakan tambahkan ikan terlebih dahulu.")
        return
    nama_pembeli = input("Masukkan nama pembeli: ").strip()
    if not nama_pembeli.isalpha():
        print("Nama berupa huruf saja.")
        return

    pembeli = next((p for p in keranjang_beli if p['nama'] == nama_pembeli), None)
    if not pembeli:
        pembeli = {'nama': nama_pembeli, 'belanja': []}
        keranjang_beli.append(pembeli)

    while True:
        print("\n--- Daftar Ikan Tersedia ---")
        for ikan in ikan_list:
            print(f"{ikan['kode']} | {ikan['nama']} | Rp{ikan['harga']}/kg")

        kode = input("Masukkan kode ikan (contoh : IK01) , klik 'selesai' bila ingin berhenti transaksi: ").upper()
        if kode == 'SELESAI':
            print(f"Transaksi untuk {nama_pembeli} selesai.")
            break

        ikan = next((i for i in ikan_list if i['kode'] == kode), None)
        if not ikan:
            print("Kode ikan tidak ditemukan.")
            continue

        try:
            jumlah = float(input("Masukkan jumlah dalam kg: "))
            if jumlah <= 0:
                raise ValueError
        except ValueError:
            print("Jumlah tidak valid.")
            continue

        item = next((b for b in pembeli['belanja'] if b['kode'] == kode), None)
        if item:
            item['jumlah'] += jumlah
        else:
            pembeli['belanja'].append({
                'kode': kode,
                'nama': ikan['nama'],
                'harga': ikan['harga'],
                'jumlah': jumlah
            })

        waktu = datetime.now()
        total = jumlah * ikan['harga']
        transaksi = {
            'waktu': waktu.strftime('%Y-%m-%d %H:%M:%S'),
            'pembeli': nama_pembeli,
            'kode': kode,
            'nama': ikan['nama'],
            'jumlah': jumlah,
            'harga': ikan['harga'],
            'total': total
        }
        antrian_transaksi.append(transaksi)
        tanggal = waktu.strftime('%Y-%m-%d')
        penghasilan_harian[tanggal] += total

        print(f"{nama_pembeli} membeli {jumlah} kg {ikan['nama']}")
