'''Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.'''

class Solution:
    def lastWord(self, str1):
        # Remove leading and trailing whitespaces, then split the string into words
        s = str1.strip().split()
        # Return the length of the last word in the string
        return len(s[-1])

# Create an instance of the Solution class
solution_instance = Solution()

# Example input string
str1 = "Hello world!"

# Call the lastWord method to find the length of the last word in the string
ans = solution_instance.lastWord(str1)

# Print the length of the last word
print(ans)
