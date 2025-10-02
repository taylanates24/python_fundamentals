"""
Problem 1: Count Down
Write a function `count_down(n)` that:

Takes an integer `n`.
Prints numbers from `n` down to 1.

Hint: You can use a `while` loop that continues as long as `n` is greater than 0.

Example:
Input: 5
Output:
5
4
3
2
1
"""
def count_down(n):
    pass

"""
Problem 2: Even or Odd
Write a function `is_even_or_odd(n)` that:

Takes an integer `n`.
Returns the string "Even" if the number is even, and "Odd" if the number is odd.

Hint: Think about how the modulo operator (%) can help you determine if a number is even or odd. This is a classic use of an if-else statement.

Example:
Input: 4
Output: "Even"
"""
def is_even_or_odd(n):
    pass

"""
Problem 3: Print Even Numbers
Write a function `print_even_numbers(n)` that:

Takes an integer `n`.
Prints all even numbers from 1 to `n`.

Hint: You can combine the ideas from the first two problems. A loop can iterate from 1 to `n`, and a conditional statement can check if each number is even before printing.

Example:
Input: 10
Output:
2
4
6
8
10
"""
def print_even_numbers(n):
    pass

"""
Problem 4: Generate a List of Numbers
Write a function `generate_list_of_numbers(n)` that:

Takes an integer `n`.
Returns a list of numbers from 1 up to `n`.

Hint: Create an empty list. Then, use a loop to count from 1 to `n`, adding each number to your list.

Example:
Input: 5
Output: [1, 2, 3, 4, 5]
"""
def generate_list_of_numbers(n):
    pass

"""
Problem 5: Count Specific Element
Write a function `count_elements_in_list(items, element_to_count)` that:

Takes a list of items and a single element to count.
Returns the number of times `element_to_count` appears in the list.

Hint: Start with a counter at zero. Loop through the list, and every time you see the element you're looking for, increment the counter.

Example:
Input: (['a', 'b', 'c', 'a', 'd', 'a'], 'a')
Output: 3
"""
def count_elements_in_list(items, element_to_count):
    pass

"""
Problem 6: Filter Positive Numbers
Write a function `filter_positive(numbers)` that:

Takes a list of numbers.
Returns a new list containing only the positive numbers.

Hint: Create an empty list. Loop through the input list, and if a number is positive, append it to your new list.

Example:
Input: [-2, -1, 0, 1, 2]
Output: [1, 2]
"""
def filter_positive(numbers):
    pass

"""
Problem 7: Multiply List Elements
Write a function `multiply_elements(numbers, multiplier)` that:

Takes a list of numbers and a multiplier.
Returns a new list where each number from the original list is multiplied by the multiplier.

Hint: Create a new empty list. Loop through the `numbers` list, and for each number, multiply it by the `multiplier` and append the result to your new list.

Example:
Input: ([1, 2, 3], 5)
Output: [5, 10, 15]
"""
def multiply_elements(numbers, multiplier):
    pass

"""
Problem 8: Count Vowels
Write a function `count_vowels(s)` that:

Takes a string `s`.
Returns the number of vowels (a, e, i, o, u) in the string.

Hint: Loop through each character of the string and use a conditional to check if it's a vowel.

Example:
Input: "hello"
Output: 2
"""
def count_vowels(s):
    pass

"""
Problem 9: Reverse a List
Write a function `reverse_list(items)` that:

Takes a list.
Returns a new list with the elements in reverse order.

Hint: You can loop through the original list and insert each element at the beginning of the new list.

Example:
Input: [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
"""
def reverse_list(items):
    pass

"""
Problem 10: Find the Second Largest Number
Write a function `find_second_largest(numbers)` that:

Takes a list of numbers. Assumes the list has at least two numbers.
Returns the second largest number in the list.

Hint: You'll need to keep track of two values: the largest number found so far and the second largest. Initialize both variables after looking at the first two elements, then loop through the rest of the list and update them as needed.

Example:
Input: [1, 5, 3, 9, 2]
Output: 5
"""
def find_second_largest(numbers):
    pass

"""
Problem 11: Remove Duplicates from a List
Write a function `remove_duplicates(items)` that:

Takes a list.
Returns a new list with all duplicate elements removed, while preserving the original order of the first occurrence of each element.

Hint: Create a new empty list. Iterate through the original list, and for each element, add it to your new list only if it's not already in there.

Example:
Input: [1, 2, 2, 3, 4, 3, 5]
Output: [1, 2, 3, 4, 5]
"""
def remove_duplicates(items):
    pass

"""
Problem 12: Find the Longest String
Write a function `find_longest_string(strings)` that:

Takes a list of strings.
Returns the longest string from the list. If there are multiple strings with the same maximum length, return the first one that appears.

Hint: Keep track of the longest string you've found so far. Loop through the list, and if you find a string that is longer than your current longest, update your record.

Example:
Input: ["apple", "banana", "cherry", "date"]
Output: "banana"
"""
def find_longest_string(strings):
    pass

"""
Problem 13: Check for Prime Number
Write a function `is_prime(n)` that:

Takes an integer `n`.
Returns `True` if `n` is a prime number, and `False` otherwise. A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

Hint: Loop from 2 up to `n-1`. If `n` is divisible by any of those numbers, it's not prime. Don't forget to handle the cases where `n` is less than 2.

Example:
Input: 7
Output: True
"""
def is_prime(n):
    pass

"""
Problem 14: Matrix Addition
Write a function `add_matrices(matrix1, matrix2)` that:

Takes two matrices (represented as lists of lists) of the same dimensions.
Returns a new matrix which is the sum of the two.

Hint: You'll need to use nested loops to iterate through the rows and columns of the matrices. Create a new matrix of the same size, filled with zeros, to store your results.

Example:
Input: ([[1, 2], [3, 4]], [[5, 6], [7, 8]])
Output: [[6, 8], [10, 12]]
"""
def add_matrices(matrix1, matrix2):
    pass

"""
Problem 15: Caesar Cipher
Write a function `caesar_cipher(text, shift)` that:

Takes a string `text` and an integer `shift`.
Returns a new string where each letter in the `text` is shifted by `shift` positions in the alphabet. The shift should wrap around the alphabet (e.g., 'z' shifted by 2 becomes 'b'). Non-alphabetic characters should be left unchanged.

Hint: You can use `ord()` to get the ASCII value of a character and `chr()` to convert it back. You'll need to handle uppercase and lowercase letters separately and perform the wrap-around logic.

Example:
Input: ("Hello, World!", 3)
Output: "Khoor, Zruog!"
"""
def caesar_cipher(text, shift):
    pass 