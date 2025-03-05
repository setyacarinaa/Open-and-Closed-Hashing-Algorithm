# Konstanta untuk jumlah bucket
BUCKET_SIZE = 7


class Hash:
    def __init__(self, bucket):
        self.__bucket = bucket  # Jumlah bucket
        self.__table = [[] for _ in range(bucket)]  # Inisialisasi tabel hash kosong

    # Fungsi Hash untuk memetakan kunci ke indeks tabel
    def fungsiHash(self, kunci):
        return kunci % self.__bucket

    # Fungsi untuk menyisipkan elemen ke tabel hash
    def masukkanItem(self, kunci):
        indeks = self.fungsiHash(kunci)
        self.__table[indeks].append(kunci)
        print(f"Kunci {kunci} disisipkan pada indeks {indeks}")

    # Fungsi untuk menghapus elemen dari tabel hash
    def hapusItem(self, kunci):
        indeks = self.fungsiHash(kunci)

        if kunci in self.__table[indeks]:
            self.__table[indeks].remove(kunci)
            print(f"Kunci {kunci} berhasil dihapus dari indeks {indeks}")
        else:
            print(f"Kunci {kunci} tidak ditemukan")

    # Fungsi untuk menampilkan isi tabel hash
    def tampilkanHash(self):
        print("\nIsi Tabel Hash:")
        for i in range(self.__bucket):
            print(f"[{i}] -> ", end="")
            if self.__table[i]:
                print(" --> ".join(map(str, self.__table[i])))
            else:
                print("Kosong")
        print()


# Program Utama
if __name__ == "__main__":
    # Data yang akan dimasukkan ke dalam tabel hash
    daftar_kunci = [15, 11, 27, 8, 12]

    # Membuat tabel hash dengan ukuran bucket
    tabelHash = Hash(BUCKET_SIZE)

    print("\n** Penyisipan Elemen **")
    for kunci in daftar_kunci:
        tabelHash.masukkanItem(kunci)

    # Menampilkan isi tabel hash setelah penyisipan
    tabelHash.tampilkanHash()

    # Menghapus elemen
    print("\n** Penghapusan Elemen **")
    tabelHash.hapusItem(12)
    tabelHash.tampilkanHash()

    # Mencoba menghapus elemen yang tidak ada
    print("\n** Penghapusan Elemen yang Tidak Ada **")
    tabelHash.hapusItem(99)