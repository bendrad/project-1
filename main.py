import os
import random
import pyinputplus as pyip
from tabulate import tabulate

sistemoperasi = os.name
data_siswa = [] # List untuk menyimpan data siswa
next_id = 1  # Tambahkan variabel next_id dan inisialisasi dengan 1

def clear():
    if sistemoperasi == "posix":
        os.system("clear")
    elif sistemoperasi == "nt":
        os.system("cls")

def validasi_nama(nama_siswa):
    return all(char.isalpha() or char.isspace() for char in nama_siswa)

def validasi_nilai(nilai):
    return nilai.isdigit() and 0 <= int(nilai) <= 100

def tambah_nilai(file_name):
    global next_id
    id_siswa = str(random.randint(100000, 999999))  # Generate ID siswa acak dengan 6 digit
    next_id += 1
    nama_siswa = pyip.inputStr("Masukkan nama siswa: ", allowRegexes=[r'^[a-zA-Z\s]*$'])
    nama_siswa = nama_siswa.title()
    nilai_tugas = pyip.inputInt("Masukkan nilai tugas: ", min=0, max=100)
    nilai_uts = pyip.inputInt("Masukkan nilai UTS: ", min=0, max=100)
    nilai_uas = pyip.inputInt("Masukkan nilai UAS: ", min=0, max=100)

    data = f"{id_siswa}, {nama_siswa}, {nilai_tugas}, {nilai_uts}, {nilai_uas}"
    data_siswa.append([id_siswa, nama_siswa, nilai_tugas, nilai_uts, nilai_uas])

    

    print(f"ID Siswa: {id_siswa}")
    print(f"Nama Siswa: {nama_siswa}")
    print(f"Nilai Tugas: {nilai_tugas}")
    print(f"Nilai UTS: {nilai_uts}")
    print(f"Nilai UAS: {nilai_uas}")

    konfirmasi = pyip.inputChoice(["y", "n"], prompt="Apakah Anda ingin menambahkan data siswa di atas? (y/n): ")

    if konfirmasi.lower() == "y":
        print(f"Data siswa telah ditambahkan:\n{data}")
        print("\nTabel Data Siswa:")
        headers = ["ID Siswa", "Nama Siswa", "Nilai Tugas", "Nilai UTS", "Nilai UAS"]
        print(tabulate([data_siswa[-1]], headers=headers, tablefmt="fancy_grid"))
    else:
        print("Data is not added")
    with open(file_name, "a") as file:
        file.write(data + "\n")

def baca_nilai(file_name):
    try:
        with open(file_name, "r") as file:
            nilai_siswa = file.readlines()
        return nilai_siswa
    except FileNotFoundError:
        return []

def update_nilai(file_name, id_siswa, nama_siswa, nilai_tugas, nilai_uts, nilai_uas):
    existing_data = baca_nilai(file_name)
    found = False

    for nilai in existing_data:
        data = nilai.strip().split(", ")
        existing_id = data[0]
        if existing_id == id_siswa:
            found = True
            print("Data yang akan diupdate:")
            print(f"ID Siswa: {data[0]}")
            print(f"Nama Siswa: {data[1]}")
            print(f"Nilai Tugas: {data[2]}")
            print(f"Nilai UTS: {data[3]}")
            print(f"Nilai UAS: {data[4]}")

            konfirmasi = pyip.inputChoice(["y", "n"], prompt="Apakah Anda ingin mengupdate data siswa di atas? (y/n): ")

            if konfirmasi.lower() == "y":
                # Update data siswa
                data[1] = nama_siswa
                data[2] = str(nilai_tugas)
                data[3] = str(nilai_uts)
                data[4] = str(nilai_uas)

                with open(file_name, "w") as file:
                    for existing_data in existing_data:
                        file.write(existing_data)
                        file.write("\n")

                print("Data siswa telah diupdate.")
            else:
                print("Pengupdatean data dibatalkan.")
            return

    if not found:
        print("Siswa dengan ID tersebut tidak ditemukan.")


