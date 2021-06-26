# Create a Fraction class, which will represent all basic arithmetic logic for fractions (+, -, /, *) with appropriate
# checking and error handling
# https://www.youtube.com/watch?v=o1fUy3mnEQE
def fraction_to_list(our_list_1, our_list_2):
    # Спільний знаменник
    try:
        first_list = our_list_1.split('/')
        second_list = our_list_2.split('/')
        final_list = []
        final_list.append(float(second_list[1]) * float(first_list[0]))
        final_list.append(float(second_list[1]) * float(first_list[1]))
        final_list.append(float(first_list[1]) * float(second_list[0]))
        final_list.append(float(second_list[1]) * float(first_list[1]))
        return final_list
    except ValueError:
        print('Must be a numbers')
    except ZeroDivisionError:
        print('Denominator cant be 0')
    except IndexError:
        print('This is not a fraction')


def smart_div(my_list):
    # Cпрощення
    nominator = int(my_list[0])
    denominator = int(my_list[1])
    least_common_divisor = max(abs(nominator), abs(denominator))
    for search_item in range(least_common_divisor, 1, -1):
        if abs(nominator) % search_item == 0 and abs(denominator) % search_item == 0 and nominator != 0:
            nominator /= search_item
            denominator /= search_item
    if nominator < 0 and denominator < 0:
        nominator *= -1
        denominator *= -1
    elif denominator < 0:
        denominator *= -1
    my_list.clear()
    my_list.append(int(nominator))
    my_list.append(int(denominator))
    return my_list


class Fraction:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('Wrong argument')
        our_fraction_in_list = fraction_to_list(self.value, other.value)
        try:
            answer_nominator = float(our_fraction_in_list[0] + float(our_fraction_in_list[2]))
            answer_denominator = float(our_fraction_in_list[1])
            final_answer = smart_div([answer_nominator, answer_denominator])
            if final_answer[-1] == 1:
                return Fraction(f'{final_answer[0]}')
            if final_answer[0] == 0:
                return Fraction(f'{final_answer[0]}')
            else:
                return Fraction(f'{final_answer[0]}/{final_answer[-1]}')
        except TypeError:
            print('Incorrect datas')

    def __sub__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('Невірний тип аргументу')
        our_fraction_in_list = fraction_to_list(self.value, other.value)
        try:
            answer_nominator = float(our_fraction_in_list[0]) - float(our_fraction_in_list[2])
            answer_denominator = float(our_fraction_in_list[1])
            final_answer = smart_div([answer_nominator, answer_denominator])
            if final_answer[-1] == 1:
                return Fraction(f'{final_answer[0]}')
            if final_answer[0] == 0:
                return Fraction(f'{final_answer[0]}')
            else:
                return Fraction(f'{final_answer[0]}/{final_answer[-1]}')
        except TypeError:
            print('Incorrect datas')

    def __mul__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('Incorrect type')
        our_fraction_in_list = fraction_to_list(self.value, other.value)
        try:
            answer_nominator = float(our_fraction_in_list[0]) * float(our_fraction_in_list[2])
            answer_denominator = float(our_fraction_in_list[1]) * float(our_fraction_in_list[3])
            final_answer = smart_div([answer_nominator, answer_denominator])
            if final_answer[-1] == 1:
                return Fraction(f'{final_answer[0]}')
            if final_answer[0] == 0:
                return Fraction(f'{final_answer[0]}')
            else:
                return Fraction(f'{final_answer[0]}/{final_answer[-1]}')
        except TypeError:
            print('Incorrect type')

    def __truediv__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('Incorrect type')
        our_fraction_in_list = fraction_to_list(self.value, other.value)
        try:
            answer_nominator = int(our_fraction_in_list[0] * our_fraction_in_list[3])
            answer_denominator = int(our_fraction_in_list[1] * our_fraction_in_list[2])
            final_answer = smart_div([answer_nominator, answer_denominator])
            if final_answer[-1] == 1:
                return Fraction(f'{final_answer[0]}')
            if final_answer[0] == 0:
                return Fraction(f'{final_answer[0]}')
            else:
                return Fraction(f'{final_answer[0]}/{final_answer[-1]}')
        except TypeError:
            print('Incorrect datas')

    def __str__(self):
        return f'Answer: {self.value}'

    def __repr__(self):
        return self.__str__()


x = Fraction('10/16')
y = Fraction('2/27')

print(x + y)
print(x - y)
print(x * y)
print(x / y)
