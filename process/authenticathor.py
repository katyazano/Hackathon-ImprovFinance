import pyotp
import qrcode
from PIL import Image
from flask import Flask, render_template, request

app = Flask(__name__)

def authenticator():
    # Genera un secreto de 16 caracteres base32
    secret = pyotp.random_base32()

    # Crea una instancia TOTP usando el secreto
    totp = pyotp.TOTP(secret)

    # Genera el código OTP
    otp_code = totp.now()

    # Imprime el secreto y el código QR
    print("Secreto:", secret)
    print("Escanee este código QR con Google Authenticator:")

    # Crea la URL para el código QR
    url = totp.provisioning_uri('usuario', issuer_name="Atrato")

    # Crea y guarda el código QR en un archivo
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_code.png")

    # Imprime el código QR en pantalla
    img.show()

@app.route('/validate', methods=['POST'])
def validate():
    otp_code = request.form['otp']

    # Validate the OTP code
    if totp.verify(otp_code):
        return "OTP is valid"
    else:
        return "OTP is invalid"
