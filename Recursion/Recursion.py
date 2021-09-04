from typing import Optional, Union


# Optional means [type, None]https://stackoverflow.com/questions/51710037/how-should-i-use-the-optional-type-hint
def to_power(x: Optional[Union[int, float]], exp: int) -> Optional[Union[int, float]]:  
    if exp == 1:
        return x
    if exp > 1:
        return (x * to_power(x, exp - 1))


print(to_power(3.5, 2))


def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if len(looking_str) <= 1:
        return True
    if looking_str[0] != looking_str[-1]:
        return False
    return is_palindrome(looking_str[1:-1])


print(is_palindrome("daads"))


def mult(a: int, n: int) -> int:
    if a == 1:
        return n
    if n == 1:
        return a
    else:
        return a + mult(a, (n - 1))


print(mult(2, 3))


def reverse(input_str: str) -> str:
    if len(input_str) == 0:
        return " "
    else:
        return input_str[-1] + reverse(input_str[0: -1])


print(reverse("hello"))


def sum_of_digits(digit_string: str) -> int:
    if len(digit_string) == 1:
        return int(digit_string)
    else:
        return int(digit_string[0]) + sum_of_digits(digit_string[1:])


print(sum_of_digits("35"))
