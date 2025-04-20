"""
FizzBuzz module.

Provides a function fizzbuzz(n) that returns the FizzBuzz sequence from 1 to n.
"""

def fizzbuzz(n):
    """
    Return a list of FizzBuzz results from 1 to n inclusive.

    For multiples of 3, 'Fizz' is returned.
    For multiples of 5, 'Buzz' is returned.
    For multiples of both 3 and 5, 'FizzBuzz' is returned.
    Otherwise, the number itself as a string is returned.

    Parameters:
        n (int): The upper limit of the sequence.

    Returns:
        List[str]: The FizzBuzz sequence.
    """
    results = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            results.append("FizzBuzz")
        elif i % 3 == 0:
            results.append("Fizz")
        elif i % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(i))
    return results

if __name__ == "__main__":
    import sys

    try:
        n = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    except ValueError:
        print("Please provide a valid integer.", file=sys.stderr)
        sys.exit(1)

    for value in fizzbuzz(n):
        print(value)