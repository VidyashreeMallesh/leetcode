'''Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.'''


class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary to map Roman numerals to their corresponding decimal values
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        # Initialize a variable to store the total decimal value of the Roman numeral
        total = 0
        
        # Iterate through each character in the input string except the last one
        for i in range(len(s) - 1):
            # If the value of the current Roman numeral is less than the value of the next one
            if roman_dict[s[i]] < roman_dict[s[i+1]]:
                # Subtract the value of the current Roman numeral from the total
                total -= roman_dict[s[i]]
            else:
                # Otherwise, add the value of the current Roman numeral to the total
                total += roman_dict[s[i]]
        
        # Add the value of the last Roman numeral to the total
        # The loop above didn't include the last character, so we add it here
        return total + roman_dict[s[-1]] 

# Create an instance of the Solution class
solution_instance = Solution()

# Test the function with a Roman numeral string
roman_num = "LXXII"
ans = solution_instance.romanToInt(roman_num)
print(f"Value of {roman_num} is {ans}")
