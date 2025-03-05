# Open-and-Closed-Hashing-Algorithm

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

* __Nama: Setya Carina Rianti__
* __NIM: 23343054__
* __Prodi: Informatika(NK)__
* __Kode Kelas: INF1.62.4001__
* __Seksi: 202323430156__
* __Dosen Pengampu: Randi Proska Sandra, S.Pd, M.Sc__

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

## Uraian Materi📜

 
Hashing adalah salah satu teknik penting dalam struktur data yang digunakan untuk menyimpan, mengakses, dan mengelola data secara efisien.  Hashing bekerja dengan menggunakan fungsi hash yang mengubah key (kunci) menjadi indeks tertentu di dalam tabel hash. Indeks ini digunakan sebagai alamat penyimpanan data dalam tabel. Teknik ini memungkinkan proses pencarian, penyisipan, dan penghapusan data dilakukan dalam waktu yang relatif singkat, terutama dibandingkan dengan metode pencarian berurutan atau pencarian biner. Hashing banyak digunakan dalam aplikasi seperti sistem basis data, kamus digital, dan cache memori karena kecepatan aksesnya yang tinggi. Meskipun hashing menawarkan efisiensi tinggi, metode ini memiliki tantangan yang dikenal sebagai collision. Collision terjadi ketika dua atau lebih kunci yang berbeda menghasilkan indeks hash yang sama. Hal ini membuat dua data bersaing untuk disimpan di lokasi yang sama dalam tabel hash. Collision harus ditangani dengan baik agar tidak menurunkan performa pencarian dan penyimpanan data. Oleh karena itu, terdapat beberapa teknik penanganan collision yang digunakan dalam implementasi tabel hash.

Efisiensi kedua metode ini bergantung pada load factor tabel hash, yaitu rasio antara jumlah elemen yang disimpan dengan kapasitas tabel hash. Open Hashing lebih cocok digunakan jika jumlah data yang disimpan tidak diketahui sebelumnya atau jika ada kemungkinan banyak collision. Sementara itu, Closed Hashing lebih efisien untuk tabel hash dengan jumlah data terbatas dan load factor yang kecil. Namun, performa Closed Hashing akan menurun jika tabel mendekati kapasitas penuh karena semakin sulit menemukan slot kosong. Dalam memilih metode hashing, faktor-faktor seperti efisiensi ruang, kecepatan pencarian, dan kemudahan implementasi harus diperhitungkan. Open Hashing menawarkan fleksibilitas lebih besar tetapi membutuhkan memori tambahan, sedangkan Closed Hashing lebih hemat memori tetapi kinerjanya bisa menurun saat tabel penuh. Pemahaman tentang kedua metode ini sangat penting dalam pengembangan aplikasi yang memerlukan penyimpanan data dengan akses cepat dan efisien.


</details>
<details><summary><h3>1. Open Hashing</h3></summary>
Metode ini menggunakan struktur data tambahan berupa linked list di setiap slot tabel hash. Jika terjadi collision, elemen baru akan ditambahkan ke dalam linked list pada slot tersebut. Proses pencarian pada Open Hashing dilakukan dengan menelusuri linked list hingga data ditemukan atau akhir list tercapai. Keunggulan metode ini adalah kemampuannya menangani jumlah data yang tidak terbatas, selama memori masih tersedia. Namun, metode ini membutuhkan memori tambahan untuk menyimpan pointer ke linked list dan bisa menjadi lambat jika banyak elemen dalam satu slot.

</details>
<details><summary><h3>2. Closed Hashing</h3></summary>
Closed Hashing atau Open Addressing menyimpan semua elemen langsung di dalam tabel hash tanpa menggunakan linked list. Jika terjadi collision, tabel hash akan mencari slot kosong lainnya menggunakan metode tertentu. Salah satu metode yang umum digunakan adalah Linear Probing, yang mencari slot kosong berikutnya secara berurutan. Ada juga metode Quadratic Probing, yang mencari slot kosong dengan loncatan kuadrat, serta Double Hashing, yang menggunakan dua fungsi hash untuk menentukan lokasi slot baru. Closed Hashing lebih hemat memori karena tidak membutuhkan struktur tambahan, tetapi rentan terhadap clustering, yaitu penumpukan data pada slot yang berdekatan.
