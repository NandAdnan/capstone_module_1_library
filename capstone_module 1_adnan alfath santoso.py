from datetime import datetime

user = {
    "admin123": {"password": "adminadmin", "role": "admin"},
}

buku = [
    {'kode': 'N1', 'judul': 'Bumi', 'penulis': 'Tere Liye', 'penerbit': 'Gramedia', 'tahun': 2014, 'stok': 10, 'jenis': 'Novel'},
    {'kode': 'N2', 'judul': 'Bulan', 'penulis': 'Nanda Santos', 'penerbit': 'Erlangga', 'tahun': 2015, 'stok': 10, 'jenis': 'Novel'},
    {'kode': 'K1', 'judul': 'Matahari', 'penulis': 'Alfa', 'penerbit': 'GreenBook', 'tahun': 2016, 'stok': 10, 'jenis': 'Komik'}
]
buku_dipinjam = {}

def buat_akun():
    print("\n=== Buat Akun ===")
    username = input("Masukkan nama pengguna: ").strip()

    if username == "":
        print("Nama pengguna tidak boleh kosong. Silakan coba lagi.")
        return
    
    if username in user:
        print("Nama pengguna sudah ada. Silakan coba lagi.")
        return
    
    password = input("Masukkan kata sandi: ").strip()

    if password == "":
        print("Kata sandi tidak boleh kosong. Silakan coba lagi.")
        return

    user[username] = {'password': password, 'role': 'user'}

    print("\nAkun berhasil dibuat!")

def login():
    print("\n=== Masuk ===")

    username = input("Masukkan nama pengguna: ").strip()
    password = input("Masukkan kata sandi: ").strip()
    
    if username in user and user[username]['password'] == password:
        print("\nMasuk berhasil!")
        return username
    
    else:
        print("\nNama pengguna atau kata sandi salah. Silakan coba lagi.")
        return None

def tambah_buku():
    while (True):
        print("\n=== Tambah Buku ===")
        jenis_buku = input("Masukkan jenis buku (Novel/Komik): ").strip().lower()

        if jenis_buku not in ['novel', 'komik']:
            print("Jenis buku tidak valid. Silakan coba lagi.")
            continue
        
        judul = input("Masukkan judul buku: ").strip()

        if judul == "":
            print("Judul buku tidak boleh kosong. Silakan coba lagi.")
            continue

        penulis = input("Masukkan nama penulis: ").strip()

        if penulis == "":
            print("Nama penulis tidak boleh kosong. Silakan coba lagi.")
            continue

        penerbit = input("Masukkan nama penerbit: ").strip()

        if penerbit == "":
            print("Nama penerbit tidak boleh kosong. Silakan coba lagi.")
            continue

        try:
            tahun = int(input("Masukkan tahun terbit: ").strip())

        except ValueError:
            print("Tahun terbit harus berupa angka. Silakan coba lagi.")
            continue
        
        try:
            stok = int(input("Masukkan jumlah stok: ").strip())

        except ValueError:
            print("Jumlah stok harus berupa angka. Silakan coba lagi.")
            continue
        
        kode_buku = f"{'N' if jenis_buku == 'novel' else 'K'}{len(buku) + 1}"
        buku.append({'kode': kode_buku, 'judul': judul, 'penulis': penulis, 'penerbit': penerbit, 'tahun': tahun, 'stok': stok, 'jenis': jenis_buku.capitalize()})

        print("\nBuku berhasil ditambahkan!")
        
        kembali = input("\nKetik 'b' untuk kembali ke menu utama: ").strip().lower()

        if kembali == 'b':
            break

def hapus_buku():
    while (True):
        print("\n=== Hapus Buku ===")
        daftar_buku()

        try:
            indeks = int(input("Masukkan indeks buku yang ingin dihapus: ").strip()) - 1
            
        except ValueError:
            print("Indeks harus berupa angka. Silakan coba lagi.")
            continue

        if 0 <= indeks < len(buku):
            buku.pop(indeks)
            print("Buku berhasil dihapus!")

        else:
            print("Indeks buku tidak valid.")
        
        kembali = input("\nKetik 'b' untuk kembali ke menu utama: ").strip().lower()
        if kembali == 'b':
            break

