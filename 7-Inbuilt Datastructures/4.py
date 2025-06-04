"""
Check if all elements in a list are Unique
Instructions
Check if All Elements in a List are Unique

You are given a list of integers. Write a Python program that checks if all elements in the list are unique. If all elements are unique, return True; otherwise, return False.

Parameters:

lst (List of integers): The list of integers to check for uniqueness.

Returns:

A boolean value True if all elements in the list are unique, False otherwise.

Example:

Input: lst = [1, 2, 3, 4, 5]
Output: True

Input: lst = [1, 2, 3, 3, 4, 5]
Output: False
"""

def unique_list(n):
    new_lst = []
    for i in n:
        if i not in new_lst:
            new_lst.append(i)
        else:
            pass

    if n == new_lst:
        return True
    else:
        return False
    

print(unique_list([1, 2, 3, 3, 4, 5]))