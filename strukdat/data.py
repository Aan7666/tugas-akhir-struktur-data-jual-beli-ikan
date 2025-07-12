from collections import deque, defaultdict
import csv
from datetime import datetime
ikan_list = [
    {'kode': 'IK01', 'nama': 'Lele', 'harga': 25000},
    {'kode': 'IK02', 'nama': 'Bandeng', 'harga': 20000}
]

keranjang_beli = []
antrian_transaksi = deque()
penghasilan_harian = defaultdict(float)
#
def tambah_ikan():
    kode = input("Masukkan kode ikan baru: ").strip().upper()
    if any(ikan['kode'] == kode for ikan in ikan_list):
        print("Kode ikan sudah ada.")
        return

    nama = input("Masukkan nama ikan: ").strip().title()
    try:
        harga = int(input("Masukkan harga per kg: "))
        if harga <= 0:
            raise ValueError
    except ValueError:
        print("Harga tidak valid.")
        return

    ikan_list.append({'kode': kode, 'nama': nama, 'harga': harga})
    print(f"Ikan {nama} berhasil ditambahkan.")
    
    with open('ikan.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), kode, nama, harga])
#update
def update_harga_ikan():
    kode = input("Masukkan kode ikan yang ingin diubah harganya: ").strip().upper()
    ikan = next((i for i in ikan_list if i['kode'] == kode), None)

    if not ikan:
        print("Kode ikan tidak ditemukan.")
        return

    print(f"Harga saat ini untuk {ikan['nama']}: Rp{ikan['harga']}")
    try:
        harga_baru = int(input("Masukkan harga baru: "))
        if harga_baru <= 0:
            raise ValueError
    except ValueError:
        print("Harga tidak valid.")
        return

    ikan['harga'] = harga_baru
    print(f"Harga ikan {ikan['nama']} berhasil diperbarui menjadi Rp{harga_baru}.")
#
def hapus_ikan():
    kode = input("Masukkan kode ikan yang ingin dihapus: ").strip().upper()
    ikan = next((i for i in ikan_list if i['kode'] == kode), None)
    if not ikan:
        print("Kode ikan tidak ditemukan.")
        return
# Hapus ikan dari daftar
    ikan_list.remove(ikan)
    print(f"Ikan dengan kode {kode} berhasil dihapus.")
    with open('log_hapus_ikan.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), ikan['kode'], ikan['nama'], ikan['harga']])
