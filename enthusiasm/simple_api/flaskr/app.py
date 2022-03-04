import base64
import io
import os

from flask import Flask, request
from PIL import Image, ImageFilter


welcome_text = """
\tWELCOME TO Simple Image (Img) API

API command routes:
    gray_scale -> converts your image to a gray scale
    deblur -> deblurs (sharpens) your image
    crop -> crops the image with rectangle coordinates provided (top_left, bottom_right) 
    flip -> flips the image 90 degrees right or left

\t Enjoy !!!
"""


app = Flask(__name__, instance_relative_config=True)


def configure_app():
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'simg_api.sqlite')
    )
    initialize_instance_dir(app)


def initialize_instance_dir(app: Flask):
    try:
        os.makedir(app.instance_path)
    except:
        pass


@app.route('/')
def root():
    return welcome_text


@app.route("/test_response", methods={"POST"})
def response_test():
    return "SUCCESS"


@app.route("/test_payload", methods={"POST"})
def payload_test():
    print(request.form)
    return request.form


@app.route("/gray_scale", methods={"POST"})
def gray_scale():
    json_data = request.get_json()
    payload = bytes(json_data["payload"], "ascii")
    payload = base64.b64decode(payload)
    payload = payload.split(b'!')
    file_format = str(payload[0]).lower()[2:-1]
    image_data = b'!'.join(payload[1:])
    img = Image.open(io.BytesIO(image_data))
    img = img.convert("L")
    buff = io.BytesIO()
    img.save(buff, format="JPEG" if file_format.upper() == "JPG" else file_format.upper())
    result_bytes = buff.getvalue()
    encoded_result = str(base64.b64encode(result_bytes))[2:-1]
    return {"payload": encoded_result}
    

@app.route("/deblur", methods={"POST"})
def deblur():
    json_data = request.get_json()
    payload = bytes(json_data["payload"], "ascii")
    payload = base64.b64decode(payload)
    payload = payload.split(b'!')
    file_format = str(payload[0]).lower()[2:-1]
    image_data = b'!'.join(payload[1:])
    img = Image.open(io.BytesIO(image_data))
    img = img.convert("L")
    buff = io.BytesIO()
    img.save(buff, format="JPEG" if file_format.upper() == "JPG" else file_format.upper())
    result_bytes = buff.getvalue()
    encoded_result = str(base64.b64encode(result_bytes))[2:-1]
    return {"payload": encoded_result}
    

@app.route("/crop", methods={"POST"})
def crop():
    json_data = request.get_json()
    payload = bytes(json_data["payload"], "ascii")
    payload = base64.b64decode(payload)
    payload = payload.split(b'!')
    file_format = str(payload[0]).lower()[2:-1]
    image_data = b'!'.join(payload[1:])
    img = Image.open(io.BytesIO(image_data))
    img = img.convert("L")
    buff = io.BytesIO()
    img.save(buff, format="JPEG" if file_format.upper() == "JPG" else file_format.upper())
    result_bytes = buff.getvalue()
    encoded_result = str(base64.b64encode(result_bytes))[2:-1]
    return {"payload": encoded_result}
    

@app.route("/flip", methods={"POST"})
def flip():
    json_data = request.get_json()
    payload = bytes(json_data["payload"], "ascii")
    payload = base64.b64decode(payload)
    payload = payload.split(b'!')
    file_format = str(payload[0]).lower()[2:-1]
    image_data = b'!'.join(payload[1:])
    img = Image.open(io.BytesIO(image_data))
    img = img.convert("L")
    buff = io.BytesIO()
    img.save(buff, format="JPEG" if file_format.upper() == "JPG" else file_format.upper())
    result_bytes = buff.getvalue()
    encoded_result = str(base64.b64encode(result_bytes))[2:-1]
    return {"payload": encoded_result}
    

if __name__ == "__main__":
    configure_app()
    app.run(port=5000)
