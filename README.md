# Cipi's Water World

Game interaktif siklus air untuk IPAS Kelas 5 SD. Anak-anak mengikuti Cipi si tetes air melewati 5 tahap siklus air, membuka peti hadiah, lalu mengikuti Ujian Cipi (10 soal acak dari 60 soal).

Bisa dibuka langsung di browser HP atau laptop, tanpa install dan tanpa login.

## File

| File | Isi |
|---|---|
| `app.html` | Sumber utama: tampilan, animasi, logika game, dan bank soal. Edit di sini. |
| `index.html` | Halaman siap online, dibuat dari `app.html` oleh `build.py`. Jangan diedit langsung. |
| `build.py` | Membungkus `app.html` jadi halaman web lengkap dan menambahkan preview link (WhatsApp, dll). |
| `BANK-SOAL.md` | Dokumentasi bank soal: cara pengacakan, topik, cara menambah soal, daftar lengkap soal. |
| `favicon.svg`, `icon-180.png`, `og.png` | Ikon tab, ikon layar utama HP, dan gambar preview saat link dibagikan. |

## Update situs

```bash
python3 build.py https://cipi-water-world.github.io/
git add -A && git commit -m "Update soal" && git push
```

GitHub Pages memperbarui situs sekitar 1 menit setelah push.

## Poin, lencana, dan rahasia

Tetes air menaikkan lencana: **Bronze** 0 · **Silver** 100 · **Gold** 250 · **Platinum** 450 · **Diamond** 700.

| Sumber | Poin | Batas |
|---|---|---|
| 5 tahap siklus air | +10 per tahap | 50 |
| Bonus transpirasi (ketuk pohon) | +5 | 5 |
| Peti hadiah setelah 5 tahap | +50 | 50 |
| Ujian Cipi | +5 per soal yang **pertama kali** dijawab benar | 300 (60 soal) |
| 16 rahasia tersembunyi | 15 sampai 30 per rahasia | 345 |
| **Total maksimal** | | **750** |

Diamond (700) hanya bisa dicapai kalau siswa menuntaskan siklus, menguasai hampir semua soal (mengulang ujian sampai soal yang belum dikuasai habis), dan menemukan hampir semua rahasia. Paket ujian berikutnya otomatis mengutamakan soal yang belum pernah dijawab benar.

### Daftar rahasia (untuk guru)

| Rahasia | Cara menemukan | Poin |
|---|---|---|
| Apel emas | Ketuk pohon besar 5 kali dengan cepat | 30 |
| Bintang laut | Ketuk bintang laut di dasar laut | 30 |
| Kristal tanah | Ketuk kristal ungu di lapisan tanah (kanan, dekat sumur) | 30 |
| Ikan lompat | Ketuk ikan saat sedang melompat | 25 |
| Kupu-kupu | Ketuk kupu-kupu | 25 |
| Bebek sungai | Ketuk bebek di sungai | 25 |
| Teman burung | Ketuk burung yang terbang | 20 |
| Ember sumur | Ketuk sumur 3 kali | 20 |
| Salju gunung | Ketuk puncak gunung bersalju | 20 |
| Kacamata matahari | Ketuk matahari 5 kali dengan cepat | 20 |
| Pelangi berkilau | Ketuk pelangi | 20 |
| Cipi geli | Ketuk Cipi 5 kali saat ia di laut | 20 |
| Awan di kejauhan | Ketuk awan kecil di latar belakang | 15 |
| Pohon kecil | Ketuk pohon kecil 3 kali | 15 |
| Bunga mekar | Ketuk bunga | 15 |
| Perahu tut-tut | Ketuk perahu | 15 |

## Data yang disimpan

Semua data hanya disimpan di browser perangkat itu (`localStorage`), tidak dikirim ke mana pun.

- **Refresh halaman:** nama, tetes air, lencana, progres misi, peti, rahasia, dan soal yang dikuasai tetap ada.
- **Tombol Mulai ulang:** muncul konfirmasi dulu. Kalau disetujui, semua data di atas dihapus dan permainan mulai lagi dari layar isi nama. Pengaturan suara (volume dan lagu) tetap disimpan.
