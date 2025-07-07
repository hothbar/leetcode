class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        n = len(numbers)

        for i in range(n):
            diff = target - numbers[i]

            if diff in d:
                return [d[diff]+1, i+1]
            d[numbers[i]] = i
        