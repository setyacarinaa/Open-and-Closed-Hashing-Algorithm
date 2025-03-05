# Fungsi untuk mencetak isi tabel hash
def cetak_array(arr):
    print("\nIsi Tabel Hash:")
    for i, nilai in enumerate(arr):
        if nilai == -1:
            print(f"{i} -> Kosong")
        else:
            print(f"{i} -> {nilai}")
    print()

# Fungsi untuk menghitung pangkat 2 berikutnya yang lebih besar atau sama dengan m
def pangkat_2_berikutnya(m):
    m -= 1
    m |= m >> 1
    m |= m >> 2
    m |= m >> 4
    m |= m >> 8
    m |= m >> 16
    return m + 1

# Fungsi untuk menerapkan Quadratic Probing
def hashing(tabel, ukuran_tabel, arr):
    for angka in arr:
        # Hitung nilai hash
        hash_value = angka % ukuran_tabel
        print(f"\nMenyisipkan {angka} pada indeks {hash_value}")

        # Masukkan ke dalam tabel jika tidak ada tabrakan
        if tabel[hash_value] == -1:
            tabel[hash_value] = angka
            print(f"{angka} disisipkan pada indeks {hash_value}")
        else:
            print(f"Terdeteksi collision pada indeks {hash_value}")
            m = pangkat_2_berikutnya(ukuran_tabel)
            for j in range(1, m + 1):
                posisi = (hash_value + (j + j * j) // 2) % ukuran_tabel
                if tabel[posisi] == -1:
                    tabel[posisi] = angka
                    print(f"{angka} disisipkan pada indeks {posisi} setelah Quadratic Probing")
                    break

    # Cetak hasil tabel hash
    cetak_array(tabel)

# Program Utama (Driver Code)
if __name__ == "__main__":
    # Daftar Data
    arr = [21, 10, 32, 43, 54, 65, 87, 76]
    n = len(arr)

    # Ukuran Tabel Hash
    ukuran_tabel = 11
    tabel_hash = [-1] * ukuran_tabel

    print("** Hashing dengan Quadratic Probing **")
    # Panggil fungsi hashing
    hashing(tabel_hash, ukuran_tabel, arr)