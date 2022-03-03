"""Unit tests for dictionary functions."""

__author__ = "730358979"

from dictionary import invert, favorite_color, count


def test_invert() -> None:
    """Tests the invert function's main use."""
    ys: dict[str, str] = {"a": "z", "b": "y", "c": "x"}
    assert invert(ys) == {"z": "a", "y": "b", "x": "c"}


def test_invert_single() -> None:
    """Tests the invert function when given a dictionary with a single key-value pair."""
    ys: dict[str, str] = {"hootie": "blowfish"}
    assert invert(ys) == {"blowfish": "hootie"}


def test_invert_empty() -> None:
    """Tests the invert function when given an empty dictionary."""
    ys: dict[str, str] = dict()
    assert invert(ys) == {}


def test_fav_color() -> None:
    """Tests the favorite color function's main use."""
    ys: dict[str, str] = {"john": "blue", "jane": "green", "sean": "green"}
    assert favorite_color(ys) == "green"


def test_fav_color_same_number() -> None:
    """Tests the favorite color function when given a dictionary with a single key-value pair."""
    ys: dict[str, str] = {"john": "blue", "jane": "blue", "sean": "green", "lara": "green"}
    assert favorite_color(ys) == "blue"


def test_fav_color_empty() -> None:
    """Tests the favorite color function when given an empty dictionary."""
    ys: dict[str, str] = {}
    assert favorite_color(ys) == ""


def test_count() -> None:
    """Tests the count function's main use."""
    xs: list[str] = ["alex", "jake", "sean", "sean"]
    assert count(xs) == {"alex": 1, "jake": 1, "sean": 2}


def test_count_single() -> None:
    """Tests the count function when given a list of a single item."""
    xs: list[str] = ["alex"]
    assert count(xs) == {"alex": 1}


def test_count_empty() -> None:
    """Tests the count function when given an empty list."""
    xs: list[str] = []
    assert count(xs) == {}