class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        total_set = set()
        n =len(nums)
        max_length = 0
        for k in range(n):
            res_set = set() 
            while nums[k] not in total_set :
                total_set.add(nums[k])
                res_set.add(nums[k])
                k = nums[k]
                
            max_length = max(len(res_set), max_length)
            #res_set = set()
    
        return max_length