def perbarui_buku():
    while (True):
        print("\n=== Perbarui Buku ===")
        daftar_buku()

        try:
            indeks = int(input("Masukkan indeks buku yang ingin diperbarui: ").strip()) - 1
        except ValueError:
            print("Indeks harus berupa angka. Silakan coba lagi.")
            continue

        if 0 <= indeks < len(buku):
            judul = input("Masukkan judul buku baru: ").strip()

            if judul == "":
                print("Judul buku tidak boleh kosong. Silakan coba lagi.")
                continue
            
            penulis = input("Masukkan nama penulis baru: ").strip()

            if penulis == "":
                print("Nama penulis tidak boleh kosong. Silakan coba lagi.")
                continue

            penerbit = input("Masukkan nama penerbit baru: ").strip()

            if penerbit == "":
                print("Nama penerbit tidak boleh kosong. Silakan coba lagi.")
                continue

            try:
                tahun = int(input("Masukkan tahun terbit baru: ").strip())
            except ValueError:
                print("Tahun terbit harus berupa angka. Silakan coba lagi.")
                continue

            try:
                stok = int(input("Masukkan jumlah stok baru: ").strip())
            except ValueError:
                print("Jumlah stok harus berupa angka. Silakan coba lagi.")
                continue

            buku[indeks] = {'kode': buku[indeks]['kode'], 'judul': judul, 'penulis': penulis, 'penerbit': penerbit, 'tahun': tahun, 'stok': stok, 'jenis': buku[indeks]['jenis']}
            print("Buku berhasil diperbarui!")

        else:
            print("Indeks buku tidak valid.")
        
        kembali = input("\nKetik 'b' untuk kembali ke menu utama: ").strip().lower()
        if kembali == 'b':
            break

def daftar_buku():
    print("\n=== Daftar Buku ===")
    if not buku:
        print("Tidak ada buku yang tersedia.")
        return
    
    print(f"{'Indeks':<6}{'Kode':<6}{'Judul':<20}{'Penulis':<20}{'Penerbit':<20}{'Tahun':<6}{'Stok':<6}{'Jenis':<10}")

    for idx, item_buku in enumerate(buku, start=1):

        jenis_buku = item_buku.get('jenis', 'Tidak Diketahui')

        print(f"{idx:<6}{item_buku['kode']:<6}{item_buku['judul']:<20}{item_buku['penulis']:<20}{item_buku['penerbit']:<20}{item_buku['tahun']:<6}{item_buku['stok']:<6}{jenis_buku:<10}")

    print()

def pinjam_buku(username):
    while (True):
        print("\n=== Pinjam Buku ===")
        daftar_buku()

        try:
            indeks = int(input("Masukkan indeks buku yang ingin dipinjam: ").strip()) - 1
        except ValueError:
            print("Indeks harus berupa angka. Silakan coba lagi.")
            continue

        try:
            jumlah = int(input("Masukkan jumlah buku yang ingin dipinjam: ").strip())
        except ValueError:
            print("Jumlah harus berupa angka. Silakan coba lagi.")
            continue
        
        tanggal_pinjam = input("Masukkan tanggal pinjam (DD-MM-YYYY): ").strip()

        try:
            datetime.strptime(tanggal_pinjam, "%d-%m-%Y")
        except ValueError:
            print("Format tanggal tidak valid. Silakan coba lagi.")
            continue

        if 0 <= indeks < len(buku) and buku[indeks]['stok'] >= jumlah:
            buku[indeks]['stok'] -= jumlah
            if username not in buku_dipinjam:
                buku_dipinjam[username] = []
            buku_dipinjam[username].append({
                'judul': buku[indeks]['judul'],
                'jumlah': jumlah,
                'tanggal_pinjam': tanggal_pinjam
            })
            print("Buku berhasil dipinjam!")

        else:
            print("Indeks buku tidak valid atau stok tidak mencukupi.")
        
        kembali = input("\nKetik 'b' untuk kembali ke menu utama: ").strip().lower()
        if kembali == 'b':
            break

def status_pinjaman(username):
    while (True):
        print("\n=== Status Pinjaman ===")

        if username not in buku_dipinjam or not buku_dipinjam[username]:
            print("Tidak ada buku yang dipinjam.")

        else:
            print(f"{'Judul':<20}{'Jumlah':<10}{'Tanggal Pinjam':<15}")
            for record in buku_dipinjam[username]:
                print(f"{record['judul']:<20}{record['jumlah']:<10}{record['tanggal_pinjam']:<15}")
        
        kembali = input("\nKetik 'b' untuk kembali ke menu utama: ").strip().lower()
        if kembali == 'b':
            break

