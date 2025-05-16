"""Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2]."""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        lst = []
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1 ,right+1]
                break
            elif numbers[left]+numbers[right] < target:
                left+=1
            else:
                right-=1