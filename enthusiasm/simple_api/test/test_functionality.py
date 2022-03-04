import base64
import io
import requests

from PIL import Image, ImageFilter


def test_gray_scale():
    image_path = "./test_img.jpg"
    img_content = bytes(image_path.split('.')[-1].upper() + '!', "ascii")
    img_content += open(image_path, "rb").read()
    encoded_img = base64.b64encode(img_content)
    data = {"payload": str(encoded_img)[2:-1]}
    url = "http://127.0.0.1:5000/gray_scale"
    response = requests.post(url, json=data)

    img = Image.open(image_path)
    img = img.convert('L')
    buff = io.BytesIO()
    img.save(buff, format="JPEG" if image_path.split('.')[-1].upper() == "JPG" else image_path.split('.')[-1])
    img_bytes = buff.getvalue()
    img_encoded = str(base64.b64encode(img_bytes))[2:-1]

    assert response.json()["payload"] == img_encoded
