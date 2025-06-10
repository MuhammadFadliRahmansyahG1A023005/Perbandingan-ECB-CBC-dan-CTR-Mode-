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

Pengujian dilakukan untuk membandingkan performansi dari tiga mode enkripsi
pada algoritma AES (Advanced Encryption Standard), yaitu ECB (Electronic Codebook),
CBC (Cipher Block Chaining), dan CTR (Counter). Pengujian ini menggunakan input
plaintext yang sama: "Muhammad Fadli Rahmansyah Salah Nasser Hasan Meqdam",
dengan fokus utama pada akurasi dekripsi, waktu eksekusi, dan panjang ciphertext dalam
format heksadesimal. Dari hasil pengujian, seluruh mode mampu mengembalikan plaintext
ke bentuk semula setelah proses dekripsi, yang menunjukkan bahwa akurasi enkripsi-
dekripsi mencapai 100% untuk ketiganya. Ini menunjukkan implementasi algoritma
berjalan dengan benar dan stabil.

## 🔐 Analisis keamanan atau kelemahan system
da beberapa pertimbangan penting tentang aspek keamanan dan kemungkinan
kelemahan algoritma AES saat menerapkan sistem enkripsi menggunakan mode ECB,
CBC, dan CTR. Dalam hal keamanan, mode ECB (Electronic Codebook) dikenal memiliki
kelemahan terbesar karena setiap blok plaintext yang sama akan menghasilkan blok
ciphertext yang sama. Oleh karena itu, ECB tidak disarankan untuk digunakan ketika data
sensitif atau polanya mudah ditebak dienkripsi karena pola data plaintext masih dapat
dilihat pada hasil enkripsi.
25
Mode CBC (Cipher Block Chaining) berbeda dengan ECB karena setiap blok plaintext
sebelum dienkripsi akan di-XOR dengan ciphertext blok sebelumnya. Dengan demikian,
meskipun blok plaintext memiliki nilai yang sama, hasil ciphertext akan berbeda selama
inisialisasi vector (IV). Namun, kelemahan CBC adalah paralelisme: proses dekripsi dan
enkripsi dapat dilakukan secara bersamaan, tetapi enkripsi tidak, karena setiap blok
bergantung pada hasil sebelumnya. Selain itu, serangan tertentu, seperti serangan padding
oracle, masih dapat menyerang sistem jika IV tidak dikelola dengan aman.
Namun, mode Counter (Counter) adalah salah satu yang paling aman dan fleksibel dari
ketiganya. Seperti stream cipher, CTR meng-XOR plaintext dengan hasil enkripsi counter
yang berubah setiap blok. Salah satu keuntungan utamanya adalah mendukung proses
enkripsi dan dekripsi secara bersamaan, yang sangat efektif untuk informasi yang sangat
besar. Namun, kelemahan utama CTR adalah mengelola counter dan nonce, atau angka
yang digunakan sekali. Jika counter atau nonce digunakan lagi dalam dua pesan yang
berbeda, itu dapat menimbulkan ancaman keamanan sistem secara keseluruhan karena
penyerang dapat melakukan analisis XOR antar ciphertext untuk mendapatkan informasi
tentang plaintext asli.

## ⚙️ Arsitektur sistem atau logika algoritma
Arsitektur Sistem dalam proyek yang dirancang merupakan simulasi enkripsi dan
dekripsi teks menggunakan algoritma AES (Advanced Encryption Standard) dengan tiga
mode operasi berbeda, yaitu ECB, CBC, dan CTR. Sistem dibangun menggunakan bahasa
pemrograman Python dan mengandalkan pustaka kriptografi eksternal (seperti
PyCryptodome) yang diakses melalui file utils.py. Dan juga sistem ini termasuk komponen
yang ada antar interaksi komponen.

## 📌 Tampilan antarmuka
 <img src="https://github.com/MuhammadFadliRahmansyahG1A023005/Perbandingan-ECB-CBC-dan-CTR-Mode-/blob/main/Cuplikan%20layar%202025-06-01%20224011.png" width="180"/>

