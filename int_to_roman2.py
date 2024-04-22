'''Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, 
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle 
applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.'''


class Solution:
    def intToRoman(self, num: int) -> str:
        # List of Roman numeral representations and their corresponding decimal values
        romanList = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], 
                     ["XC", 90], ["C", 100],["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]] 
        
        # Initialize an empty string to store the resulting Roman numeral
        roman_num = ''
        
        # Loop through romanList in reverse order to start with the largest Roman numerals
        for roman, val in  reversed(romanList):
            # Check if the current Roman numeral is needed in the representation of num
            if num // val > 0:
                # Calculate how many times the current Roman numeral should be repeated
                count = num // val
                # Append the Roman numeral to the result string count times
                roman_num += (roman * count)
                # Update num to the remainder after subtracting the value of the Roman numeral
                num = num % val 
        
        # Return the final Roman numeral representation
        return roman_num

# Test the function
solution_instance = Solution()
num = 32
res = solution_instance.intToRoman(num)
print(f"Roman form of {num} is {res}")
