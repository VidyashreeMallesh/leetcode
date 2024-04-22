'''Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
Each input has exactly one solution, that is same element should not be used twice.'''
import array as arr  # Import the array module and alias it as 'arr'

nums = arr.array('i', [5, 19, 3, 6])  # Define an array 'nums' with integer values
target = 11  # Define the target sum to find
found_match = False  # Flag to track if a match is found
leng = len(nums)  # Get the length of the 'nums' array
for i in range(0, leng - 1):  # Loop through indices of 'nums' array from 0 to length - 1
    for j in range(i + 1, leng):  # Nested loop to compare each pair of numbers
        if nums[i] + nums[j] == target:  # Check if the sum of the current pair equals the target
            print("Match found by adding index", i, "and", j)  # Print the indices of the matching pair
            found_match = True  # Set flag to True if match is found

if not found_match:  # Check if no match is found after iterating through all pairs
    print("Match not found")  # Print "Match not found" if no match is found
