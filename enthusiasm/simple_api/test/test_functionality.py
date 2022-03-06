import base64
import io
import pytest
import random
import requests

from PIL import Image, ImageFilter


def save_response_img(encoded_response_img: str, path: str):
    img = bytes(encoded_response_img, "ascii")
    img = base64.b64decode(img)
    img = Image.open(io.BytesIO(img))
    img.save(path)


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

    save_response_img(response.json()["payload"], "./test_result_imgs/gray_scale_test." + image_path.split('.')[-1])
    assert response.json()["payload"] == img_encoded


def test_deblur():
    image_path = "./test_img.jpg"
    img_content = bytes(image_path.split('.')[-1].upper() + '!', "ascii")
    img_content += open(image_path, "rb").read()
    encoded_img = base64.b64encode(img_content)
    data = {"payload": str(encoded_img)[2:-1]}
    url = "http://127.0.0.1:5000/deblur"
    response = requests.post(url, json=data)

    img = Image.open(image_path)
    img = img.filter(ImageFilter.SHARPEN)
    buff = io.BytesIO()
    img.save(buff, format="JPEG" if image_path.split('.')[-1].upper() == "JPG" else image_path.split('.')[-1])
    img_bytes = buff.getvalue()
    img_encoded = str(base64.b64encode(img_bytes))[2:-1]

    save_response_img(response.json()["payload"], "./test_result_imgs/deblur_test." + image_path.split('.')[-1])
    assert response.json()["payload"] == img_encoded


def test_crop():
    image_path = "./test_img.jpg"
    img = Image.open(image_path)
    width, height = img.size
    bbox = [random.randint(0, width), random.randint(0, height)]
    bbox += [random.randint(bbox[0], width), random.randint(bbox[1], height)]

    img_content = bytes(image_path.split('.')[-1].upper() + '!', "ascii")
    img_content += open(image_path, "rb").read()
    encoded_img = base64.b64encode(img_content)
    data = {"payload": str(encoded_img)[2:-1], "bbox": bbox}
    url = "http://127.0.0.1:5000/crop"
    response = requests.post(url, json=data)

    img = img.crop(bbox)
    buff = io.BytesIO()
    img.save(buff, format="JPEG" if image_path.split('.')[-1].upper() == "JPG" else image_path.split('.')[-1])
    img_bytes = buff.getvalue()
    img_encoded = str(base64.b64encode(img_bytes))[2:-1]

    save_response_img(response.json()["payload"], "./test_result_imgs/crop_test." + image_path.split('.')[-1])
    assert response.json()["payload"] == img_encoded


@pytest.mark.parametrize(
    "rotate_angle", [90, 30, -45, -120]
)
def test_rotate(rotate_angle: int):
    image_path = "./test_img.jpg"
    img = Image.open(image_path)

    img_content = bytes(image_path.split('.')[-1].upper() + '!', "ascii")
    img_content += open(image_path, "rb").read()
    encoded_img = base64.b64encode(img_content)
    data = {"payload": str(encoded_img)[2:-1], "angle": rotate_angle}
    url = "http://127.0.0.1:5000/rotate"
    response = requests.post(url, json=data)

    img = img.rotate(rotate_angle, expand=True)
    buff = io.BytesIO()
    img.save(buff, format="JPEG" if image_path.split('.')[-1].upper() == "JPG" else image_path.split('.')[-1])
    img_bytes = buff.getvalue()
    img_encoded = str(base64.b64encode(img_bytes))[2:-1]

    save_response_img(response.json()["payload"], "./test_result_imgs/rotate_test_" + str(rotate_angle) + "." + image_path.split('.')[-1])
    assert response.json()["payload"] == img_encoded
