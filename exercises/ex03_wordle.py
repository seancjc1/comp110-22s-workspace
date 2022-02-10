"""Exercise 3 for COMP110 - Structured Wordle."""

__author__ = "730358979"


def contains_char(search_word: str, char: str) -> bool:  # declaration of contains_char function
    """Searches for a character in a given string, then returns a resulting boolean value."""
    assert len(char) == 1
    i: int = 0
    while i < len(search_word):  # while loop to check indices for matching characters
        if search_word[i] == char:
            return True
        else:
            i += 1
    return False


def emojified(guess_word: str, secret: str) -> str:  # declaration of emojified function
    """Returns an emoji which determines correctness of guess."""
    assert len(guess_word) == len(secret)  # assertion and declaration of variables
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    result: str = ""
    while i < len(secret):  # while loop which utilizes the contains_char function  
        if contains_char(secret, guess_word[i]):  # to check indices of the user's input 
            if guess_word[i] == secret[i]:  # for characters that match characters in the secret's indices
                result += GREEN_BOX
                i = i + 1
            else:
                result += YELLOW_BOX
                i = i + 1
        else:
            result += WHITE_BOX
            i = i + 1
    return result


def input_guess(expected_length: int) -> str:  # declaration of the input_guess function
    """Prompts user for a guess of specified length."""
    user_guess: str = input(f"Enter a {expected_length} character word: ")
    while len(user_guess) != expected_length:  # while loop which checks for poor end-user input 
        user_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return user_guess


def main() -> None:  # declaration of the main function
    """Entrypoint of the program and main game loop."""
    SECRET: str = "codes"
    turns: int = 1
    win: bool = False
    while turns <= 6 and not win:  # while loop which utilizes the previously declared functions
        print(f"=== Turn {turns}/6 ===")  # to produce the game
        user_guess: str = input_guess(len(SECRET))
        print(emojified(user_guess, SECRET))
        if user_guess == SECRET:
            win = True
        else:
            turns += 1
    if win:  # if-else statement which determines output upon win or loss
        print(f"You won in {turns}/6 turns!")
    else:
        print(f"The word was {SECRET}!")
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":  # if statement from website which allows 
    main()  # for running as module in REPL and importing functions to other modules
