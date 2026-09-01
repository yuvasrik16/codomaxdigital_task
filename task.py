"""
Task.py
Module 1 - Introduction to AI & Python
All tasks combined into a single file for easy execution in VS Code.

Run with:
    python Task.py
"""

import sys


# =====================================================
# TASK 1: Basics - Variables and Data Types
# =====================================================
def task1_basics():
    print("=" * 50)
    print("TASK 1: BASICS - VARIABLES & DATA TYPES")
    print("=" * 50)

    print("Python version:", sys.version)
    print("-" * 40)

    name = "Aria"          # string
    age = 21                # integer
    height = 5.6             # float
    is_student = True        # boolean

    print(f"Name: {name} (type: {type(name).__name__})")
    print(f"Age: {age} (type: {type(age).__name__})")
    print(f"Height: {height} (type: {type(height).__name__})")
    print(f"Is student: {is_student} (type: {type(is_student).__name__})")

    total = age + 5
    print(f"\nIn 5 years, {name} will be {total} years old.\n")


# =====================================================
# TASK 2: Loops - For and While
# =====================================================
def task2_loops():
    print("=" * 50)
    print("TASK 2: LOOPS - FOR & WHILE")
    print("=" * 50)

    print("For loop - numbers 1 to 10:")
    for i in range(1, 11):
        print(i, end=" ")
    print("\n")

    print("Multiplication table of 5:")
    for i in range(1, 11):
        print(f"5 x {i} = {5 * i}")
    print()

    print("While loop - countdown:")
    count = 5
    while count > 0:
        print(count)
        count -= 1
    print("Liftoff!\n")


# =====================================================
# TASK 3: Functions
# =====================================================
def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def greet(name="friend"):
    """Return a greeting message."""
    return f"Hello, {name}! Welcome to Python."


def task3_functions():
    print("=" * 50)
    print("TASK 3: FUNCTIONS")
    print("=" * 50)

    print(add_numbers(4, 7))
    print(greet("Aria"))

    print("\nPrime numbers between 1 and 30:")
    for num in range(1, 31):
        if is_prime(num):
            print(num, end=" ")
    print("\n")


# =====================================================
# TASK 4: Lists
# =====================================================
def task4_lists():
    print("=" * 50)
    print("TASK 4: LISTS")
    print("=" * 50)

    fruits = ["apple", "banana", "cherry", "mango"]
    print("Original list:", fruits)

    print("\nLooping through fruits:")
    for fruit in fruits:
        print("-", fruit)

    fruits.append("orange")
    print("\nAfter adding 'orange':", fruits)

    fruits.remove("banana")
    print("After removing 'banana':", fruits)

    print("\nFirst fruit:", fruits[0])
    print("Last fruit:", fruits[-1])

    numbers = [12, 5, 9, 20, 3]
    print("\nNumbers:", numbers)
    print("Sum:", sum(numbers))
    print("Average:", sum(numbers) / len(numbers))
    print("Sorted:", sorted(numbers))
    print()


# =====================================================
# TASK 5: Mini Project - Simple Calculator
# =====================================================
def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


def task5_calculator():
    print("=" * 50)
    print("TASK 5: MINI PROJECT - SIMPLE CALCULATOR")
    print("=" * 50)
    print("Operations: +, -, *, /")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("Enter calculation (e.g., 5 + 3): ")

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        try:
            parts = user_input.split()
            if len(parts) != 3:
                print("Please use format: number operator number\n")
                continue

            num1, op, num2 = float(parts[0]), parts[1], float(parts[2])

            if op == "+":
                result = add_numbers(num1, num2)
            elif op == "-":
                result = subtract(num1, num2)
            elif op == "*":
                result = multiply(num1, num2)
            elif op == "/":
                result = divide(num1, num2)
            else:
                print("Unknown operator. Use +, -, *, /\n")
                continue

            print(f"Result: {result}\n")

        except ValueError:
            print("Invalid numbers. Try again.\n")


# =====================================================
# MAIN - Run all tasks in sequence
# =====================================================
if __name__ == "__main__":
    task1_basics()
    task2_loops()
    task3_functions()
    task4_lists()
    task5_calculator()   # interactive - runs last