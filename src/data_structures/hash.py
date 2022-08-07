from typing import Any, List


def make_key_hash(obj: Any) -> int:
    str_obj = str(obj)

    bins_rev = [int(j)^1 for j in
        sum([list(f"{x:08b}") 
        for x in str_obj], [])]

    while len(bins_rev) % 8 != 0:
        bins_rev = [0] + bins_rev
        
    def to_decimal(ls: List[int]) -> int:
        sum = 0

        for i, l in enumerate(ls):
            sum += l * (2**i)

            return sum

    return abs(sum([
        to_decimal(bins_rev[i:i + 8])
                for i in range(0, len(bins_rev), 8)
    ]))