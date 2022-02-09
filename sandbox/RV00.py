"""Review session function writing."""

__author__ = "730358979"


def remove_ws(word: str) -> str:
    new_word: str = ""
    i: int = 0
    while i < len(word):
        if word[i] != " ":
            new_word += word[i]
        i += 1
    return new_word