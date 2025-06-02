"""
Square of side 'N'
Instructions
Problem Description: You are given an integer n. Your task is to return a square pattern of size n x n made up of the character '*', represented as a list of strings.



Input Parameters:

n (int): The size of the square (number of rows and columns).



Output:

A list of strings where each string is a row of n characters.



Example:

Input: 3
Output: 
['***', '***', '***']
"""

def square_of_side_n(n):
    lst = []
    for i in range(n):
        lst.append('*'*n)
    return lst

print(square_of_side_n(6))
