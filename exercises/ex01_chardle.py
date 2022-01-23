"""Exercise 01 for COMP110 - Chardle."""

__author__ = "730358979"

guess_word: str = input("Enter a 5-character word: ")

if len(guess_word) != 5:
    print("Error: Response must be a 5 letter word.")
    quit()

single_character: str = input("Enter a single character: ")

if len(single_character) != 1:
    print("Error: Response must be a single character.")
    quit()

print("Searching for " + single_character + " in " + guess_word)

indices: int = 0

if single_character == guess_word[0]:
    print(single_character + " found at index 0")
    indices = indices + 1
if single_character == guess_word[1]:
    print(single_character + " found at index 1")
    indices = indices + 1
if single_character == guess_word[2]:
    print(single_character + " found at index 2")
    indices = indices + 1
if single_character == guess_word[3]:
    print(single_character + " found at index 3")
    indices = indices + 1
if single_character == guess_word[4]:
    print(single_character + " found at index 4")
    indices = indices + 1

if indices == 0:
    print("No instances of " + single_character + " found in " + guess_word)
if indices == 1:
    print("1 instance of " + single_character + " found in " + guess_word)
if indices == 2:
    print("2 instances of " + single_character + " found in " + guess_word)
if indices == 3:
    print("3 instances of " + single_character + " found in " + guess_word)
if indices == 4:
    print("4 instances of " + single_character + " found in " + guess_word)
if indices == 5:
    print("5 instances of " + single_character + " found in " + guess_word)
