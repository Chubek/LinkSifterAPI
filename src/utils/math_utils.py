from typing import Union


def clamp(
    value: Union[int, float],
    max_val: Union[int, float],
    min_val: Union[int, float]
) -> Union[int, float]:
    return min(max(value, min_val), max_val)
