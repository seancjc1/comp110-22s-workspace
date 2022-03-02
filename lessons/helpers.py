"""Demonstrate defining a module imported elsewhere."""

__author__ = "730358979"

THE_ANSWER: int = 42


def main() -> None:
    print(powerful(2, 10))
    print("helpers.py run as a module")


def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n


# Ididom for making a module able to run as a program
# Or have its global definitons imported elsewhere
if __name__ == "__main__":
    main()
else:
    # It is not idiomatic to have an else branch
    print(f"helpers.py was imported: {__name__}")