"""
Hollow Inverted Right Triangle
Instructions
Problem Description:

You are given an integer n. Your task is to return a hollow inverted right-angled triangle pattern of '*', where the first row contains n stars, while the inner rows contain a star at the beginning and end, with spaces in between. The triangle should be left-aligned.



Input:

A single integer n, where 1 <= n <= 100.



Output:

A list of strings where each string represents a row in the hollow inverted right-angled triangle.



Example:

Input: 4
Output: ['****', '* *', '**', '*']

Input: 5
Output: ['*****', '*  *', '* *', '**', '*']

"""

def hollow_inverted_triangle_n(n):
    lst = []
    for i in range(n,0,-1):
        if i == n:
            lst.append('*'*n)
        elif i >= int(n/2) and i != n:
            lst.append('*'+' '*(i-2)+'*')
        else:
            lst.append('*'*i)
        
    return lst

print(hollow_inverted_triangle_n(5))