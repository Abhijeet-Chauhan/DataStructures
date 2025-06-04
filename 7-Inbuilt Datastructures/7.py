"""
Maximum difference between two consecutive elements in a list
Instructions
Find Maximum Difference Between Two Consecutive Elements (Brute Force Approach)

You are given a list of integers. Write a Python program to find the maximum difference between two consecutive elements in the list using a brute-force approach. The difference is defined as the absolute value of the difference between two consecutive elements.

Parameters:

lst (List of integers): A list of integers.

Returns:

An integer representing the maximum difference between two consecutive elements.

Example:

Input: lst = [1, 7, 3, 10, 5]
Output: 7

The maximum difference is between 3 and 10 (i.e., |3 - 10| = 7).

Input: lst = [10, 11, 15, 3]
Output: 12
"""

def max_consecutive_difference(lst):
    max_diff = 0  
    for i in range(len(lst) - 1):
        diff = abs(lst[i] - lst[i + 1])  
        if diff > max_diff:
            max_diff = diff
    return max_diff

# Example test cases
print(max_consecutive_difference([1, 7, 3, 10, 5]))  
print(max_consecutive_difference([10, 11, 15, 3]))  
