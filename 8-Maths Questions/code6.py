"""
Binary to Decimal
Instructions
Problem Description:

You are given a string binary_str representing a binary number. Your task is to convert this binary string to its corresponding decimal integer. Do not use any built-in functions for conversion.



Input:

A string binary_str, consisting of characters '0' and '1', where the length of the string is between 1 and 30 (inclusive).



Output:

An integer representing the decimal value of the binary string



Example:

Input: binary_str = "101"
Output: 5

Input: binary_str = "1101"
Output: 13

"""

def binary_to_decimal(binary_str):
    """
    Function to convert a binary string to its decimal integer representation without using built-in functions.
    
    Parameters:
    binary_str (str): The binary string to convert.
    
    Returns:
    int: The decimal representation of the binary string.
    """
    decimal_value = 0
    length = len(binary_str)
    
    # Iterate over each character in the binary string
    for i in range(length):
        # Get the digit (either '0' or '1')
        digit = binary_str[length - 1 - i]  # Start from the end of the string
        
        # If the digit is '1', add the corresponding power of 2 to the decimal value
        if digit == '1':
            decimal_value += 2 ** i  # Add 2 raised to the current power

    return decimal_value