# Perbandingan-ECB-CBC-dan-CTR-Mode-
> pryek pembuatan kriptografi dalam perbandingan ECB, CBC, CTR Moda Dalam dunia kriptografi modern, algoritma AES (Advanced Encryption Standard) menjadi standar utama untuk pengamanan data. Namun, efektivitas algoritma ini sangat bergantung pada mode operasi yang digunakan untuk memproses blok-blok data. Di antara mode-mode yang tersedia, tiga yang paling umum digunakan adalah:

- ECB (Electronic Codebook): mode dasar yang mengenkripsi setiap blok secara independen.
- CBC (Cipher Block Chaining): mode yang mengaitkan setiap blok dengan blok sebelumnya menggunakan XOR.
- CTR (Counter): menggunakan counter yang berubah-ubah untuk mengenkripsi blok, memungkinkan enkripsi paralel.

## 🎯 Tujuan Penelitian
Tujuan utama proyek ini adalah untuk:

- Menganalisis perbedaan antara mode ECB, CBC, dan CTR dalam konteks keamanan dan efisiensi.
- Mengimplementasikan masing-masing mode dalam Python menggunakan pustaka PyCryptodome.
- Mengembangkan aplikasi web sederhana dengan Flask yang memungkinkan pengguna memilih mode enkripsi dan melihat hasilnya secara real-time.
- Mengukur dan membandingkan waktu eksekusi serta keamanan hasil ciphertext terhadap pola plaintext.

## 🛠️ Metodologi

- Implementasi Backend: dilakukan menggunakan Python 3 dan PyCryptodome. Tiga fungsi enkripsi dan dekripsi dibuat di utils.py untuk masing-masing mode.
- Frontend: antarmuka web dikembangkan dengan Flask dan HTML untuk menerima input teks dan menampilkan ciphertext, hasil dekripsi, serta waktu eksekusi.
- Uji Coba: dilakukan dengan plaintext yang mengandung pola berulang (“Muhammad Fadli Rahmansyah Salah Nasser Hasan Meqdam”) untuk melihat apakah mode bisa menyamarkan pola tersebut.

## 🧪 Hasil dan Analisis
Hasil yang diperoleh adalah sebagai berikut:

Mode	Pola Ciphertext	Waktu Eksekusi (detik)	Hasil Dekripsi
ECB	❌ Terlihat pola	0.002057	✅ Akurat
CBC	✅ Acak	0.000281	✅ Akurat
CTR	✅ Acak	0.000352	✅ Akurat

## Analisis:
ECB menghasilkan ciphertext yang masih mengandung pola dari plaintext karena setiap blok dienkripsi dengan cara yang sama.
CBC dan CTR menyamarkan pola dengan baik, sehingga lebih aman untuk digunakan pada data sensitif.
Waktu eksekusi menunjukkan bahwa CBC adalah yang tercepat, disusul CTR, dan terakhir ECB.
Semua mode berhasil melakukan dekripsi dengan akurat, membuktikan bahwa fungsionalitas dasar mereka berjalan baik.
