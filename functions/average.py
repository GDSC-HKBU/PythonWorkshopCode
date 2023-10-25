# average.py

"""
Description: Calculate the average of some numbers.

Difficulty: Easy

Task: Write a function that takes a list of three numbers as input and returns their average.

Input: A list of three numbers (integer or float).

Output: Float.

Return: The average of the input numbers.
"""

def average(numbers):
    sum = 0
    count = 0
    for n in numbers:
        sum += n
        count += 1

    return sum/count