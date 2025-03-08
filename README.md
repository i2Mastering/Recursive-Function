# Recursive Functions in Python

## Description
This repository contains a Python program that demonstrates two recursive functions:
- **`binary_expansion(n)`**: Determines the number of binary digits needed to represent a given number.
- **`sum_of_squares(n)`**: Computes the sum of squares from 1 to `n`.

This program is structured to explore recursion and provides test cases to validate functionality.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)
- [Functions](#functions)
- [Requirements](#requirements)
- [License](#license)

## Features
- Implements recursion to determine binary digit length.
- Computes the sum of squares using a recursive approach.
- Provides test cases for validation.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/recursive-functions.git
   ```
2. Navigate to the project directory:
   ```sh
   cd recursive-functions
   ```
3. Ensure Python 3.x is installed.

## Usage
1. Run the script:
   ```sh
   python recursive_functions.py
   ```
2. The program will calculate and display the results for predefined test cases.

## Example Output
```sh
Number of binary digits in 256 is 9
Number of binary digits in 750 is 10
Sum of all squares for n=12: 650.
Sum of all squares for n=20: 2870.
```

## Functions
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

## Requirements
- Python 3.x

## License
This project is licensed under the MIT License.
