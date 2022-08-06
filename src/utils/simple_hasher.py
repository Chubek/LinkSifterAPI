from typing import List


def str_bits_to_list(bits_str: str) -> List[int]:
    return [int(i) for i in list(bits_str)]

def reverse_bits(bits: List[int]) -> List[int]:
    return [u ^ 1 for u in bits]

def eight_bit_to_byte(bits: List[int]) -> int:
    return sum([u*(2**i) for u, i in enumerate(bits)])

def get_all_bytes(bits: List[int]) -> List[int]:
    while len(bits) % 8 != 0:
        bits = [0] + bits

    return [eight_bit_to_byte(
        eight_bit_to_byte(bits[i:i + 8])
    )
        for i in range(0, len(bits), 8)
    ]

def get_final_str(bytes: List[str]) -> str:
    fin_str = ""

    for byte in bytes:
        fin_str += chr(byte)

def hasher(*args) -> str:
    bits_str = []

    for arg in args:
        bits_str += f"{arg:08b}"


    list_bits = str_bits_to_list(bits_str)
    bits_reversed = reverse_bits(list_bits)
    all_bytes = get_all_bytes(bits_reversed)
    final_str = get_final_str(all_bytes)


    return final_str

    