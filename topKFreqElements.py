class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_count_map = {}
        results = []
        
        for num in nums:
            if num in nums_count_map:
                nums_count_map[num] += 1
            else:
                nums_count_map[num] = 1
        
        for i in range(k):
            max_key_value = max(nums_count_map, key=nums_count_map.get)
            results.append(max_key_value)
            nums_count_map[max_key_value] = 0
        
        return results