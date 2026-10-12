# Interactive Personal Data Collector

## About the Project
The **Interactive Personal Data Collector** is a beginner-friendly Python program that asks the user to enter a few personal details and displays each value along with its Python data type and memory address.

## Features
- Collects the user's name, age, height, and favourite number.
- Converts age and favourite number to integers.
- Converts height to a floating-point number.
- Calculates an estimated birth year using `2026 - age`.
- Displays each input value, its data type, and its memory address.
- Prints a thank-you message when the program finishes.

## Requirements
- Python 3.x
- A terminal or code editor that can run Python files

## How to Run
1. Save the program as `pr1.py`.
2. Open a terminal in the folder containing the file.
3. Run:

   ```bash
   python pr1.py
   ```

   On some systems, use `python3 pr1.py`.

4. Enter your name, age, height, and favourite number when prompted.

## Example
```text
Welcome to the interactive personal data collector!!!!!!
Enter your name: Krish
Enter your age: 19
Enter your height: 5.8
Enter your favourite number: 7
Name: Krish
Type: <class 'str'>
Memory address: ...
Age: 19
Type: <class 'int'>
Memory address: ...
Height: 5.8
Type: <class 'float'>
Memory address: ...
Favourite number: 7
Type: <class 'int'>
Memory address: ...
Birth year: 2007
Thank you for using this program!!
```

*Note: Memory addresses vary between program runs and Python implementations. The birth-year calculation uses the fixed year 2026, so the result is an estimate based only on the age entered.*

## Concepts Used
- `input()` for user input
- `int()` and `float()` for type conversion
- Variables and arithmetic
- `type()` to inspect data types
- `id()` to display an object's identity
- `print()` to display output

## Author
Add your name here.
