from typing import Optional


def to_power(x: Optional[int, float], exp: int) -> Optional[int, float]:
    if exp == 1:
        return x
    if exp > 1:
        return (x * to_power(x, exp - 1))


print(to_power(2, 3))
