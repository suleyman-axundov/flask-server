from flask import Flask, request
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)
CORS(app)

# Gmail hesab məlumatları
GMAIL_USER = 'suleyman.axundov2004@gmail.com'  # <-- Buraya öz gmail ünvanını yaz
GMAIL_PASSWORD = 'ldvdfdkbubkffzty'   # <-- App Password-u boşluqsuz yazdım

@app.route('/')
def home():
    return 'Sayt işləyir!'

@app.route('/submit', methods=['POST'])
def submit():
    ad = request.form.get('ad')
    telefon = request.form.get('telefon')
    mesaj = request.form.get('mesaj')

    # E-mail məzmunu
    email_content = f"Yeni müraciət:\n\nAd: {ad}\nTelefon: {telefon}\nMesaj: {mesaj}"

    # E-mail başlıqları
    msg = MIMEText(email_content)
    msg['Subject'] = 'Saytdan Yeni Müraciət'
    msg['From'] = GMAIL_USER
    msg['To'] = GMAIL_USER  # Özünə göndərmək üçün

    # SMTP server ilə göndərmək
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.send_message(msg)

    return 'Təşəkkürlər! Mesajınız uğurla göndərildi.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