## 🧪 Penjelasan Kode
📄 **Kode:**
```python 
from flask import Flask, render_template, request
import time
from utils import encrypt_ecb, encrypt_cbc, encrypt_ctr  # sesuaikan dengan utils.py kamu

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    hasil = {}
    plaintext = ''
    mode = ''

    if request.method == 'POST':
        plaintext = request.form['plaintext']
        mode = request.form['mode']

        start = time.time()
        if mode == 'ECB':
            ciphertext, decrypted = encrypt_ecb(plaintext)
        elif mode == 'CBC':
            ciphertext, decrypted = encrypt_cbc(plaintext)
        elif mode == 'CTR':
            ciphertext, decrypted = encrypt_ctr(plaintext)
        else:
            ciphertext = decrypted = 'Mode tidak valid'

        end = time.time()
        hasil = {
            'ciphertext': ciphertext,
            'decrypted': decrypted,
            'time': round(end - start, 6)
        }

    return render_template('index.html', hasil=hasil, plaintext=plaintext, mode=mode)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request
import time
from utils import encrypt_ecb, encrypt_cbc, encrypt_ctr  # sesuaikan dengan utils.py kamu

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    hasil = {}
    plaintext = ''
    mode = ''

    if request.method == 'POST':
        plaintext = request.form['plaintext']
        mode = request.form['mode']

        start = time.time()
        if mode == 'ECB':
            ciphertext, decrypted = encrypt_ecb(plaintext)
        elif mode == 'CBC':
            ciphertext, decrypted = encrypt_cbc(plaintext)
        elif mode == 'CTR':
            ciphertext, decrypted = encrypt_ctr(plaintext)
        else:
            ciphertext = decrypted = 'Mode tidak valid'

        end = time.time()
        hasil = {
            'ciphertext': ciphertext,
            'decrypted': decrypted,
            'time': round(end - start, 6)
        }

    return render_template('index.html', hasil=hasil, plaintext=plaintext, mode=mode)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request
import time
from utils import encrypt_ecb, encrypt_cbc, encrypt_ctr  # sesuaikan dengan utils.py kamu

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    hasil = {}
    plaintext = ''
    mode = ''

    if request.method == 'POST':
        plaintext = request.form['plaintext']
        mode = request.form['mode']

        start = time.time()
        if mode == 'ECB':
            ciphertext, decrypted = encrypt_ecb(plaintext)
        elif mode == 'CBC':
            ciphertext, decrypted = encrypt_cbc(plaintext)
        elif mode == 'CTR':
            ciphertext, decrypted = encrypt_ctr(plaintext)
        else:
            ciphertext = decrypted = 'Mode tidak valid'

        end = time.time()
        hasil = {
            'ciphertext': ciphertext,
            'decrypted': decrypted,
            'time': round(end - start, 6)
        }

    return render_template('index.html', hasil=hasil, plaintext=plaintext, mode=mode)

if __name__ == '__main__':
    app.run(debug=True)
```

📄 **Kode:**
```python
# utils.py
import os
from Crypto.Cipher import AES
from Crypto.Util import Counter

def pad(s):
    pad_len = AES.block_size - len(s) % AES.block_size
    return s.encode() + bytes([pad_len] * pad_len)

def unpad(s):
    return s[:-s[-1]].decode()

def encrypt_ecb(text):
    key = os.urandom(16)
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(text))
    
    # cipher decrypt harus dipisah
    cipher_dec = AES.new(key, AES.MODE_ECB)
    decrypted = unpad(cipher_dec.decrypt(ciphertext))
    
    return ciphertext.hex(), decrypted

def encrypt_cbc(text):
    key = os.urandom(16)
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(text))
    
    cipher_dec = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher_dec.decrypt(ciphertext))
    
    return ciphertext.hex(), decrypted

def encrypt_ctr(text):
    key = os.urandom(16)
    iv = os.urandom(16)
    
    # Enkripsi
    ctr = Counter.new(128, initial_value=int.from_bytes(iv, byteorder='big'))
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    ciphertext = cipher.encrypt(text.encode())
    
    # Dekripsi pakai counter baru
    ctr_dec = Counter.new(128, initial_value=int.from_bytes(iv, byteorder='big'))
    cipher_dec = AES.new(key, AES.MODE_CTR, counter=ctr_dec)
    decrypted = cipher_dec.decrypt(ciphertext).decode()
    
    return ciphertext.hex(), decrypted
```

