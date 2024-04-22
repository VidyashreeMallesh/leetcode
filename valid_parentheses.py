'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.'''


class Solution(object):
    def isValid(self, s):
        # Initialize an empty stack to store opening brackets
        stack = [] # only use append and pop
        
        # Dictionary defining the pairs of opening and closing brackets
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        # Iterate through each bracket in the input string
        for bracket in s:
            # If the current bracket is an opening bracket, push it onto the stack
            if bracket in pairs:
                stack.append(bracket)
            # If the current bracket is a closing bracket
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                # If the stack is empty or the current bracket does not match the last opening bracket
                # Return False, as the sequence of brackets is invalid
                return False
        
        # After iterating through all brackets, if the stack is empty, return True
        # Otherwise, return False
        if len(stack) == 0:
            return True
        else:
            return False


# Example usage:
# Create an instance of the Solution class
solution_instance = Solution()

# Test the function with a string containing brackets
brackets = "()[]{}"
print(solution_instance.isValid(brackets))  # Output: True

# Test the function with another string containing brackets
brackets = "([)]"
print(solution_instance.isValid(brackets))  # Output: False
