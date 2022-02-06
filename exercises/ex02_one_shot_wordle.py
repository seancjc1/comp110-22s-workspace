"""Exercise 02 for COMP 110 - One-Shot Wordle."""

__author__ = "730358970"

SECRET: str = "farter"  # initialization of variables, gathering input, and invalid input while loop

guess_word: str = input(f"What is your {len(SECRET)}-letter guess? ")

while len(guess_word) != len(SECRET):
    guess_word = input(f"That was not {len(SECRET)} letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0
result: str = ""


while i < len(SECRET):  # while loop to check indices for correct matches
    if guess_word[i] == SECRET[i]:
        result = result + GREEN_BOX
    else:
        char_location: bool = False
        alt_idx: int = 0
        while not char_location and alt_idx < len(SECRET):  # nested while loop to check for correct letters at incorrect positions
            if guess_word[i] == SECRET[alt_idx]:
                char_location = True
            else:
                alt_idx = alt_idx + 1
        if char_location:
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX
    i = i + 1

print(result)  # prints a result based on emojis from checking indices

if guess_word == SECRET: 
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")