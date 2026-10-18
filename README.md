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
python3 build.py https://bayuananda.github.io/cipi-water-world/
git add -A && git commit -m "Update soal" && git push
```

GitHub Pages memperbarui situs sekitar 1 menit setelah push.
