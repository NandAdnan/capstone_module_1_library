Penjelasan Program dan Fungsi-Fungsi
Program ini adalah sistem manajemen perpustakaan sederhana yang memungkinkan admin dan pengguna untuk mengelola akun, buku, dan pinjaman. Berikut adalah penjelasan singkat tentang fungsi-fungsi yang ada:

buat_akun(): Membuat akun pengguna baru dengan nama pengguna dan kata sandi. Menambahkan pengguna ke dalam user dictionary.
login(): Memungkinkan pengguna untuk masuk dengan nama pengguna dan kata sandi. Memeriksa kredensial pengguna dan mengembalikan nama pengguna jika berhasil.
tambah_buku(): Admin dapat menambahkan buku baru ke dalam perpustakaan dengan detail seperti judul, penulis, penerbit, tahun terbit, dan stok. Kode buku ditentukan berdasarkan jenis buku.
hapus_buku(): Admin dapat menghapus buku dari daftar buku berdasarkan indeks.
perbarui_buku(): Admin dapat memperbarui detail buku yang ada berdasarkan indeks.
daftar_buku(): Menampilkan daftar semua buku yang ada di perpustakaan.
pinjam_buku(username): Pengguna dapat meminjam buku dengan memasukkan indeks buku dan jumlah yang ingin dipinjam. Detail pinjaman dicatat dengan tanggal pinjam.
status_pinjaman(username): Menampilkan status pinjaman buku pengguna, termasuk judul, jumlah, dan tanggal pinjam.
kembalikan_buku(username): Pengguna dapat mengembalikan buku yang dipinjam. Menghitung biaya berdasarkan jumlah hari pinjaman dan meminta pembayaran. Memeriksa apakah pembayaran mencukupi dan mengembalikan sisa uang jika ada.
