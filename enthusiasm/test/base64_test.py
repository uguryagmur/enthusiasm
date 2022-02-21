import base64
import filecmp
import pytest

from ..src.base64 import Base64


def get_file_as_binary(file_path: str):
    file_content = b""
    with open(file_path, "rb") as file:
        for line in file:
            file_content += line
    return file_content


def test_encode_to_base64():
    file_path = "/home/adm1n/Shop/enthusiasm/enthusiasm/test/base64_test.py"
    computed_encoding = Base64.encode(file_path)
    expected_encoding = str(base64.b64encode(get_file_as_binary(file_path)))[2:-1]
    assert computed_encoding == expected_encoding