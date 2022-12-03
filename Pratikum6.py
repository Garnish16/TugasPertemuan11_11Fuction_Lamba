# import tabulate
from tabulate import tabulate

#GARNISH ANDHIKA PRATAMA 
#TI.22.B1

dataMahasiswa = {
    'No': [],
    'Nim': [],
    'Nama': [],
    'Tugas': [],
    'Uts': [],
    'Uas': [],
    'Nilai Akhir': [],
}
no = 0
# fungsi untuk menampilkan data


def tampilan():
    print("Berikut Data Yang Ada Cari")
    print(tabulate(dataMahasiswa, headers=[
        'No', 'NIM', 'NAMA', 'TUGAS', 'UTS', 'UAS', 'Nilai Akhir'], tablefmt="fancy_grid"))

# fungsi untuk menambah data 


def tambah(no):
    # menginput data
    nim = int(input("Masukan NIM : "))
    nama = input("Masukan Nama : ")
    tugas = int(input("Masukan Nilai Tugas :"))
    uts = int(input("Masukan Nilai Uts : "))
    uas = int(input("Masukan Nilai Uas : "))
    nila_akhir = (tugas * 30 / 100) + (uts * 35 / 100) + (uas * 35 / 100)
    # menambahkan data
    dataMahasiswa['No'].append(no)
    dataMahasiswa['Nim'].append(nim)
    dataMahasiswa['Nama'].append(nama)
    dataMahasiswa['Uts'].append(uts)
    dataMahasiswa['Tugas'].append(tugas)
    dataMahasiswa['Uas'].append(uas)
    dataMahasiswa['Nilai Akhir'].append(nila_akhir)
    print('Data berhasil ditambahkan.')
    # print(tabulate(dataMahasiswa, headers=[
    #      'NIM', 'Nama', 'Tugas', 'UTS', 'UAS', 'Nilai Akhir'], tablatefmt="fancy_grid"))

# fungsi untuk  Mengedit data


def ubah(nama):
    # cek jika ada nama tersebut di dataMahasiswa
    if nama in dataMahasiswa['Nama']:
        # cari posisi indexnya lalu di simpan di namindex
        namaIndex = dataMahasiswa['Nama'].index(nama)
        print("Pilih Data yang mau diedit")
        # perulangan mengedit data dalam bentuk perulangan
        while True:
            editApa = int(input(
                "(1) Nim, \n (2) Nama, \n (3) Nilai Uts, \n (5) Nilai Uas, \n (00) Save Peribahan & exit \n : "))
            print("")

            if editApa == 1:
                # Merubah nim
                newNim = int(input("Masikan Nim ;"))
                dataMahasiswa['Nim'][namaIndex] = newNim
            elif editApa == 2:
                # Merubah nama 
                newNama = input("Masukan Nama :")
                dataMahasiswa['Nama'][namaIndex] = newNama
            elif editApa == 3:
                # Merubah nilai tugas & nilai akhir
                newTugas = int(input("Masukan Nilai Tugas :"))
                nilai_akhir = (newTugas * 30 / 100) + (dataMahasiswa['Uts'][namaIndex] * 35 / 100) + (
                    dataMahasiswa['Uas'][namaIndex] * 35 / 100)
                dataMahasiswa['Tugas'][namaIndex] = newTugas
                dataMahasiswa['Nilai Akhir'][namaIndex] = nilai_akhir
            elif editApa == 4 :
                # Merubah nilai tugas & nilai akhir
                newUts = int(input("Masukan Nilai Uts :"))
                nilai_akhir = (dataMahasiswa['Tugas'][namaIndex] * 30 / 100) + (newUts * 35 / 100) + (
                    dataMahasiswa['Uas'][namaIndex] * 35 / 100)
                dataMahasiswa['Uts'][namaIndex] = newUts
                dataMahasiswa['Nilai Akhir'][namaIndex] = nilai_akhir
            elif editApa == 5 :
                # Merubah nilai uas & nilai akhir
                newUas = int(input("Masukan Nilai Uas :"))
                nilai_akhir = (dataMahasiswa['Tugas'][namaIndex] * 30 / 100) + (dataMahasiswa['Uts'][namaIndex] * 35 / 100) + (
                    newUas * 35 / 100)
                dataMahasiswa['Uas'][namaIndex] = newUas
                dataMahasiswa['Nilai Akhir'][namaIndex] = nilai_akhir
            elif editApa == 00 :
                print('Perubahan Data Berhasil Disimpan,')
                break
    else: 
        print("data tidak ditemukan")

# fungsi untuk Menghapus data


def hapus(nama):
    if nama in dataMahasiswa['Nama']:
        namaIndex = dataMahasiswa['Nama'].index(nama)
        # menghapus data berdasarkan position index pada nama
        del dataMahasiswa['No'][namaIndex]
        del dataMahasiswa['Nim'][namaIndex]
        del dataMahasiswa['Nama'][namaIndex]
        del dataMahasiswa['Tugas'][namaIndex]
        del dataMahasiswa['Uts'][namaIndex]
        del dataMahasiswa['Uas'][namaIndex]
        del dataMahasiswa['Nilai Akhir'][namaIndex]
        print("Data Berhasil Dihapus. ")
    else:
        print("Data Tidak Ditemukan")

# fungsi untuk mencari data

# melakulan perulangan mengguanaka while sampai user menekan huruf Q perulangan akan behenti 
while True:
    # opsi input pilihan C,R,U,D,F,Q
    tanya = input (" (C) Menambah data,\n (R) Meliat semua Data,\n (U) Update data,\n (D) Menghapus Data, \n (Q) Keluar Program \n Masukan Perintah: ")
    if tanya == "C":
        while True: 
            no += 1
            # memanggil fungsi tambahanData dan memparsing data no
            tambah(no)
            tambahDatalagi = input("Tambah Data Lagi ? (y/n) :")
            if tambahDatalagi == 'n' :
                break
    elif tanya == "R":
        # menampilkan data dalam bentuh table menggunakan package tabulate
        tampilan()
        print("")
    elif tanya == "U":
        print(tabulate(dataMahasiswa, headers=[
            'NO', 'NIM', 'Nama', 'Tugas', 'UTS', 'UAS', 'Nilai_akhir'], tablefmt="fancy_grid"))
        nama = input("Masukan Nama Yang Mau Diedit : ")
        print("")
        ubah(nama)
    elif tanya == "D":
        print(tabulate(dataMahasiswa, headers=[
            'NO', 'NIM', 'Nama', 'Tugas', 'UTS', 'UAS', 'Nilai_akhir'], tablefmt="fancy_grid"))
        nama = input("Masukan Nama Yang Mau Dihapus : ")
        print("")
        hapus(nama)
    elif tanya == "Q":
        print("")
        print("Andha Telah Keluar Dari Program. ")
        break