def kembalikan_buku(username):
    while (True):
        print("\n=== Kembalikan Buku ===")
        if username not in buku_dipinjam or not buku_dipinjam[username]:
            print("Tidak ada buku yang dipinjam.")
            break

        else:
            print(f"{'Indeks':<6}{'Judul':<20}{'Jumlah':<10}{'Tanggal Pinjam':<15}")
            for idx, record in enumerate(buku_dipinjam[username], start=1):
                print(f"{idx:<6}{record['judul']:<20}{record['jumlah']:<10}{record['tanggal_pinjam']:<15}")
            
            try:
                indeks = int(input("Masukkan indeks buku yang ingin dikembalikan: ").strip()) - 1
            except ValueError:
                print("Indeks harus berupa angka. Silakan coba lagi.")
                continue

            if 0 <= indeks < len(buku_dipinjam[username]):
                record = buku_dipinjam[username].pop(indeks)
                for item_buku in buku:
                    if item_buku['judul'] == record['judul']:
                        item_buku['stok'] += record['jumlah']
                        break

                tanggal_pinjam = datetime.strptime(record['tanggal_pinjam'], "%d-%m-%Y")
                tanggal_kembali = input("Masukkan tanggal kembali (DD-MM-YYYY): ").strip()

                try:
                    tanggal_kembali = datetime.strptime(tanggal_kembali, "%d-%m-%Y")
                except ValueError:
                    print("Format tanggal tidak valid. Silakan coba lagi.")
                    continue

                hari_dipinjam = (tanggal_kembali - tanggal_pinjam).days

                if hari_dipinjam <= 3:
                    biaya = 2000
                elif hari_dipinjam <= 7:
                    biaya = 7000
                else:
                    biaya = 20000
                total_biaya = biaya * record['jumlah']
                
                print(f"Detail Peminjaman:")
                print(f"Judul Buku: {record['judul']}")
                print(f"Jenis Buku: {item_buku['jenis']}")
                print(f"Dipinjam pada tanggal: {record['tanggal_pinjam']}")
                print(f"\nTotal = {hari_dipinjam} hari peminjaman = {biaya} x {record['jumlah']} = {total_biaya}")
                
                while (True):
                    try:
                        uang_dibayar = int(input("Masukkan jumlah uang untuk membayar: ").strip())
                    except ValueError:
                        print("Jumlah uang harus berupa angka. Silakan coba lagi.")
                        continue

                    if uang_dibayar < total_biaya:
                        kurang = total_biaya - uang_dibayar
                        print(f"Uang anda kurang {kurang}. Silakan masukkan jumlah yang benar.")
                    else:
                        kembalian = uang_dibayar - total_biaya
                        print(f"Pembayaran berhasil! Kembalian Anda: {kembalian}")
                        break
            else:
                print("Indeks buku tidak valid.")
        
        kembali = input("\nKetik 'b' untuk kembali ke menu utama: ").strip().lower()
        if kembali == 'b':
            break

while (True):
    print("\n=== Selamat Datang Di Perpustakaan ABC ===")
    print("1. Buat Akun")
    print("2. Masuk")
    print("3. Keluar")
    
    pilihan = input("Masukkan pilihan Anda: ").strip()
    
    if pilihan == '1':
        buat_akun()

    elif pilihan == '2':
        pengguna_masuk = login()
        if pengguna_masuk:
            while (True):
                print("\n=== Menu Utama ===")
                print("1. Tambah Buku (admin only)")
                print("2. Hapus Buku (admin only)")
                print("3. Perbarui Buku (admin only)")
                print("4. Daftar Buku")
                print("5. Pinjam Buku")
                print("6. Status Pinjaman")
                print("7. Kembalikan Buku")
                print("8. Keluar")
                
                pilihan = input("Masukkan pilihan Anda: ").strip()
                role = user[pengguna_masuk]['role']
                
                if pilihan == '1' and role == 'admin':
                    tambah_buku()

                elif pilihan == '2' and role == 'admin':
                    hapus_buku()

                elif pilihan == '3' and role == 'admin':
                    perbarui_buku()
                    
                elif pilihan == '4':
                    daftar_buku()
                    input("\nMasukkan 'b' untuk kembali ke menu utama: ").strip().lower()
                    
                elif pilihan == '5':
                    pinjam_buku(pengguna_masuk)

                elif pilihan == '6':
                    status_pinjaman(pengguna_masuk)

                elif pilihan == '7':
                    kembalikan_buku(pengguna_masuk)

                elif pilihan == '8':
                    print("Anda sudah keluar. Terima Kasih!")
                    break
                
                else:
                    print("Pilihan tidak valid atau akses ditolak.")
                    
    elif pilihan == '3':
        print("\nAnda berhasil keluar dari program. Terima Kasih!")
        break
    
    else:
        print("\nPilihan tidak valid. Silakan coba lagi.")



