# Given an integer n, return true if n is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, num: int) -> bool:
        # Check if the number is negative or ends with a zero (except for zero itself)
        if num < 0 or (num != 0 and num % 10 == 0):
            return False  # If either condition is met, the number is not a palindrome

        rev_num = 0  # Initialize a variable to store the reverse of the number

        # Reverse the second half of the number
        while num > rev_num:
            rev_num = rev_num * 10 + num % 10  # Add the last digit of 'num' to 'rev_num'
            num //= 10  # Remove the last digit from 'num'

        # Check if 'num' is equal to 'rev_num' (for even number of digits)
        # or 'num' is equal to 'rev_num // 10' (for odd number of digits)
        return num == rev_num or num == rev_num // 10

# Create an instance of the Solution class
solution_instance = Solution()

num = 1001  # Define the number to check for palindrome property

# Call the isPalindrome method with the input number
res = solution_instance.isPalindrome(num)

if res == True:  # Check if the result from isPalindrome is True
    print("{} is a palindrome number".format(num))  # Print message if the number is a palindrome
else:
    print("{} is not a palindrome number".format(num))  # Print message if the number is not a palindrome
