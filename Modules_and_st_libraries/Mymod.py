def count_lines(name):
    with open(name, 'r') as i:
        my_lines = i.readlines()
    return len(my_lines)


if __name__ == '__main__':
    print(count_lines('Mike Inez.txt'))
