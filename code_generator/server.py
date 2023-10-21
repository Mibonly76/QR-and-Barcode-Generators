from flask import Flask, render_template, request
from waitress import serve
from qr_code_generator import qr_encoder


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/request')
def get_qrcode():
    data = request.args.get('data')
    png_image = qr_encoder(data)
    return render_template("qrcode.html", image_name=data, image_png=png_image)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
