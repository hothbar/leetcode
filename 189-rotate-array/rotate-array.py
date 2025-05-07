class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # pop from the list
        # insert at pos 0

        #for _ in range(k):
            #nums.insert(0, nums.pop())
            #if k <= len(nums) else nums[::-1]
        k = k%len(nums)
        lst = nums[len(nums) - k :] + nums[:len(nums) - k] 
        for i in range(len(lst)):
            nums[i] = lst[i]


        
        
        