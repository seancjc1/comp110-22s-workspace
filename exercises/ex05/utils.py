"""Function skeletons and implementations."""

__author__ = "730358979"


def only_evens(given_list: list[int]) -> list[int]:
    """Returns the even numbers of given list."""
    even_list: list[int] = []
    i: int = 0 
    while i < len(given_list):
        if given_list[i] == ((given_list[i]) // 2) * 2:
            even_list.append(given_list[i])
        i += 1
    return even_list


def sub(given_list: list[int], start: int, end: int) -> list[int]:
    """Generates subset of given list based on start and end arguments."""
    i: int = 0
    subset: list[int] = []
    while i < len(given_list):
        if i >= start and i < end:
            subset.append(given_list[i])
        i += 1
    return subset


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Concatenates two given lists."""
    concat_list: list[int] = list_one + list_two
    return concat_list