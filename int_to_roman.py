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
        # Dictionary to map decimal numbers to their Roman numeral equivalents
        roman_dict = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }
        # Initialize an empty string to store the resulting Roman numeral
        roman_num = ''

        # Iterate through the list of decimal numbers in descending order
        # This ensures that we use the largest possible Roman numeral representation
        for i in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            # Repeat until the current decimal number is less than or equal to the input num
            while i <= num:
                # Append the corresponding Roman numeral to the result string
                roman_num += roman_dict[i]
                # Subtract the decimal number from the input num
                num -= i
        # Return the final Roman numeral representation
        return roman_num

# Test the function
solution_instance = Solution()
num = 54
ans = solution_instance.intToRoman(num)
print(f"Roman form of {num} is {ans}")
