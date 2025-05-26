# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        def find_first(nums, target):
            left = 0
            right = n - 1
            result = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    result = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left += 1
                else:
                    right -= 1
            return result
        
        def find_last(nums, target):
            left = 0
            right = n - 1
            result = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    result = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left += 1
                else:
                    right -= 1
            return result
        return [find_first(nums, target), find_last(nums, target)]