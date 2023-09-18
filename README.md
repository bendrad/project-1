# Aplikasi Data Nilai Siswa

Aplikasi ini adalah sebuah program sederhana untuk mengelola data nilai siswa. Program ini memungkinkan Anda untuk melakukan berbagai operasi seperti menambahkan data siswa, melihat data siswa, mengupdate data siswa, menghapus data siswa, serta menampilkan status kelulusan siswa.

## Fitur

Aplikasi ini memiliki beberapa fitur utama:

1. **Lihat Data Nilai Siswa**: Anda dapat melihat data nilai siswa, baik secara keseluruhan maupun untuk siswa tertentu. Aplikasi ini juga menghitung total nilai semua siswa.

2. **Tambah Data Nilai Siswa**: Anda dapat menambahkan data siswa baru ke dalam sistem. Data yang harus dimasukkan mencakup nama siswa, nilai tugas, nilai UTS, dan nilai UAS. Setelah menambahkan data siswa, Anda dapat melihat data tersebut dalam bentuk tabel.

3. **Update Data Nilai Siswa**: Anda dapat mengupdate data siswa yang sudah ada dalam sistem. Anda bisa mengganti nama siswa, nilai tugas, nilai UTS, dan nilai UAS. Data yang diupdate juga akan tersimpan dalam file.

4. **Hapus Data Nilai Siswa**: Anda bisa menghapus data siswa baik secara individu maupun semua data siswa. Jika Anda menghapus data individu, program akan meminta ID siswa yang ingin dihapus.

5. **Status Kelulusan Siswa**: Aplikasi ini bisa menampilkan status kelulusan semua siswa, siswa yang lulus, serta siswa yang tidak lulus berdasarkan nilai rata-rata mereka.

## Cara Penggunaan

1. Jalankan program dengan menjalankan script Python `main_menu()`. Program akan memulai dengan menu utama.

2. Pilih salah satu operasi yang ingin Anda lakukan (1-6) sesuai dengan menu yang ditampilkan.

3. Ikuti petunjuk yang diberikan oleh program untuk setiap operasi. Anda akan diminta untuk memasukkan data siswa, memasukkan ID siswa, nama siswa, dan nilai-nilai tugas, UTS, dan UAS.

4. Data siswa akan disimpan dalam file `data_nilai.txt` dan bisa diakses kembali saat program dijalankan kembali.

5. Untuk melihat status kelulusan siswa, Anda dapat memilih opsi di submenu Status Kelulusan Siswa (menu 5).

6. Untuk keluar dari program, pilih opsi 6 pada menu utama.

## Kebutuhan

Aplikasi ini membutuhkan beberapa library pihak ketiga yang harus diinstal sebelum menjalankannya. Anda dapat menginstal library-library ini menggunakan pip:
pip install pyinputplus
pip install tabulate


## Catatan

- ID siswa akan digenerate secara acak dengan 6 digit setiap kali Anda menambahkan siswa baru.
- Nilai tugas, UTS, dan UAS harus berada dalam rentang 0 hingga 100.
- Status kelulusan dihitung berdasarkan perbandingan nilai tugas, UTS, dan UAS dengan bobot tertentu. Nilai akhir di atas atau sama dengan 80 dianggap "LULUS."

Selamat menggunakan aplikasi Data Nilai Siswa! Jika Anda memiliki pertanyaan atau masukan, jangan ragu untuk menghubungi kami.
Pastikan Anda telah menginstal pustaka-pustaka yang dibutuhkan (pyinputplus dan tabulate) sebelum menjalankan program ini.
