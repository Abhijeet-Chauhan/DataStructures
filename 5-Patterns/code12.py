"""
Sandglass Pattern
Instructions
Problem Description:

You are given an integer n. Your task is to return a sandglass pattern of '*', where the first row contains 2n - 1 stars and each subsequent row decreases the number of stars by 2, until the last row contains a single star. After reaching the smallest width, the pattern then continues with the same number of stars increasing back to 2n - 1. The stars in each row should be centered.



Input:

A single integer n, where 1 <= n <= 100.



Output:

A list of strings where each string represents a row in the sandglass pattern.



Example:

Input: 3
Output: ['*****', ' *** ', '  *  ', ' *** ', '*****']

Input: 4
Output: ['*******', ' ***** ', '  ***  ', '   *   ', '  ***  ', ' ***** ', '*******']
"""

def sandglass_pattern(n):
    lst = []
    
    for i in range(n,0,-1):
        lst.append(' '*(n-i)+'*'*(2*i-1)+' '*(n-i))

    for i in range(1,n):
         lst.append(' '*(2-i)+'*'*(2*i+1)+' '*(2-i))
           
    return lst

print(sandglass_pattern(3))