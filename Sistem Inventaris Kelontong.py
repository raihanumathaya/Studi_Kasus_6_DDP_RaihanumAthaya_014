import json
import os

file_name = "Data.json"


def muat_data():
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def simpan_data(data):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def tambah_barang(data):
    nama_barang = input("Masukkan nama barang baru: ")
    jumlah_stok = input("Masukkan jumlah stok baru: ")
    harga = input("Masukkan harga baru: ")

    barang_baru = {
        "Nama barang": nama_barang,
        "Jumlah stok": jumlah_stok,
        "Harga": harga,
    }
    data.append(barang_baru)
    simpan_data(data)
    print("Barang berhasil ditambahkan.")


def update_barang(data):
    nama_barang = input("Masukkan nama barang yang ingin diupdate: ")

    for barang in data:
        if barang["Nama barang"] == nama_barang:
            barang["Nama barang"] = input("Masukkan nama barang baru: ")
            barang["Jumlah stok"] = input("Masukkan jumlah stok baru: ")
            barang["Harga"] = input("Masukkan harga baru: ")
            simpan_data(data)
            print("Barang berhasil diupdate.")
            return

    print("Barang tidak ditemukan.")


def hapus_barang(data):
    nama_barang = input("Masukkan nama barang yang ingin dihapus: ")

    for barang in data:
        if barang["Nama barang"] == nama_barang:
            data.remove(barang)
            simpan_data(data)
            print("Barang berhasil dihapus.")
            return

    print("Barang tidak ditemukan.")


def tampilkan_barang(data):
    if len(data) == 0:
        print("Data kosong.")
        return

    for i, barang in enumerate(data, start=1):
        print("Barang", i)
        print("Nama barang:", barang["Nama barang"])
        print("Jumlah stok:", barang["Jumlah stok"])
        print("Harga:", barang["Harga"])
        print("--------------------")


def main():
    data = muat_data()

    print("Sistem Inventaris Toko Kelontong")

    while True:
        print("\nMenu:")
        print("1. Tambah barang")
        print("2. Update barang")
        print("3. Hapus barang")
        print("4. Lihat barang")
        print("5. Keluar")
        pilihan = input("Masukkan pilihan (1-5): ")

        if pilihan == "1":
            tambah_barang(data)
        elif pilihan == "2":
            update_barang(data)
        elif pilihan == "3":
            hapus_barang(data)
        elif pilihan == "4":
            tampilkan_barang(data)
        elif pilihan == "5":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
