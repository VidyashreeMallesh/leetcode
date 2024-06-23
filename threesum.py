'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Note: Solution set must not contain duplicate triplets.'''

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        # Sort the input list of numbers
        nums.sort() 
        
        # Initialize an empty list to store the unique triplets that sum to zero
        list1 = []
        
        # Iterate through the sorted list of numbers
        for i in range(len(nums)):  
            # Skip duplicate values to avoid duplicate triplets
            if i > 0 and nums[i-1] == nums[i]:  
                continue 
			
            # Initialize pointers j and k
            j = i + 1 
            k = len(nums) - 1 
            
            # Iterate until j is less than k
            while j < k: 
                # Calculate the sum of the current triplet
                sum = nums[i] + nums[j] + nums[k] 
                
                # If the sum is greater than 0, decrement k to reduce the sum
                if sum > 0: 
                    k -= 1  
                
                # If the sum is less than 0, increment j to increase the sum
                elif sum < 0: 
                    j += 1  
                
                # If the sum is zero, add the triplet to the result list
                else:
                    list1.append([nums[i], nums[j], nums[k]]) 
                    j += 1 
                    
                    # Skip duplicate values of j to avoid duplicate triplets
                    while nums[j-1] == nums[j] and j < k: 
                        j += 1   
        
        # Return the list of unique triplets that sum to zero
        return list1


# Create an instance of the Solution class
solution_instance = Solution()

# Test the function with an example list of numbers
nums = [-1,0,1,2,-1,-4]
ans = solution_instance.threeSum(nums)
print(ans)
