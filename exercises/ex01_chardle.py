"""Exercise 01 for COMP110 - Chardle."""

__author__ = "730358979"

guess_word: str = input("Enter a 5-character word: ")
single_character: str = input("Enter a single character: ")

print("Searching for " + single_character + " in " + guess_word)

if single_character == guess_word[0]:
    print(single_character + " found at index 0")

if single_character == guess_word[1]:
    print(single_character + " found at index 1")

if single_character == guess_word[2]:
    print(single_character + " found at index 2")

if single_character == guess_word[3]:
    print(single_character + " found at index 3")

if single_character == guess_word[4]:
    print(single_character + " found at index 4")