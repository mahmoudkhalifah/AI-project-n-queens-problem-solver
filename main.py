class NQSolver:
    numberOfQueens = 0
    board = []

    # constructor to just initialize the matrix
    def __init__(self, numberOfQueens):
        if numberOfQueens > 3:
            self.numberOfQueens = numberOfQueens
            self.board = [[0 for i in range(numberOfQueens)] for j in range(numberOfQueens)]
            # col are inside, rows are outside
        else:
            print("this number of queens impossible to be solved! please enter number greater than 3 :)")

    def printBoard(self):
        for row in range(self.numberOfQueens):
            for col in range(self.numberOfQueens):
                if self.board[row][col] == 1:
                    print("Q", end="  ")
                else: print("-", end="  ")
            print()

    def isSafe(self,row,col):
        # check for previous columns in the same row
        for i in range(col):
            if self.board[row][i] == 1:
                return False
        # check for upper diagonal
        for i, j in zip(range(row,-1,-1), range(col,-1,-1)):
            if self.board[i][j] == 1:
                return False
        # check for lower diagonal
        for i, j in zip(range(row,self.numberOfQueens,+1), range(col,-1,-1)):
            if self.board[i][j] == 1:
                return False

        return True

    def solve(self,col):
        # base (end of columns)
        if col >= self.numberOfQueens:
            return True
        # looping in all rows in the same column
        for row in range(self.numberOfQueens):
            # check if is safe to place queen
            if self.isSafe(row, col):
                self.board[row][col] = 1
                # continue to place the next queens
                if self.solve(col+1):
                    return True
                # if solve is false so it doesn't solve the problem and we backtrack to the previous
                self.board[row][col] = 0
        # no solution at this time
        return False

    def solution(self):
        self.solve(0)
        self.printBoard()


solver = NQSolver(int(input("Enter number of queens \n")))
solver.solution()
