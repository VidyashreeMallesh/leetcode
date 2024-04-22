'''Given a list of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
Each input has exactly one solution, that is same element should not be used twice.'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create an empty dictionary to store the numbers and their indices
        num_dict = {}  # Use a dictionary to store the numbers and their indices

        # Loop through the numbers and their indices using enumerate
        for i, n in enumerate(nums):
            # Calculate the difference needed to reach the target
            difference = target - n
            # Check if the difference is already in the dictionary
            if difference in num_dict:
                # If found, return the indices of the two numbers that add up to the target
                return [num_dict[difference], i]
            # Store the current number and its index in the dictionary
            num_dict[n] = i

        # If no solution is found, return an empty list
        return []

# Create an instance of the Solution class
solution_instance = Solution()

# Example usage: 
# Define a list of numbers and a target value
nums = [4, 21, 10, 17]
target = 14
# Call the twoSum method with the list of numbers and target value
result = solution_instance.twoSum(nums, target)
# Print the indices of the two numbers that add up to the target
print("Indices of the two numbers:", result)
