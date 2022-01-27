# https://leetcode.com/problems/reverse-integer/

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        
        negative_check = False
        num = x
        reverse_num = 0
        
        if x < 0:
            num *= -1
            negative_check = True
        
        
        while num:
            remainder = num % 10
            reverse_num = (reverse_num) * 10 + remainder
            
            num //=10
        
        
        if negative_check:
            reverse_num *= -1
        
        if reverse_num < (-1 * (2 ** 31)) or reverse_num > ((2 ** 31)-1):
            return 0
        
        else:
            return reverse_num
        