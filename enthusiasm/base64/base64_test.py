import base64
import filecmp
import os
import pytest

from .base64 import Base64


def get_file_as_binary(file_path: str):
    file_content = b""
    with open(file_path, "rb") as file:
        for line in file:
            file_content += line
    return file_content


def test_encode_to_base64():
    file_path = "/home/adm1n/Shop/enthusiasm/enthusiasm/base64/base64_test.py"
    computed_encoding = Base64.encode(file_path)
    expected_encoding = str(base64.b64encode(get_file_as_binary(file_path)))[2:-1]
    assert computed_encoding == expected_encoding


def test_decode_from_base64():
    file_path = "/home/adm1n/Shop/enthusiasm/enthusiasm/base64/base64_test.py"
    output_path = "/home/adm1n/Shop/enthusiasm/enthusiasm/shit"
    base64_encoding = str(base64.b64encode(get_file_as_binary(file_path)))[2:-1]
    Base64.decode(base64_encoding, output_path)
    assert filecmp.cmp(file_path, output_path)
    os.remove(output_path)
