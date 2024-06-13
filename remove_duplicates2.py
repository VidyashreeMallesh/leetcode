'''Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique
element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed 
in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the 
first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory'''


import array as arr

class Solution:
    def removeDuplicates(self, nums):
        # Initialize a pointer j to keep track of the position where unique elements will be placed
        j = 1
        # Initialize a count variable to keep track of the number of occurrences of the current element
        count = 1

        # Iterate through each element in the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is equal to the previous one
            if nums[i] == nums[i-1]:
                # Increment the count of occurrences
                count += 1
            else:
                # Reset the count since the current element is different from the previous one
                count = 1

            # If the count of occurrences is less than or equal to 2, keep the current element
            if count <= 2:
                # Place the current element at position j
                nums[j] = nums[i]
                # Move the pointer j to the next position
                j += 1
                
        # j represents the new length of the array with at most two duplicates allowed for each element
        return j

# Create an instance of the Solution class
solution_instance = Solution()

# Example input array with duplicates
nums = arr.array('i',[1,1,1,2,2,3,3,3])

# Call the removeDuplicates method to remove duplicates from nums and get the new length of the array
ans = solution_instance.removeDuplicates(nums)

# Print the new length of the array after removing duplicates
print(ans)
