# Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and
# the number of occurrences as values.
string = "Make() a program that has some sentence (a string) on input and returns a dict containing all unique words " \
         "as keys and the number of occurrences as values. ".lower()
marks = '!()-[]{};?@#$%:\,./^&;*_'
for mark in marks:
    string = string.replace(mark, " ")
strings = string.split()
dict = {word: strings.count(word) for word in strings}
print(dict)
