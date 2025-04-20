import pytest
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fizzbuzz import fizzbuzz


@pytest.mark.parametrize("n,expected", [
    (0, []),
    (1, ["1"]),
    (3, ["1", "2", "Fizz"]),
    (5, ["1", "2", "Fizz", "4", "Buzz"]),
    (15, [
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz"
    ]),
])
def test_fizzbuzz_sequence(n, expected):
    assert fizzbuzz(n) == expected


@pytest.mark.parametrize("i,expected", [
    (1, "1"),
    (3, "Fizz"),
    (5, "Buzz"),
    (15, "FizzBuzz"),
    (16, "16"),
])
def test_fizzbuzz_last_value(i, expected):
    # The last element of the sequence for n == i should match expected
    assert fizzbuzz(i)[-1] == expected
