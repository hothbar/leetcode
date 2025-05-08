class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        total_set = set()
        
        max_length = 0
        for i in range(len(nums)):
            res_set = set()
            k = i 
            while nums[k] not in total_set :
                total_set.add(nums[k])
                res_set.add(nums[k])
                k = nums[k]
                
            max_length = max(len(res_set), max_length)
            #res_set = set()
    
        return max_length