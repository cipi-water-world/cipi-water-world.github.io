# Bank Soal Ujian Cipi

Catatan dokumentasi untuk kuis di `app.html` (Cipi's Water World, IPAS Kelas 5 SD Bab 4).

## Ringkasan

| | |
|---|---|
| Jumlah soal di bank | 60 |
| Soal per ujian | 10 |
| Jumlah topik | 9 |
| Opsi per soal | 4 (A–D) |
| Poin | +5 tetes air per jawaban benar |
| Bintang | 9–10 benar = 3 bintang, 6–8 = 2 bintang, 0–5 = 1 bintang |

## Cara soal dipilih (kenapa tiap paket terasa beda)

Setiap kali ujian dimulai, termasuk saat tombol **Paket soal baru** ditekan:

1. **1 soal dari setiap topik** (9 topik = 9 soal), jadi semua materi selalu terwakili.
2. **1 soal tambahan** diambil acak dari sisa bank.
3. Soal yang **sudah muncul di paket sebelumnya dilewati**, dan baru boleh muncul lagi setelah semua soal di topik itu habis terpakai. Dengan 60 soal, sekitar 6 paket berturut-turut hampir tidak ada yang berulang (hasil uji: 59 dari 60 soal unik dalam 6 paket).
4. **Urutan soal diacak**, dan **urutan opsi A–D juga diacak**, jadi soal yang sama pun posisi jawabannya berbeda.

Riwayat soal yang sudah muncul disimpan di browser perangkat itu (`localStorage`, kunci `cipi-seen`). Artinya:
- Di perangkat yang sama, paket berikutnya tetap berbeda walau halaman di-refresh.
- Di perangkat lain, riwayat mulai dari nol.
- Membuka di jendela private atau menghapus data situs membuat riwayat ikut hilang. Ujian tetap jalan normal, hanya pengecualian soal lama yang mulai dari awal lagi.

Kunci lain yang disimpan di browser: `cipi-gems` (jumlah tetes air), `cipi-badge` (lencana sudah diambil), `cipi-round` (nomor paket).

## Topik

| Kode | Topik | Jumlah | Fokus materi |
|---|---|---|---|
| `EVAP` | Evaporasi | 7 | Penguapan, perubahan wujud cair → gas, contoh sehari-hari |
| `KOND` | Kondensasi | 7 | Pengembunan, pembentukan awan, embun, gelas es |
| `PRES` | Presipitasi | 6 | Hujan, salju, hujan es, mengapa air jatuh dari awan |
| `TRAN` | Transpirasi | 6 | Stomata, air dari akar ke daun, evapotranspirasi |
| `LIMP` | Sungai & limpasan | 7 | Aliran tinggi → rendah, hulu, muara, DAS, banjir |
| `INFI` | Infiltrasi & air tanah | 7 | Peresapan, akuifer, sumur, biopori |
| `SIKL` | Siklus air | 7 | Urutan tahap, energi matahari, air tidak habis |
| `SUMB` | Sumber & persebaran air | 6 | Air laut asin, air tawar ±3%, es kutub |
| `JAGA` | Menjaga air | 7 | Hemat air, sumur resapan, dampak menebang hutan dan sampah |

## Cara menambah atau mengubah soal

Semua soal ada di satu blok di bagian bawah `app.html`:

```html
<script type="application/json" id="bank">
[
{"id":"EVAP-01","t":"EVAP","q":"Pertanyaan...","o":["Jawaban benar","Pengecoh 1","Pengecoh 2","Pengecoh 3"],"e":"Penjelasan singkat."},
...
]
</script>
```

| Field | Isi | Aturan |
|---|---|---|
| `id` | Kode unik | Diawali kode topik + nomor, mis. `EVAP-08`. Harus unik. |
| `t` | Kode topik | Salah satu dari 9 kode di tabel topik. |
| `q` | Teks soal | Bahasa anak kelas 5, satu kalimat tanya. |
| `o` | 4 opsi | **Opsi pertama selalu jawaban benar.** Urutannya diacak otomatis saat tampil. Keempat opsi harus berbeda. |
| `e` | Penjelasan | 1 kalimat, muncul setelah anak menjawab. |

Tips menulis soal:
- Hindari opsi "semua benar" atau "A dan B", karena urutan opsi diacak.
- Untuk soal urutan, pastikan pengecohnya bukan urutan yang juga benar kalau dibaca melingkar. Misalnya "kondensasi → presipitasi → evaporasi" juga benar secara siklus.
- Menambah topik baru berarti menambah satu baris di objek `TOPICS` di script (nama + warna). Tiap topik otomatis menyumbang 1 soal per paket, jadi jumlah topik maksimal 10 supaya tetap 10 soal per ujian.
- Setelah mengedit, jalankan `python3 build.py <link-situs>` untuk membuat ulang `index.html`, lalu buka dan mulai ujian. Kalau JSON salah ketik (misalnya kurang koma), kuis tidak akan terbuka.

## Daftar lengkap soal

Kolom **Jawaban benar** sama dengan `o[0]` di data.

### Evaporasi (`EVAP`, 7 soal)

| ID | Soal | Jawaban benar | Pengecoh |
|---|---|---|---|
| EVAP-01 | Tuan Matahari memanaskan air laut sampai berubah menjadi uap dan naik ke udara. Proses ini disebut... | **Evaporasi** | Kondensasi; Presipitasi; Infiltrasi |
| EVAP-02 | Saat evaporasi, air berubah wujud dari... | **Cair menjadi gas** | Gas menjadi cair; Padat menjadi cair; Cair menjadi padat |
| EVAP-03 | Baju yang dijemur cepat kering saat siang hari yang terik. Peristiwa ini adalah contoh... | **Penguapan** | Pengembunan; Peresapan; Pembekuan |
| EVAP-04 | Di mana evaporasi paling banyak terjadi di bumi? | **Di laut dan samudra** | Di dalam tanah; Di dalam gua; Di dalam akar pohon |
| EVAP-05 | Genangan air hujan di halaman bisa hilang saat siang hari. Mengapa? | **Airnya menguap karena panas matahari** | Airnya berubah menjadi es; Airnya berubah menjadi pasir; Airnya naik menjadi pelangi |
| EVAP-06 | Uap air hasil evaporasi bergerak ke mana? | **Naik ke udara** | Turun ke dalam tanah; Masuk ke dasar laut; Masuk ke akar tumbuhan |
| EVAP-07 | Pada keadaan mana air paling cepat menguap? | **Hari panas dan berangin** | Malam yang dingin; Hari mendung tanpa angin; Saat air disimpan di kulkas |

### Kondensasi (`KOND`, 7 soal)

| ID | Soal | Jawaban benar | Pengecoh |
|---|---|---|---|
| KOND-01 | Uap air di langit mendingin lalu berubah menjadi titik-titik air yang membentuk awan. Proses ini disebut... | **Kondensasi** | Evaporasi; Transpirasi; Infiltrasi |
| KOND-02 | Kondensasi terjadi karena uap air... | **Mendingin** | Dipanaskan; Meresap ke tanah; Diserap akar |
| KOND-03 | Saat kondensasi, air berubah wujud dari... | **Gas menjadi cair** | Cair menjadi gas; Padat menjadi gas; Cair menjadi padat |
| KOND-04 | Bagian luar gelas berisi es batu menjadi basah. Peristiwa ini mirip dengan... | **Kondensasi** | Evaporasi; Infiltrasi; Limpasan |
| KOND-05 | Awan terbentuk dari... | **Kumpulan titik-titik air yang sangat kecil** | Asap kendaraan; Kapas yang terbang; Debu dari gunung |
| KOND-06 | Embun di daun pada pagi hari terbentuk karena... | **Uap air mengembun saat udara dingin** | Daun mengeluarkan air hujan; Air sumur naik ke daun; Matahari memanaskan daun |
| KOND-07 | Mengapa awan terlihat gelap sebelum hujan? | **Titik-titik airnya semakin banyak dan rapat** | Awannya terbakar matahari; Awannya kehilangan air; Awannya berubah menjadi asap |

### Presipitasi (`PRES`, 6 soal)

| ID | Soal | Jawaban benar | Pengecoh |
|---|---|---|---|
| PRES-01 | Awan yang sudah berat menjatuhkan air ke bumi. Peristiwa ini disebut... | **Presipitasi** | Evaporasi; Kondensasi; Transpirasi |
| PRES-02 | Contoh presipitasi adalah... | **Hujan, salju, dan hujan es** | Embun, kabut, dan uap; Air sungai dan air sumur; Ombak dan arus laut |
| PRES-03 | Di daerah yang sangat dingin, presipitasi dapat turun dalam bentuk... | **Salju** | Uap air; Embun; Pelangi |
| PRES-04 | Mengapa titik-titik air di awan akhirnya jatuh ke bumi? | **Titik air bergabung menjadi besar dan berat** | Awan didorong oleh matahari; Awan ditarik oleh gunung; Titik air berubah menjadi uap |
| PRES-05 | Di Indonesia, bentuk presipitasi yang paling sering terjadi adalah... | **Hujan** | Salju; Hujan es; Embun beku |
| PRES-06 | Hujan biasanya turun dari awan yang... | **Tebal dan gelap** | Tipis dan sangat tinggi; Berasal dari asap pabrik; Menempel di permukaan tanah |

### Transpirasi (`TRAN`, 6 soal)

| ID | Soal | Jawaban benar | Pengecoh |
|---|---|---|---|
| TRAN-01 | Tumbuhan mengeluarkan uap air melalui pori-pori kecil di daun. Proses ini disebut... | **Transpirasi** | Infiltrasi; Presipitasi; Kondensasi |
| TRAN-02 | Pori-pori kecil di daun tempat keluarnya uap air bernama... | **Stomata** | Akar; Akuifer; Muara |
| TRAN-03 | Air yang dikeluarkan tumbuhan saat transpirasi berasal dari... | **Air tanah yang diserap akar** | Air laut; Awan; Embun di batang |
| TRAN-04 | Transpirasi paling banyak terjadi ketika... | **Cuaca panas dan cerah** | Malam hari yang dingin; Tumbuhan tidak berdaun; Hujan deras |
| TRAN-05 | Mengapa hutan yang lebat membantu terbentuknya awan dan hujan? | **Banyak pohon melepaskan uap air ke udara** | Pohon menghalangi matahari; Pohon menyerap awan; Pohon membuat laut menjadi asin |
| TRAN-06 | Gabungan penguapan dari permukaan air dan dari tumbuhan disebut... | **Evapotranspirasi** | Kondensasi; Infiltrasi; Presipitasi |

### Sungai & limpasan (`LIMP`, 7 soal)

| ID | Soal | Jawaban benar | Pengecoh |
|---|---|---|---|
| LIMP-01 | Air hujan yang mengalir di atas permukaan tanah menuju sungai disebut... | **Limpasan permukaan** | Infiltrasi; Kondensasi; Transpirasi |
| LIMP-02 | Ke mana air sungai selalu mengalir? | **Dari tempat tinggi ke tempat rendah** | Dari tempat rendah ke tempat tinggi; Berputar di tempat yang sama; Naik ke puncak gunung |
| LIMP-03 | Tempat bertemunya sungai dengan laut disebut... | **Muara** | Hulu; Danau; Akuifer |
| LIMP-04 | Bagian sungai tempat aliran berasal, biasanya di pegunungan, disebut... | **Hulu** | Hilir; Muara; Pantai |
| LIMP-05 | Limpasan air hujan menjadi sangat banyak ketika tanah... | **Tertutup semen dan aspal** | Banyak ditumbuhi pohon; Gembur dan berpori; Ditanami rumput |
| LIMP-06 | Wilayah yang menampung air hujan lalu mengalirkannya ke satu sungai disebut... | **Daerah Aliran Sungai (DAS)** | Akuifer; Muara; Samudra |
| LIMP-07 | Air sungai pada akhirnya akan mengalir ke... | **Laut** | Puncak gunung; Awan; Akar pohon |

### Infiltrasi & air tanah (`INFI`, 7 soal)

| ID | Soal | Jawaban benar | Pengecoh |
|---|---|---|---|
| INFI-01 | Air hujan yang meresap masuk ke dalam tanah disebut... | **Infiltrasi** | Evaporasi; Kondensasi; Presipitasi |
| INFI-02 | Lapisan di bawah tanah yang menyimpan air tanah disebut... | **Akuifer** | Stomata; Muara; Awan |
| INFI-03 | Air sumur berasal dari... | **Air tanah** | Air laut; Awan; Embun |
| INFI-04 | Permukaan seperti apa yang paling mudah meresapkan air hujan? | **Tanah gembur yang banyak pori** | Lantai keramik; Jalan aspal; Halaman yang disemen |
| INFI-05 | Apa manfaat infiltrasi bagi manusia? | **Menyimpan cadangan air tanah untuk sumur** | Membuat laut menjadi asin; Membuat sungai mengering; Membuat awan menjadi gelap |
| INFI-06 | Lubang kecil di tanah yang dibuat untuk membantu air hujan meresap disebut... | **Lubang biopori** | Saluran irigasi; Kolam ikan; Terowongan |
| INFI-07 | Air tanah yang mengalir pelan di dalam tanah akhirnya bisa sampai ke... | **Sungai atau laut** | Awan; Puncak gunung; Matahari |

### Siklus air (urutan & energi) (`SIKL`, 7 soal)

| ID | Soal | Jawaban benar | Pengecoh |
|---|---|---|---|
| SIKL-01 | Apa sumber energi utama yang membuat siklus air terus berputar? | **Matahari** | Bulan; Angin; Gunung |
| SIKL-02 | Urutan tiga tahap siklus air yang benar, dimulai dari laut, adalah... | **Evaporasi, kondensasi, presipitasi** | Evaporasi, presipitasi, kondensasi; Kondensasi, evaporasi, presipitasi; Presipitasi, kondensasi, evaporasi |
| SIKL-03 | Setelah uap air menjadi awan, tahap berikutnya adalah... | **Presipitasi** | Evaporasi; Infiltrasi; Transpirasi |
| SIKL-04 | Setelah hujan turun di darat, air dapat... | **Mengalir di sungai atau meresap ke tanah** | Naik ke awan tanpa menguap; Berubah menjadi batu; Hilang selamanya |
| SIKL-05 | Mengapa peristiwa ini disebut siklus air? | **Karena terjadi terus-menerus dan berulang** | Karena hanya terjadi sekali; Karena hanya terjadi di laut; Karena hanya terjadi saat hujan |
| SIKL-06 | Apakah jumlah air di bumi habis karena siklus air? | **Tidak, air hanya berpindah tempat dan berubah wujud** | Ya, air habis karena menguap; Ya, air hilang ke luar angkasa; Ya, air berubah menjadi tanah |
| SIKL-07 | Tahap siklus air yang paling membutuhkan panas matahari adalah... | **Evaporasi** | Kondensasi; Infiltrasi; Limpasan |

### Sumber & persebaran air (`SUMB`, 6 soal)

| ID | Soal | Jawaban benar | Pengecoh |
|---|---|---|---|
| SUMB-01 | Sebagian besar air di bumi berada di... | **Laut dan samudra** | Sungai; Danau; Sumur |
| SUMB-02 | Air laut tidak bisa langsung kita minum karena... | **Rasanya asin karena mengandung garam** | Warnanya biru; Terlalu dingin; Terlalu banyak ombak |
| SUMB-03 | Air hujan berasal dari laut, tetapi rasanya tidak asin. Mengapa? | **Garam tertinggal di laut saat air menguap** | Garam larut di awan; Garam dimakan ikan; Garam terbakar matahari |
| SUMB-04 | Contoh sumber air tawar di darat adalah... | **Sungai, danau, dan air tanah** | Laut dan samudra; Pelangi dan awan; Ombak dan pasir |
| SUMB-05 | Berapa kira-kira bagian air di bumi yang merupakan air tawar? | **Sangat sedikit, sekitar 3 persen** | Sekitar setengahnya; Hampir semuanya; Sekitar tiga perempat |
| SUMB-06 | Es di kutub dan di puncak gunung yang sangat tinggi menyimpan... | **Air tawar dalam bentuk padat** | Air laut yang asin; Uap air panas; Minyak bumi |

### Menjaga air (`JAGA`, 7 soal)

| ID | Soal | Jawaban benar | Pengecoh |
|---|---|---|---|
| JAGA-01 | Perbuatan mana yang membantu air hujan meresap ke dalam tanah? | **Menanam pohon dan membuat lubang biopori** | Menebang pohon di hutan; Menutup halaman dengan semen; Membuang sampah ke sungai |
| JAGA-02 | Salah satu cara menghemat air di rumah adalah... | **Menutup keran saat menggosok gigi** | Membiarkan keran tetap terbuka; Mencuci motor setiap jam; Mandi berjam-jam |
| JAGA-03 | Menebang hutan secara sembarangan dapat menyebabkan... | **Banjir dan tanah longsor** | Air tanah bertambah; Udara semakin sejuk; Sungai semakin jernih |
| JAGA-04 | Membuang sampah ke sungai dapat menyebabkan... | **Sungai tersumbat dan banjir** | Air sungai semakin bersih; Ikan semakin banyak; Air sungai mengalir ke gunung |
| JAGA-05 | Sumur resapan berguna untuk... | **Menampung air hujan agar meresap ke tanah** | Membuang sampah rumah tangga; Membuat air laut menjadi tawar; Mengeringkan sawah |
| JAGA-06 | Mengapa air tanah di kota besar bisa berkurang? | **Air tanah banyak diambil dan tanahnya tertutup bangunan** | Terlalu banyak pohon; Terlalu sering hujan; Terlalu banyak sungai |
| JAGA-07 | Kekeringan dapat terjadi ketika... | **Lama tidak turun hujan dan air tanah berkurang** | Hujan turun setiap hari; Sungai meluap; Banyak pohon ditanam |
