"""
Diamond Pattern
Instructions
Problem Description:

You are given an integer n. Your task is to return a diamond pattern of '*' with n rows for the upper part (the widest row will have 2n - 1 stars), and the lower part is the mirrored version of the upper part. Each row should be centered with appropriate spaces.



Input:

A single integer n, where 1 <= n <= 100.



Output:

A list of strings where each string represents a row in the diamond pattern.



Example:

Input: 3
Output: ['  *  ', ' *** ', '*****', ' *** ', '  *  ']

Input: 5
Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********', ' ******* ', '  *****  ', '   ***   ', '    *    ']

"""

def diamond_pattern(n):
    lst = []
    for i in range(n):
         lst.append(' '*(2-i)+'*'*(2*i+1)+' '*(2-i))
            
    for i in range(i,0,-1):
        lst.append(' '*(n-i)+'*'*(2*i-1)+' '*(n-i))
    return lst

print(diamond_pattern(5))