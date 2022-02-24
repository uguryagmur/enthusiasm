import re
import string
from typing import Dict


class Base64:
    def __init__(Base64):
        pass

    @staticmethod
    def encode(file_path: str) -> str:
        binary_input = Base64._extract_binaries_from_file(file_path)
        padding, zeros_size = Base64._calculate_encoding_padding_size_and_zeros(
            binary_input
        )
        binary_input += "".join(["0"] * zeros_size)
        return Base64._encode(binary_input, padding)

    @staticmethod
    def decode(base64_code: str, file_path: str):
        padding_size = len(re.findall("=", base64_code))
        encoded = base64_code[:-padding_size] if padding_size > 0 else base64_code
        table = Base64._generate_decode_table()
        binary_array = "".join([table[elem] for elem in encoded])
        binary_array = binary_array[: -(len(binary_array) % 8)]
        binaries = bytearray()
        for i in range(len(binary_array) // 8):
            binaries.append(int(binary_array[i * 8 : (i + 1) * 8], 2))
        with open(file_path, "wb") as file:
            file.write(binaries)

    @staticmethod
    def _extract_binaries_from_file(file_path: str) -> str:
        binary_file = ""
        with open(file_path, "rb") as f:
            for line in f.readlines():
                binary_file += "".join(["{:08b}".format(l) for l in line])
        return binary_file

    @staticmethod
    def _calculate_encoding_padding_size_and_zeros(binary_string: str) -> int:
        extra_zeros = 6 - len(binary_string) % 6 if len(binary_string) % 6 != 0 else 0
        zeros_size = extra_zeros
        padding = 0
        while extra_zeros != 0:
            padding += 1
            extra_zeros = (extra_zeros + 6) % 8
        return padding, zeros_size

    @staticmethod
    def _encode(binary_string: str, padding: int) -> str:
        encoded = Base64._encode_characters(binary_string)
        encoded += "".join(["="] * padding)
        return encoded

    @staticmethod
    def _encode_characters(binary_string: str) -> str:
        encoded = ""
        table = Base64._generate_encode_table()
        for i in range(len(binary_string) // 6):
            encoded += table[binary_string[i * 6 : (i + 1) * 6]]
        return encoded

    @staticmethod
    def _generate_encode_table() -> Dict[bytes, str]:
        base64_chars = (
            string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"
        )
        base64_encode_table = dict()
        for i, elem in enumerate(base64_chars):
            base64_encode_table["{:06b}".format(i)] = elem
        return base64_encode_table

    @staticmethod
    def _generate_decode_table() -> Dict[bytes, str]:
        base64_chars = (
            string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"
        )
        base64_decode_table = dict()
        for i, elem in enumerate(base64_chars):
            base64_decode_table[elem] = "{:06b}".format(i)
        return base64_decode_table
