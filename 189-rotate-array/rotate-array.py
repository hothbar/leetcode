class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # pop from the list
        # insert at pos 0

        for _ in range(k):
            num = nums.pop()
            nums.insert(0, num)
        
        