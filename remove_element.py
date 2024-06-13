'''Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order 
of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you
need to do the following things:
1. Change the array nums such that the first k elements of nums contain the elements which are 
   not equal to val. The remaining elements of nums are not important as well as the size of nums.
2. Return k.'''


import array as arr

class Solution:
    def removeElement(self, nums, val):
        # Initialize a pointer j to keep track of the position where non-val elements will be placed
        j = 0
        
        # Iterate through each element in the array
        for i in range(len(nums)):
            # If the current element is not equal to the given value, update nums[j] to this element
            if nums[i] != val:
                nums[j] = nums[i]
                # Move the pointer j to the next position
                j += 1
        
        # j represents the new length of the array with val removed
        return j

# Create an instance of the Solution class
solution_instance = Solution()

# Example input array and value to remove
nums = [1, 2, 3, 2, 4]
val = 2

# Call the removeElement method to remove val from nums and get the new length of the array
ans = solution_instance.removeElement(nums, val)

# Print the new length of the array after removal
print(ans)
