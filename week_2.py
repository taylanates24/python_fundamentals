"""
Problem 1: Check if a List is Empty
Write a function is_list_empty(items) that:

Takes a list.
Returns True if the list is empty, and False otherwise.

Example:
Input: []
Output: True
"""
def is_list_empty(items):
    pass

"""
Problem 2: Get the First Element
Write a function get_first_element(items) that:

Takes a list.
Returns the first element of the list.
If the list is empty, return None.

Example:
Input: [1, 2, 3]
Output: 1
"""
def get_first_element(items):
    pass

"""
Problem 3: Get the Last Element
Write a function get_last_element(items) that:

Takes a list.
Returns the last element of the list.
If the list is empty, return None.

Example:
Input: ['a', 'b', 'c']
Output: 'c'
"""
def get_last_element(items):
    pass

"""
Problem 4: Sum of Elements
Write a function sum_list(numbers) that:

Takes a list of integers.
Returns the sum of all the numbers in the list.

Example:
Input: [1, 2, 3, 4, 5]
Output: 15
"""
def sum_list(numbers):
    pass

"""
Problem 5: Find Maximum Value
Write a function find_max(numbers) that:

Takes a list of integers.
Returns the largest number in the list.

Example:
Input: [1, 9, 3, 5, 7]
Output: 9
"""
def find_max(numbers):
    pass

"""
Problem 6: Append an Element to a List
Write a function append_element(items, element) that:

Takes a list and an element.
Appends the element to the end of the list.
Returns the modified list.

Example:
Input: ([1, 2, 3], 4)
Output: [1, 2, 3, 4]
"""
def append_element(items, element):
    pass

"""
Problem 7: Slice a List
Write a function slice_list(items, start, end) that:

Takes a list and two integers, start, and end.
Returns a new list containing the elements from the start index up to (but not including) the end index.

Example:
Input: ([1, 2, 3, 4, 5, 6], 2, 5)
Output: [3, 4, 5]
"""
def slice_list(items, start, end):
    pass

"""
Problem 8: Count Occurrences
Write a function count_occurrences(items, element) that:

Takes a list and an element.
Returns the number of times the element appears in the list.

Example:
Input: ([1, 2, 2, 3, 2, 4], 2)
Output: 3
"""
def count_occurrences(items, element):
    pass

"""
Problem 9: Find Index of Element
Write a function find_index(items, element) that:

Takes a list and an element.
Returns the index of the first occurrence of the element in the list.
If the element is not in the list, return -1.

Example:
Input: (['a', 'b', 'c', 'd'], 'c')
Output: 2
"""
def find_index(items, element):
    pass

"""
Problem 10: List Length
Write a function list_length(items) that:

Takes a list.
Returns the number of elements in the list without using the len() function.

Example:
Input: [1, 2, 3, 4, 5]
Output: 5
"""
def list_length(items):
    pass

"""
Problem 11: Filter Even Numbers
Write a function filter_even(numbers) that:

Takes a list of integers.
Returns a new list containing only the even numbers from the original list.

Example:
Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: [2, 4, 6, 8, 10]
"""
def filter_even(numbers):
    pass

"""
Problem 12: Create a List of Squares
Write a function list_of_squares(n) that:

Takes an integer n.
Returns a list of the squares of numbers from 1 to n.

Example:
Input: 5
Output: [1, 4, 9, 16, 25]
"""
def list_of_squares(n):
    pass

"""
Problem 13: Get Every Nth Element
Write a function get_every_nth(items, n) that:

Takes a list and an integer n.
Returns a new list containing every nth element from the original list.

Example:
Input: ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
Output: [3, 6, 9]
"""
def get_every_nth(items, n):
    pass

"""
Problem 14: Find the Difference Between Two Lists
Write a function difference(list1, list2) that:

Takes two lists.
Returns a new list containing elements that are in list1 but not in list2.

Example:
Input: ([1, 2, 3, 4, 5], [4, 5, 6])
Output: [1, 2, 3]
"""
def difference(list1, list2):
    pass

"""
Problem 15: Check for Subset
Write a function is_subset(list1, list2) that:

Takes two lists.
Returns True if list2 is a subset of list1, and False otherwise.

Hint: You can iterate through each element of list2 and check if that element is present in list1. If you find an element in list2 that is not in list1, you can return False immediately. If you go through all the elements of list2 and find them all in list1, then list2 is a subset.

Example:
Input: ([1, 2, 3, 4, 5], [2, 4])
Output: True
"""
def is_subset(list1, list2):
    pass

"""
Problem 16: Remove Duplicates
Write a function remove_duplicates(items) that:

Takes a list.
Returns a new list with duplicate elements removed. The order of the remaining elements should be preserved.

Example:
Input: [1, 2, 2, 3, 4, 4, 5]
Output: [1, 2, 3, 4, 5]
"""
def remove_duplicates(items):
    pass

"""
Problem 17: Common Elements
Write a function common_elements(list1, list2) that:

Takes two lists.
Returns a new list containing elements that are present in both lists.

Hint: You can iterate through one list and check if each element exists in the second list. (ie. element in list)


Example:
Input: ([1, 2, 3, 4, 5], [4, 5, 6, 7, 8])
Output: [4, 5]
"""
def common_elements(list1, list2):
    pass

"""
Problem 18: Find the Intersection of Two Lists
Write a function intersection(list1, list2) that:

Takes two lists.
Returns a new list containing elements that are common to both lists. Each element should appear only once.

Example:
Input: ([1, 2, 3, 4], [3, 4, 5, 6])
Output: [3, 4]
"""
def intersection(list1, list2):
    pass

"""
Problem 19: Flatten a Nested List
Write a function flatten_list(nested_list) that:

Takes a list of lists (a nested list).
Returns a single list containing all the elements from the nested list.

Hint: You can use nested loops. The outer loop iterates through the list of lists, and the inner loop iterates through each sublist.

Example:
Input: [[1, 2, 3], [4, 5], [6]]
Output: [1, 2, 3, 4, 5, 6]
"""
def flatten_list(nested_list):
    pass

"""
Problem 20: Merge Two Sorted Lists
Write a function merge_sorted_lists(list1, list2) that:

Takes two lists of integers, each sorted in ascending order.
Returns a new sorted list containing all elements from both lists.

Example:
Input: ([1, 3, 5], [2, 4, 6])
Output: [1, 2, 3, 4, 5, 6]
"""
def merge_sorted_lists(list1, list2):
    pass
