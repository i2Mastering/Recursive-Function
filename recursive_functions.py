"""
Recursive Functions in Python

This Python module demonstrates two recursive functions:
- `binary_expansion(n)`: Determines the number of binary digits needed to represent a given number.
- `sum_of_squares(n)`: Computes the sum of squares from 1 to n.

## Features:
- Uses recursion to calculate binary digit length.
- Implements a recursive approach to summing squares.
- Provides test cases to validate functionality.

## Functions:
### `binary_expansion(n)`
- **Description:** Recursively calculates the number of binary digits required to represent `n`.
- **Arguments:**
  - `n (int)`: The number to be converted into binary.
- **Returns:**
  - `int`: The number of binary digits.
- **Example Usage:**
  ```python
  binary_expansion(256)  # Returns 9
  binary_expansion(750)  # Returns 10
  ```

### `sum_of_squares(n)`
- **Description:** Recursively calculates the sum of squares from `1` to `n`.
- **Arguments:**
  - `n (int)`: The upper bound for summation.
- **Returns:**
  - `int`: The sum of squares.
- **Example Usage:**
  ```python
  sum_of_squares(12)  # Returns 650
  sum_of_squares(20)  # Returns 2870
  ```

### `main()`
- **Description:** Calls test functions for both recursive implementations.
- **Example Usage:**
  ```python
  python recursive_functions.py
  ```
- **Output:**
  ```sh
  Number of binary digits in 256 is 9
  Number of binary digits in 750 is 10
  Sum of all squares for n=12: 650.
  Sum of all squares for n=20: 2870.
  ```

## Author:
Ike Iloegbu

## License:
MIT
"""

def binary_expansion(n):
    """Recursively computes the number of binary digits required to represent `n`.
    
    Args:
        n (int): The number to be represented in binary.
    
    Returns:
        int: Number of binary digits required.
    
    Example:
        >>> binary_expansion(256)
        9
        >>> binary_expansion(750)
        10
    """
    if n == 1:
        return 1
    return 1 + binary_expansion(n // 2)

def sum_of_squares(n):
    """Recursively computes the sum of squares from 1 to `n`.
    
    Args:
        n (int): Upper bound for summation.
    
    Returns:
        int: Sum of squares from 1 to `n`.
    
    Example:
        >>> sum_of_squares(12)
        650
        >>> sum_of_squares(20)
        2870
    """
    if n == 1:
        return 1
    return sum_of_squares(n - 1) + n**2

def main():
    """Main function that runs test cases for binary expansion and sum of squares."""
    def call_Binary_Exp():
        n1 = 256
        n2 = 750
        print(f"Number of binary digits in {n1} is {binary_expansion(n1)}")
        print(f"Number of binary digits in {n2} is {binary_expansion(n2)}")
    
    def call_Squares():
        n1 = 12
        n2 = 20
        print(f"Sum of all squares for n={n1}: {sum_of_squares(n1)}.")
        print(f"Sum of all squares for n={n2}: {sum_of_squares(n2)}.")
    
    call_Binary_Exp()
    call_Squares()

if __name__ == "__main__":
    main()
