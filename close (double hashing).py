from typing import List
import math 

MAX_SIZE = 10000001

class DoubleHash: 
	def __init__(self, n: int): 
		self.UKURAN_TABEL = n 
		self.PRIMA = self.__bilangan_prima_terbesar(n - 1) 
		self.jumlahKunci = 0
		self.tabelHash = [-1] * n 

	def __bilangan_prima_terbesar(self, batas: int) -> int: 
		bilangan_prima = [True] * (batas + 1) 
		bilangan_prima[0], bilangan_prima[1] = False, False
		for i in range(2, int(math.sqrt(batas)) + 1): 
			if bilangan_prima[i]: 
				for j in range(i * i, batas + 1, i): 
					bilangan_prima[j] = False
		for i in range(batas, -1, -1): 
			if bilangan_prima[i]: 
				return i 

	def __hash1(self, nilai: int) -> int: 
		return nilai % self.UKURAN_TABEL 

	def __hash2(self, nilai: int) -> int: 
		return self.PRIMA - (nilai % self.PRIMA) 

	def is_full(self) -> bool: 
		return self.UKURAN_TABEL == self.jumlahKunci 

	def masukkan(self, nilai: int) -> None: 
		if nilai == -1 or nilai == -2: 
			print(f"ERROR: Nilai {nilai} tidak dapat dimasukkan ke tabel\n") 
			return
		if self.is_full(): 
			print("ERROR: Tabel Hash Penuh\n") 
			return

		probe, offset = self.__hash1(nilai), self.__hash2(nilai) 
		print(f"Menyisipkan {nilai} pada indeks {probe}")

		while self.tabelHash[probe] != -1: 
			if self.tabelHash[probe] == -2: 
				break
			print(f"Collision pada indeks {probe}, mencari slot kosong...")
			probe = (probe + offset) % self.UKURAN_TABEL 
		self.tabelHash[probe] = nilai 
		self.jumlahKunci += 1
		print(f"{nilai} disisipkan pada indeks {probe}\n")

	def hapus(self, nilai: int) -> None: 
		if not self.cari(nilai): 
			print(f"{nilai} tidak ditemukan, tidak dapat dihapus\n")
			return

		probe, offset = self.__hash1(nilai), self.__hash2(nilai) 
		while self.tabelHash[probe] != -1: 
			if self.tabelHash[probe] == nilai: 
				self.tabelHash[probe] = -2
				self.jumlahKunci -= 1
				print(f"{nilai} dihapus dari indeks {probe}\n")
				return
			else: 
				probe = (probe + offset) % self.UKURAN_TABEL 

	def cari(self, nilai: int) -> bool: 
		probe, offset, posisiAwal, iterasiPertama = self.__hash1(nilai), self.__hash2(nilai), self.__hash1(nilai), True
		while True: 
			if self.tabelHash[probe] == -1: 
				break
			elif self.tabelHash[probe] == nilai: 
				return True
			elif probe == posisiAwal and not iterasiPertama: 
				return False
			else: 
				probe = (probe + offset) % self.UKURAN_TABEL 
			iterasiPertama = False
		return False

	def cetak(self) -> None: 
		print("Isi Tabel Hash:")
		for i in range(self.UKURAN_TABEL):
			if self.tabelHash[i] == -1:
				print(f"{i} -> Kosong")
			elif self.tabelHash[i] == -2:
				print(f"{i} -> Dihapus")
			else:
				print(f"{i} -> {self.tabelHash[i]}")
		print("\n")


if __name__ == '__main__': 
	tabelSaya = DoubleHash(13) 

	# Penyisipan Elemen
	dataMasuk = [115, 12, 87, 66, 123] 
	print("\n-- Penyisipan Elemen --")
	for elemen in dataMasuk: 
		tabelSaya.masukkan(elemen) 
	tabelSaya.cetak() 

	# Pencarian Elemen
	kueri = [1, 12, 2, 3, 69, 88, 115] 
	print("\n-- Operasi Pencarian --") 
	for nilai in kueri: 
		if tabelSaya.cari(nilai): 
			print(f"{nilai} ditemukan") 
		else: 
			print(f"{nilai} tidak ditemukan") 

	# Penghapusan Elemen
	dataHapus = [123, 87, 66] 
	print("\n-- Penghapusan Elemen --")
	for nilai in dataHapus: 
		tabelSaya.hapus(nilai) 
	tabelSaya.cetak()