def hapus_nilai_tertentu(file_name, id_siswa):
    nilai_siswa = baca_nilai(file_name)
    
    found = False
    deleted_data = None  # Ini untuk menyimpan data yang dihapus
    
    for nilai in nilai_siswa:
        data = nilai.strip().split(", ")
        if data[0] == id_siswa:
            found = True
            deleted_data = nilai  # Menyimpan data yang akan dihapus
            break

    if found:
        print("Data yang akan dihapus:")
        deleted_data = deleted_data.strip().split(", ")
        print(f"ID Siswa: {deleted_data[0]}")
        print(f"Nama Siswa: {deleted_data[1]}")
        print(f"Nilai Tugas: {deleted_data[2]}")
        print(f"Nilai UTS: {deleted_data[3]}")
        print(f"Nilai UAS: {deleted_data[4]}")

        konfirmasi = pyip.inputChoice(["y", "n"], prompt=f"Apakah Anda yakin ingin menghapus data siswa dengan ID {id_siswa}? (y/n): ")
        if konfirmasi.lower() == "y":
            with open(file_name, "w") as file:
                for nilai in nilai_siswa:
                    data = nilai.strip().split(", ")
                    if data[0] != id_siswa:
                        file.write(nilai)
            print("Data siswa telah dihapus.")
            input("Tekan Enter untuk kembali ke sub-menu.")
        else:
            print("Penghapusan data dibatalkan.")
            input("Tekan Enter untuk kembali ke sub-menu.")
    else:
        print("Siswa dengan ID tersebut tidak ditemukan.")
        input("Tekan Enter untuk kembali ke sub-menu.")


def hapus_semua_nilai(file_name):
    konfirmasi = pyip.inputChoice(["y", "n"], prompt="Apakah Anda yakin ingin menghapus semua data siswa? (y/n): ")
    if konfirmasi.lower() == "y":
        with open(file_name, "w") as file:
            file.truncate(0)
        print("Semua data siswa telah dihapus.")
    else:
        print("Penghapusan data dibatalkan.")

def hitung_rata_nilai(nilai_tugas, nilai_uts, nilai_uas):
    return (float(nilai_tugas) + float(nilai_uts) + float(nilai_uas)) / 3

def status_kelulusan(rata_nilai, rasio_tugas=30, rasio_uts=30, rasio_uas=40):
    nilai_akhir = (float(rasio_tugas) * rata_nilai) / 100 + (float(rasio_uts) * rata_nilai) / 100 + (float(rasio_uas) * rata_nilai) / 100
    if nilai_akhir >= 80:
        return "LULUS"
    else:
        return "TIDAK LULUS"

def tampilkan_semua_nilai():
    nilai_siswa = baca_nilai("data_nilai.txt")
    header = ["ID Siswa", "Nama Siswa", "Nilai Tugas", "Nilai UTS", "Nilai UAS", "Total Nilai"]
    data = [nilai.strip().split(", ") for nilai in nilai_siswa]
    if data:
        for i in range(len(data)):
            if len(data[i]) >= 5:  # Check if there are enough elements in data
                rata_nilai = hitung_rata_nilai(data[i][2], data[i][3], data[i][4])
                total_nilai = round(rata_nilai, 2)
                data[i].append(total_nilai)
            else:
                print(f"Invalid data for student with ID {data[i][0]}")
        table = tabulate(data, headers=header, tablefmt="fancy_grid")
        print(table)
    else:
        print("Data tidak tersedia.")

def tampilkan_siswa_tertentu(id_siswa):
    nilai_siswa = baca_nilai("data_nilai.txt")
    header = ["ID Siswa", "Nama Siswa", "Nilai Tugas", "Nilai UTS", "Nilai UAS", "Total Nilai"]
    found = False
    for nilai in nilai_siswa:
        data = nilai.strip().split(", ")
        if data[0] == id_siswa:
            rata_nilai = hitung_rata_nilai(data[2], data[3], data[4])
            total_nilai = round(rata_nilai, 2)
            data.append(total_nilai)
            table = tabulate([data], headers=header, tablefmt="fancy_grid")
            print(table)
            found = True
            break
    if not found:
        print("Siswa dengan ID tersebut tidak ditemukan.")
    elif not nilai_siswa:
        print("Data tidak tersedia.")

def tampilkan_status_semua_siswa():
    nilai_siswa = baca_nilai("data_nilai.txt")
    header = ["ID Siswa", "Nama Siswa", "Status Kelulusan", "Total Nilai"]
    status_data = []
    if nilai_siswa:
        for nilai in nilai_siswa:
            data = nilai.strip().split(", ")
            if len(data) >= 5:  # Memeriksa apakah data memiliki setidaknya 5 elemen
                rata_nilai = hitung_rata_nilai(data[2], data[3], data[4])
                status = status_kelulusan(rata_nilai)
                total_nilai = round(rata_nilai, 2)
                status_data.append([data[0], data[1], status, total_nilai])
            else:
                print(f"Invalid data for student with ID {data[0]}")
    if status_data:
        table = tabulate(status_data, headers=header, tablefmt="fancy_grid")
        print(table)
    else:
        print("Data tidak tersedia.")
        
