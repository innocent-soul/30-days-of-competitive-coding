# availiable on leetcode.com

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0 
        
        nums = set(nums)
        
        longest = 0
        
        for n in nums:
            if not (n - 1 in nums):  # ensures linear complexity
                sequence_length = 1
                while n + 1 in nums:
                    sequence_length += 1
                    n += 1
                
                longest = max(longest, sequence_length) 
            
        return longest
