class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        sum = 0
        prev = s[0]

        for c in s:
            sum += d[c]

            if d[prev] < d[c]:
                sum -= (2*d[prev])

            prev = c

        return sum


        
        