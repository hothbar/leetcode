class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if board[r][c] == ".":
                    continue
                if val in rows[r] or val in cols[c] or val in squares[(r//3, c//3)]:
                    return False
                cols[c].add(val)
                rows[r].add(val)
                squares[(r//3, c//3)].add(val)
        return True
        