class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1 :
            return 0
        s = set(nums)
        longest = 0

        for num in s:
            if (num - 1) not in s:
                next_num = num + 1
                l = 1

                while next_num in s:
                    l += 1
                    next_num += 1
                    
                longest = max(longest, l)
        return longest