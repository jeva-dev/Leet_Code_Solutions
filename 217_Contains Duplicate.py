#Input: nums = [1,2,3,1]

#Output: true

#Explanation: The element 1 occurs at the indices 0 and 3.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False