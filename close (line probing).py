# Struktur untuk HashNode
class HashNode:
	def __init__(self, kunci: int, nilai: int):
		self.kunci = kunci
		self.nilai = nilai

# Konstanta
kapasitas = 20  # Kapasitas tabel hash
ukuran = 0  # Jumlah elemen saat ini

# Array untuk menyimpan HashNode
array = [None] * kapasitas

# Node Dummy
dummy = HashNode(-1, -1)

# Fungsi untuk menambahkan pasangan kunci dan nilai
def masukkan(kunci: int, nilai: int):
	global ukuran
	node = HashNode(kunci, nilai)
	indeks_hash = kunci % kapasitas

	print(f"\nMenyisipkan kunci {kunci} dengan nilai {nilai} pada indeks {indeks_hash}")

	while array[indeks_hash] is not None and array[indeks_hash].kunci != kunci and array[indeks_hash].kunci != -1:
		print(f"Terdeteksi collision pada indeks {indeks_hash}, mencari slot kosong...")
		indeks_hash = (indeks_hash + 1) % kapasitas

	if array[indeks_hash] is None or array[indeks_hash].kunci == -1:
		ukuran += 1
		print(f"Kunci {kunci} disisipkan pada indeks {indeks_hash}")

	array[indeks_hash] = node

# Fungsi untuk menghapus pasangan kunci dan nilai
def hapus_kunci(kunci: int):
	global ukuran
	indeks_hash = kunci % kapasitas

	while array[indeks_hash] is not None:
		if array[indeks_hash].kunci == kunci:
			array[indeks_hash] = dummy
			ukuran -= 1
			print(f"Kunci {kunci} berhasil dihapus pada indeks {indeks_hash}")
			return 1
		indeks_hash = (indeks_hash + 1) % kapasitas

	print(f"Kunci {kunci} tidak ditemukan")
	return 0

# Fungsi untuk mencari nilai dari kunci yang diberikan
def cari(kunci: int):
	indeks_hash = kunci % kapasitas
	hitung = 0

	while array[indeks_hash] is not None:
		if hitung > kapasitas:
			break

		if array[indeks_hash].kunci == kunci:
			return array[indeks_hash].nilai

		indeks_hash = (indeks_hash + 1) % kapasitas
		hitung += 1

	return -1

# Fungsi untuk menampilkan isi tabel hash
def cetak():
	print("\nIsi Tabel Hash:")
	for i in range(kapasitas):
		if array[i] is None:
			print(f"{i} -> Kosong")
		elif array[i].kunci == -1:
			print(f"{i} -> Dihapus")
		else:
			print(f"{i} -> {array[i].kunci}:{array[i].nilai}")
	print()

# Kode Utama
if __name__ == "__main__":
	# Penyisipan Elemen
	masukkan(1, 5)
	masukkan(2, 15)
	masukkan(3, 20)
	masukkan(4, 7)

	cetak()

	# Pencarian Elemen
	print("\n-- Pencarian Elemen --")
	if cari(4) != -1:
		print("Nilai dari Kunci 4 =", cari(4))
	else:
		print("Kunci 4 tidak ditemukan")

	# Penghapusan Elemen
	print("\n-- Penghapusan Elemen --")
	if hapus_kunci(4):
		print("Node dengan Kunci 4 berhasil dihapus")
	else:
		print("Kunci tidak ditemukan")

	cetak()

	# Pencarian setelah Penghapusan
	print("\n-- Pencarian Setelah Penghapusan --")
	if cari(4) != -1:
		print("Nilai dari Kunci 4 =", cari(4))
	else:
		print("Kunci 4 tidak ditemukan")