def tampilkan_siswa_lulus():
    nilai_siswa = baca_nilai("data_nilai.txt")
    header = ["ID Siswa", "Nama Siswa", "Status Kelulusan", "Total Nilai"]
    status_data = []
    if nilai_siswa:
        for nilai in nilai_siswa:
            data = nilai.strip().split(", ")
            rata_nilai = hitung_rata_nilai(data[2], data[3], data[4])
            status = status_kelulusan(rata_nilai)
            if status == "LULUS":
                total_nilai = round(rata_nilai, 2)
                status_data.append([data[0], data[1], status, total_nilai])
        if status_data:
            table = tabulate(status_data, headers=header, tablefmt="fancy_grid")
            print(table)
        else:
            print("Data tidak tersedia.")
    else:
        print("Data tidak tersedia.")

def tampilkan_siswa_tidak_lulus():
    nilai_siswa = baca_nilai("data_nilai.txt")
    header = ["ID Siswa", "Nama Siswa", "Status Kelulusan", "Total Nilai"]
    status_data = []
    if nilai_siswa:
        for nilai in nilai_siswa:
            data = nilai.strip().split(", ")
            rata_nilai = hitung_rata_nilai(data[2], data[3], data[4])
            status = status_kelulusan(rata_nilai)
            if status == "TIDAK LULUS":
                total_nilai = round(rata_nilai, 2)
                status_data.append([data[0], data[1], status, total_nilai])
        if status_data:
            table = tabulate(status_data, headers=header, tablefmt="fancy_grid")
            print(table)
        else:
            print("Data tidak tersedia.")
    else:
        print("Data tidak tersedia.")

def hitung_total_nilai():
    nilai_siswa = baca_nilai("data_nilai.txt")
    total_nilai = 0
    for nilai in nilai_siswa:
        data = nilai.strip().split(", ")
        if len(data) >= 5:  # Check if there are enough elements in data
            rata_nilai = hitung_rata_nilai(data[2], data[3], data[4])
            total_nilai += rata_nilai
        else:
            print(f"{data[0]}")
    return round(total_nilai, 2)

