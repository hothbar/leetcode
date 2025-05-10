class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #result = -1
        f = 0
        l = len(nums)-1
        #m = (f+l//2) # Maybe need to floor/int div this?
        #if m == target: # base case, maybe more base cases?
            #return nums.index(target)
        
        while f <= l:
            m = (f+l)//2
            
            if nums[m] == target:
                return m

            if nums[f] <= nums[m]:
                if nums[f] <= target and target <=  nums[m]:
                    l = m - 1
                else:
                    f = m+1
            else:
                if nums[m] <= target and target <= nums[l]:
                    f = m + 1
                else:
                    l = m -1

        return -1