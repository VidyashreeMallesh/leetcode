'''Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each 
unique element appears only once. The relative order of the elements should be kept the same. Then return 
the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
1. Change the array nums such that the first k elements of nums contain the unique elements in the order they 
were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
2. Return k.'''


import array as arr

class Solution:
    def removeDuplicates(self, nums):
        # Initialize a pointer j to keep track of the position where unique elements will be placed
        j = 1
        
        # Iterate through each element in the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is different from the previous one
            if nums[i] != nums[i - 1]:
                # Place the current element at position j
                nums[j] = nums[i]
                # Move the pointer j to the next position
                j += 1
        
        # j represents the new length of the array with duplicates removed
        return j

# Create an instance of the Solution class
solution_instance = Solution()

# Example input array with duplicates
nums = arr.array('i',[1,1,2,3,3,3])

# Call the removeDuplicates method to remove duplicates from nums and get the new length of the array
res = solution_instance.removeDuplicates(nums)

# Print the new length of the array after removing duplicates
print(res)