def main_menu():
    global next_id  # Gunakan variabel global next_id
    while True:
        clear()
        print("-" * 45)
        print("Selamat datang di aplikasi Data Nilai Siswa")
        print("-" * 45)
        print("""

Menu Utama:
1. Lihat data nilai siswa
2. Tambah data nilai siswa
3. Update data nilai siswa
4. Hapus data nilai siswa
5. Status Kelulusan Siswa
6. Keluar
""")

        pilihan = pyip.inputChoice(["1", "2", "3", "4", "5", "6"], prompt="Pilih operasi yang ingin Anda lakukan (1-6): ")

        if pilihan == "1":
            while True:
                clear()
                print("""
Sub Menu - Lihat Data Nilai Siswa:
1. Lihat semua data siswa
2. Lihat siswa tertentu
3. Kembali ke menu utama
""")
                sub_pilihan = pyip.inputChoice(["1", "2", "3"], prompt="Pilih operasi yang ingin Anda lakukan: ")

                if sub_pilihan == "1":
                    clear()
                    print("Data Nilai Siswa saat ini:")
                    tampilkan_semua_nilai()
                    total_nilai = hitung_total_nilai()
                    input("Tekan Enter untuk kembali ke sub-menu.")
                elif sub_pilihan == "2":
                    clear()
                    id_siswa = pyip.inputStr("Masukkan ID siswa yang ingin dilihat: ", blockRegexes=[r'[^0-9]'], allowRegexes=[r'^\d{6}$'])
                    print("Data Siswa:")
                    tampilkan_siswa_tertentu(id_siswa)
                    input("Tekan Enter untuk kembali ke sub-menu.")

                elif sub_pilihan == "3":
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")

        elif pilihan == "2":
            while True:
                clear()
                print("Sub Menu - Tambah Data Nilai Siswa:")
                print("1. Tambah data siswa ")
                print("2. Kembali ke menu utama")
                
                sub_pilihan = pyip.inputChoice(["1", "2"], prompt="Pilih operasi yang ingin Anda lakukan: ")

                if sub_pilihan == "1":
                    tambah_nilai("data_nilai.txt")
                    input("Tekan Enter untuk kembali ke sub-menu.")
                elif sub_pilihan == "2":
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")



        if pilihan == "3":
            while True:
                clear()
                print("Sub Menu - Update Data Nilai Siswa:")
                print("1. Update data siswa ")
                print("2. Kembali ke menu utama")
                
                sub_pilihan = pyip.inputChoice(["1", "2"], prompt="Pilih operasi yang ingin Anda lakukan: ")

                if sub_pilihan == "1":
                    clear()
                    print("Update data siswa:")
                    tampilkan_semua_nilai()
                    id_siswa = pyip.inputStr("Masukkan ID siswa yang ingin diupdate: ", blockRegexes=[r'[^0-9]'], allowRegexes=[r'^\d{6}$'])
                    nama_siswa = pyip.inputStr("Masukkan nama siswa yang baru: ")
                    nilai_tugas = pyip.inputInt("Masukkan nilai tugas yang baru: ", min=0, max=100)
                    nilai_uts = pyip.inputInt("Masukkan nilai UTS yang baru: ", min=0, max=100)
                    nilai_uas = pyip.inputInt("Masukkan nilai UAS yang baru: ", min=0, max=100)
                    
                    update_nilai("data_nilai.txt", id_siswa, nama_siswa, nilai_tugas, nilai_uts, nilai_uas)
                    konfirmasi = pyip.inputChoice(["y", "n"], prompt="Apakah Anda ingin mengupdate data siswa lagi? (y/n): ")
                    if konfirmasi.lower() != "y":
                        continue
                elif sub_pilihan == "2":
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")



        elif pilihan == "4":
            clear()
            print("Sub Menu - Hapus Data Nilai Siswa:")
            print("1. Hapus data siswa tertentu")
            print("2. Hapus semua data siswa")
            print("3. Kembali ke menu utama")

            sub_pilihan = pyip.inputChoice(["1", "2", "3"], prompt="Pilih operasi yang ingin Anda lakukan: ")

            if sub_pilihan == "1":
                clear()
                id_siswa = pyip.inputStr("Masukkan ID siswa yang ingin dihapus: ",
                                        blockRegexes=[r'[^0-9]'], allowRegexes=[r'^\d{6}$'])
                deleted_data = baca_nilai("data_nilai.txt")  # Membaca data siswa yang akan dihapus
                found = False

                for nilai in deleted_data:
                    data = nilai.strip().split(", ")
                    if data[0] == id_siswa:
                        found = True
                        print("Data yang akan dihapus:")
                        print(f"ID Siswa: {data[0]}")
                        print(f"Nama Siswa: {data[1]}")
                        print(f"Nilai Tugas: {data[2]}")
                        print(f"Nilai UTS: {data[3]}")
                        print(f"Nilai UAS: {data[4]}")

                        konfirmasi = pyip.inputChoice(["y", "n"], prompt="Apakah Anda yakin ingin menghapus data siswa ini? (y/n): ")
                        if konfirmasi.lower() == "y":
                            hapus_nilai_tertentu("data_nilai.txt", id_siswa)
                            print("Data siswa telah dihapus.")
                        else:
                            print("Penghapusan data dibatalkan.")
                        break

                if not found:
                    print("Siswa dengan ID tersebut tidak ditemukan.")

            elif sub_pilihan == "2":
                clear()
                konfirmasi = pyip.inputChoice(["y", "n"], prompt="Apakah Anda yakin ingin menghapus semua data siswa? (y/n): ")
                if konfirmasi.lower() == "y":
                    hapus_semua_nilai("data_nilai.txt")
                    print("Semua data siswa telah dihapus.")
                    input("Tekan Enter untuk kembali ke menu utama.")
                else:
                    print("Penghapusan data dibatalkan.")
                    input("Tekan Enter untuk kembali ke menu utama.")

            elif sub_pilihan == "3":
                pass

            else:
                print("Pilihan tidak valid. Silakan coba lagi.")


        elif pilihan == "5":
            while True:
                clear()
                print("""
Sub Menu - Status Kelulusan Siswa:
1. Lihat status kelulusan semua siswa
2. Lihat siswa yang lulus
3. Lihat siswa yang tidak lulus
4. Kembali ke menu utama
""")
                sub_pilihan = pyip.inputChoice(["1", "2", "3", "4"], prompt="Pilih operasi yang ingin Anda lakukan: ")

                if sub_pilihan == "1":
                    clear()
                    print("Status Kelulusan Siswa saat ini:")
                    tampilkan_status_semua_siswa()
                    input("Tekan Enter untuk kembali ke sub-menu.")
                elif sub_pilihan == "2":
                    clear()
                    print("Siswa yang Lulus:")
                    tampilkan_siswa_lulus()
                    input("Tekan Enter untuk kembali ke sub-menu.")
                elif sub_pilihan == "3":
                    clear()
                    print("Siswa yang Tidak Lulus:")
                    tampilkan_siswa_tidak_lulus()
                    input("Tekan Enter untuk kembali ke sub-menu.")
                elif sub_pilihan == "4":
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")

        elif pilihan == "6":
            print("Terima kasih telah menggunakan aplikasi Data Nilai Siswa. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main_menu()

