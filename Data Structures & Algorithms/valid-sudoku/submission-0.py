class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rs = defaultdict(set)
        cl = defaultdict(set)
        ms = defaultdict(set)

        for row in range(9):
            for col in range(9):
                current = board[row][col]
                if current == ".":
                    continue

                if (current in rs[row] 
                or current in cl[col]
                or current in ms[row // 3, col //3]):
                    return False

                rs[row].add(current)
                cl[col].add(current)
                ms[row // 3, col // 3].add(current)

        return True



