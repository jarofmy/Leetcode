class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        
        for idx, value in enumerate(nums):
            diff = target - value
            if diff in seen:
                return [seen[diff], idx]
            
            seen[value] = idx