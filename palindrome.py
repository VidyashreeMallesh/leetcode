# Given an integer n, return true if n is a palindrome, and false otherwise.

n = 343  # Define the number to check for palindrome property

def ispalindrome(n):
    num = str(n)  # Convert the number to a string
    rev = num[::-1]  # Reverse the string using slicing
    if rev == num:  # Check if the reversed string is equal to the original string
        return True  # Return True if the number is a palindrome
    else:
        return False  # Return False if the number is not a palindrome


ans = ispalindrome(n)  # Call the ispalindrome function with the input number
if ans == True:  # Check if the result from ispalindrome is True
    print("Entered number is palindrome")  # Print message if the number is a palindrome
else:
    print("Entered number is not palindrome")  # Print message if the number is not a palindrome
