from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Sayt işləyir!'

@app.route('/submit', methods=['POST'])
def submit():
    ad = request.form.get('ad')
    telefon = request.form.get('telefon')
    mesaj = request.form.get('mesaj')

    # Mesajları fayla yazırıq
    with open('messages.txt', 'a', encoding='utf-8') as f:
        f.write(f"Ad: {ad}\nTelefon: {telefon}\nMesaj: {mesaj}\n\n")

    return 'Təşəkkürlər! Mesajınız uğurla göndərildi.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
