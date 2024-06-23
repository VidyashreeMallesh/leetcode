'''Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Merge the two sorted arrays into a single sorted array
        nums3 = nums1 + nums2
        
        # Sort the merged array
        nums3.sort()
        
        # Calculate the size of the merged array
        size = len(nums3)

        # Check if the size of the merged array is odd or even
        if size % 2 == 1:
            # If the size is odd, return the middle element as the median
            return float(nums3[size // 2])
        else:
            # If the size is even, calculate the average of the two middle elements as the median
            mid1 = nums3[size // 2 - 1]
            mid2 = nums3[size // 2]
            return (float(mid1) + float(mid2)) / 2.0
        

# Create an instance of the Solution class
solution_instance = Solution()

# Example input arrays
nums1 = [2, 5, 7]
nums2 = [1, 6, 9]

# Find the median of the merged sorted arrays by calling the function
ans = solution_instance.findMedianSortedArrays(nums1, nums2)

# Print the result
print(f"Median is {ans}")
