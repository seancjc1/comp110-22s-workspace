"""Exercise 3 for COMP110 - Structured Wordle."""

__author__ = 730358979


def contains_char(search_word: str, char: str) -> bool:
    """A function to search for a character in a given string."""
    assert len(char) == 1
    i: int = 0
    while i < len(search_word):
        if search_word[i] == char:
            return True
        else:
            i += 1
    return False


def emojified(guess_word: str, secret: str) -> str:
    """Returns an emoji which determines correctness of guess."""
    assert len(guess_word) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    result: str = ""
    while i < len(secret): 
        if contains_char and guess_word[i] == secret[i]:
            result += GREEN_BOX
        elif contains_char and guess_word[i] != secret[i]:
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        i = i + 1
    return result


def input_guess(expected_length: int) -> str:
    """Prompts user for a guess of specified length."""
    guess: str = input(f"Enter a {expected_length}-character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn\'t {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    SECRET: str = "codes"
    turns: int = 6
    win: bool = True
    while turns > 0 and not win:
        print(f"=== Turn {turns}/6 ===")
        input_guess(len(SECRET))
        emojified(str(input_guess), SECRET)
        if input_guess == SECRET:
            win
        else:
            turns -= 1
    if win:
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")
