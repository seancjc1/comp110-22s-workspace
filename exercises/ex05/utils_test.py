"""Unit tests for utilities program."""

__author__ = "730358979"

from utils import only_evens, sub, concat


def test_only_evens_odd_list() -> None:
    """Tests function when given only odd numbers."""
    xs: list[int] = [1, 3, 5, 7]
    assert only_evens(xs) == []


def test_only_evens_even_list() -> None:
    """Tests function when given only even numbers."""
    xs: list[int] = [4, 4, 4]
    assert only_evens(xs) == [4, 4, 4]


def test_only_evens_empty() -> None:
    """Tests function when given empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_sub_standard() -> None:
    """Tests function's basic objective."""
    xs: list[int] = [1, 2, 3, 4, 5]
    assert sub(xs, 2, 4) == [3, 4] 

    
def test_sub_out_of_bounds() -> None:
    """Tests function when given parameters out of range of list indices."""
    xs: list[int] = [1, 2, 3, 4, 5]
    assert sub(xs, -1, 5) == [1, 2, 3, 4, 5]


def test_sub_empty() -> None:
    """Tests function when given empty list."""
    xs: list[int] = []
    assert sub(xs, 0, 0) == []


def test_concat_standard() -> None: 
    """Tests function's basic objective."""
    xs0: list[int] = [1, 2, 3, 4, 5]
    xs1: list[int] = [6, 7, 8, 9, 10]
    assert concat(xs0, xs1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_concat_single() -> None:
    """Tests functions when given lists with a single index."""
    xs0: list[int] = [1]
    xs1: list[int] = [2]
    assert concat(xs0, xs1) == [1, 2]


def test_concat_empty() -> None:
    """Test function when given empty lists."""
    xs0: list[int] = []
    xs1: list[int] = []
    assert concat(xs0, xs1) == []