"""A set of dictionary-based functions for Exercise 06 - Dictionary Functions."""

__author__ = "730358979"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a given dictionary."""
    inversion: dict[str, str] = dict()
    for key in dictionary:
        if dictionary[key] in inversion: 
            raise KeyError("No") 
        inversion[dictionary[key]] = key
    return inversion


def favorite_color(colors: dict[str, str]) -> str:
    """Determines favorite color based on frequency in given dictionary."""
    color: str = ""
    favorites: dict[str, int] = dict()
    for key in colors:
        if colors[key] in favorites:
            favorites[colors[key]] += 1
        else:
            favorites[colors[key]] = 1
    counter: int = 0
    for key in favorites:
        if favorites[key] > counter:
            counter = favorites[key]
            color = key
    return color


def count(given_list: list[str]) -> dict[str, int]:
    """Calculate number of times a string appears in a given list."""
    frequency: dict[str, int] = dict()
    for string in given_list:
        if string in frequency:
            frequency[string] += 1
        else:
            frequency[string] = 1
    return frequency