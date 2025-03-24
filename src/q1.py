def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))): return -1
     # Swap values using arithmetic (no third variable)
    x = x + y
    y = x - y
    x = x - y
    return


def swap(a, b):
    return b, a

# Invoking the function with the scenarios:
result1 = swap("Apple", 10)
result2 = swap(9, 17)

print("Result 1:", result1)
print("Result 2:", result2)
