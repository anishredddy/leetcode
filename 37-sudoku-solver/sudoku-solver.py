class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    for num in "123456789":
                        if self.is_valid(board,i,j,num):
                            board[i][j]=num
                            if self.solveSudoku(board):
                                return True
                            else:
                                board[i][j]="."
                    return False
        return True


    def is_valid(self,board,i,j,num):

        for x in range(9):
            if board[i][x]==num :
                return False
            if board[x][j]==num :
                return False 
            if board[3*(i//3)+x//3][3*(j//3)+x%3]==num:
                return False
        return True
        