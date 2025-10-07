class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # A dictionary to store numbers and their indices
        seen = {}
        
        # Iterate through the list with both index and value
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if the complement exists in the dictionary
            if complement in seen:
                # If found, return the current index and the complement's index
                return [seen[complement], i]
            
            # If not found, add the current number and its index to the dictionary
            seen[num] = i
        
        # The problem statement guarantees a solution, so this part is technically unreachable
        # but is good practice for robustness.
        return []

