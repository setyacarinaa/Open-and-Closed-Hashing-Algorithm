# Open-and-Closed-Hashing-Algorithm

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

* __Nama: Setya Carina Rianti__
* __NIM: 23343054__
* __Prodi: Informatika(NK)__
* __Kode Kelas: INF1.62.4001__
* __Seksi: 202323430156__
* __Dosen Pengampu: Randi Proska Sandra, M.Sc__

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

## Uraian Materi📜

</details>
<details><summary><h3>1. Open Hashing</h3></summary>
Metode ini menggunakan struktur data tambahan berupa linked list di setiap slot tabel hash. Jika terjadi collision, elemen baru akan ditambahkan ke dalam linked list pada slot tersebut. Proses pencarian pada Open Hashing dilakukan dengan menelusuri linked list hingga data ditemukan atau akhir list tercapai. Keunggulan metode ini adalah kemampuannya menangani jumlah data yang tidak terbatas, selama memori masih tersedia. Namun, metode ini membutuhkan memori tambahan untuk menyimpan pointer ke linked list dan bisa menjadi lambat jika banyak elemen dalam satu slot.

</details>
<details><summary><h3>2. Closed Hashing</h3></summary>
Closed Hashing atau Open Addressing menyimpan semua elemen langsung di dalam tabel hash tanpa menggunakan linked list. Jika terjadi collision, tabel hash akan mencari slot kosong lainnya menggunakan metode tertentu. Salah satu metode yang umum digunakan adalah Linear Probing, yang mencari slot kosong berikutnya secara berurutan. Ada juga metode Quadratic Probing, yang mencari slot kosong dengan loncatan kuadrat, serta Double Hashing, yang menggunakan dua fungsi hash untuk menentukan lokasi slot baru. Closed Hashing lebih hemat memori karena tidak membutuhkan struktur tambahan, tetapi rentan terhadap clustering, yaitu penumpukan data pada slot yang berdekatan.
