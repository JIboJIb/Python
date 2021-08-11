def count_lines(name):
    with open(name, 'r', encoding='utf-8') as i:
        my_lines = i.readlines()
    return len(my_lines)


def count_chars(name):
    with open(name, 'r', encoding='utf-8') as i:
        my_chars = i.read()
    return len(my_chars)


def test(name):
    return f"Lines: {count_lines(name)} chars {count_chars(name)}"
