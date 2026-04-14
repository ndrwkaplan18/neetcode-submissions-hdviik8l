class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.isValid(row):
                return False


        j = 0
        while j < 9:
            column = []
            i = 0
            while i < 9:
                column.append(board[i][j])
                i += 1
            if not self.isValid(column):
                return False
            j += 1

        i = 0

        while i < 9:
            j = 0
            while j < 9:
                box = []
                k = i

                while k < i+3:
                    l = j
                    while l < j+3:
                        box.append(board[k][l])
                        l += 1
                    k += 1
                if not self.isValid(box):
                    return False
                j += 3
            i += 3

        return True

    def isValid(self, row: List[str]) -> bool:
        seen = set()
        for num in row:
            if num != '.' and num in seen:
                return False
            seen.add(num)
        return True