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
