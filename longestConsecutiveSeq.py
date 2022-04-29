class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        max_seq = 0
        d = set(nums)
        
        for num in nums:
            if (num - 1) not in d:
                curr_seq = 0
                while num + curr_seq in d:
                    curr_seq += 1
                max_seq = max(max_seq, curr_seq)
        return max_seq