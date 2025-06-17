class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict()
        output = []

        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1 
            
        top_items = sorted(d.items(), key=lambda item: item[1], reverse=True)[:k]
        
        for key, value in top_items:
            output.append(key)

        return output
            