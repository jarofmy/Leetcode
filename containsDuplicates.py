class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        if not nums:
            return False
        
        d = {}
        
        for num in nums:
            if num in d:
                return True
            else:
                d[num] = 1
        
        return False

        # alternate one-liner
        # return len(set(nums)) != len(nums)