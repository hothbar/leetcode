class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = []
        r = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                r.append("".join(s))
                return
            
            if openN < n:
                s.append("(")
                backtrack(openN + 1, closedN)
                s.pop()
            
            if closedN < openN:
                s.append(")")
                backtrack(openN, closedN + 1)
                s.pop()

        backtrack(0, 0)
        return r        
        