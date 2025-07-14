#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Fix: decrement n to avoid infinite loop
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <non-negative integer>".format(sys.argv[0]))
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        if number < 0:
            raise ValueError("Negative input is not allowed")
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)

    f = factorial(number)
    print(f)
