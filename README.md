# Studi_Kasus_6_DDP_RaihanumAthaya_014
Nama  :  Raihanum Athaya Rana Insyra<br>
NIM   :  2609116014<br>
Kelas :  A<br>
Tema  :  Sistem Pendataan Koleksi Tenun Samarinda<br>
---
## **Penjelasan Program**<br>
Program yang telah saya buat adalah sistem inventaris sederhana untuk toko kelontong yang menyimpan datanya secara permanen di data.json. Saat dijalankan, fungsi muat_data() membaca isi file tersebut, lalu program menampilkan menu perulangan while True yang terus berjalan sampai pengguna memilih keluar. Melalui menu yang ada, pengguna dapat menambah barang, update barang, hapus barang, tampilkan. setiap perubahan akan langsung disimpan ke file melalui simpan_data yang memakai json.dump, sehingga data tidak hilang dan tetap muncul saat di run kembali.

## **Input dan Output Beserta Penjelasan**<br>

<img width="1122" height="678" alt="image" src="https://github.com/user-attachments/assets/a75e19ce-b042-45e5-9f33-1a1e1fb54875" /><br>
- import json berfungsi untuk import modul bawaan yang berfungsi untuk menulis dan membaca format json
- import os berfngsi Untuk berinteraksi dengan sistem file yang ada, dan disitu fungsinya untuk cek apakah filenya ada atau tidak.
- alurnya adalahfungsi muat_data akan dipanggil, kemudian akan dicek menggunakan os.path.exists. Namun jika file belum ada, maka return[] akan mengembalikan list kosong sebagai data awalnya.<br>
<br>
<img width="1172" height="588" alt="image" src="https://github.com/user-attachments/assets/796fd63e-349e-4583-8511-05db8a5dd227" /><br>
<br>

- FUngsi tambah barang(data) menambahkan satu barang baru. Fungsi ini meminta pengguna mengetik nama barang, jumlah stok, dan harga melalui terminal menggunakan input(). Kemudia disatukan dalam dictionary bernama barang_baru. Dictionary tersebut ditambahkan ke akhir list data dengan append(), kemudian seluruh list yang sudah diperbarui dan disimpan ke file simpan_data(data)<br>
<br>
<img width="1196" height="512" alt="image" src="https://github.com/user-attachments/assets/c718c6aa-82a1-408e-aba3-9d86f1d8fc1b" /><br>
<br>
- Fungsi update_barang(data) dipakai untuk mengubah data barang yang sudah ada. pertama, pengguna akan diminta mengetik nama barang yang ingin diu ah program lalu menelurusi isi list data satu per satu dengan perulangan for. Jika ada barang yang kolom "nama barang" nya sama persis dengan yang diketik.<br>
<br>
<img width="1150" height="454" alt="image" src="https://github.com/user-attachments/assets/966c0b79-f671-4da3-8ec7-119a700fd757" /><br>
<br>
Fungsi hapus_barang(data) memakai pola pencarian yang sama. setelah barang dengan nama cocok ditemuka, barang itu dibuang dari list menggunakan data.remove(barang), perubahan disimpan ke file dan fungsi langsung berhenti dengan return.

<img width="1044" height="460" alt="image" src="https://github.com/user-attachments/assets/fb718c3b-4efa-4201-9fb6-c35000450470" /><br>
<br>

- Fungsi tampilkan barang data mencetak seluruh barang ke layar. namun, jika list kosong(len(data) == 0), program hanya mencetak ’data kosong." lalu berhenti. Jika ada isinya enumerate(data, start=1) dipakai agar setiap barang mendapat nomor urut yang dimulai dari 1, lalu nama, jumlah stok dan harganya dicetak.<br>
<br>

<img width="1202" height="1174" alt="image" src="https://github.com/user-attachments/assets/9cf38c66-b276-4146-8cc9-bc5ec5feec7e" /><br> 
<br>
fungsi main() adalah bagian utama yang menjalankan seluruh program. Pertama, membaca data dari file data.json lalu menampilkan menu terus menerus lewat while True dan meminta pengguna memilih angka. Tiap angka memanggil fitur-fitur.<br>

### Data awal<br>
<img width="1016" height="872" alt="image" src="https://github.com/user-attachments/assets/3ead5229-e68f-4199-a265-24191353f804" /><br>

### menampilkan barang<br>

<img width="1192" height="1060" alt="image" src="https://github.com/user-attachments/assets/7845d437-0f93-446e-af6a-3d5428500bf0" />
<br>
### Menambahkan barang<br>

<img width="1050" height="1372" alt="image" src="https://github.com/user-attachments/assets/b96ce50c-de26-46f6-849f-dbcfcbcbe255" />
<br>
### Mengupdate barng<br>
<img width="1354" height="1396" alt="image" src="https://github.com/user-attachments/assets/485fd065-7795-419e-8655-c8cd8186e73e" />
<br>
### Menghapus barang<br>
<img width="1344" height="1170" alt="image" src="https://github.com/user-attachments/assets/d7f94eb6-1839-4286-b6ba-9f4d8204a332" />
<br>
### keluar<br>
<img width="902" height="308" alt="image" src="https://github.com/user-attachments/assets/5030cd41-1f30-4ff8-8c9a-399fd800ab35" />
<br>
### DAta setelah di-run kembali<br>
<img width="836" height="930" alt="image" src="https://github.com/user-attachments/assets/605279da-b728-4f67-84b5-39470afa95e7" />

















