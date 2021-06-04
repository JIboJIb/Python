# =============================================================================
# Create a program that reads an input string and then creates and prints 
# 5 random strings from characters of the input string.
# For example, the program obtained the word ‘hello’, so it should print
# 5 random strings(words) that combine characters 
# ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …
# Tips: Use random module to get random char from string)
# =============================================================================
import random
i = 0
word = input("Write any word:  ")
while True:
    if len(word) >= 5 and word.isalpha():
        while i < 5:
            random_word = random.sample(word, len(word))
            print("".join(random_word))
            i = i+1
        break
    else:
        print("The word must contain 5 or more letters")
        word = input("Write any word with 5 or more letters:  ")