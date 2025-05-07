class Solution:
    def maxScore(self, nums: List[int]) -> int:
        # sort the list in descending order
        # initialize the max to the be the first element
        # we keep on accumulating while comparing with the max
        # return the max
        nums.sort(reverse = True)
        score = 0 if nums[0] <= 0 else 1
        #print(score)
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            if nums[i] > 0:
                score = i+1
            else:
                break 
            #maximum = max(maximum, maximum + nums[i])
        
        return score




        