#Input: nums = [1,2,3,1]

#Output: true

#Explanation: The element 1 occurs at the indices 0 and 3.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False