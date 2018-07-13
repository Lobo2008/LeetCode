"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'.
 Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
 Two cells are connected if they are adjacent cells connected horizontally or vertically.

"""

class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        """
        要被X包围的O才能换成X，所以
        边界O的不能换，
        与边界像连接的O也不能换
        比如
        xxxx
        xxoo
        xxxx
        这种，(1,3)的o不能换，与(1,3)连接的(1,2)也不能换

        那么，遍历边界就ojbk了，找到如果边界是o，换成其他的字符，比如D，然后再把这个o上下左右的o换成D。
        最后，剩下的O就是被X包围的O，换成X就可以，然后再把D换成原来的O

        也就是，只需要处理第1行、最后一行以及第一列和最后一列就可以


        注意，找到一个未被包围的O1时，替换为D，然后检查他的上下左右是否有O2，如果有的话，替换位D，然后还要再次检查O2的上下左右
        """
        def bfs(row, col):
            if board[row][col] != 'O':
                return
            board[row][col] = 'D'#替换
            #处理o上下左右的元素
            neighbor(row, col)

        def neighbor(row, col):
            #上：row-1,col
            #下：row+1,col
            #左：row,col-1
            #右：row,col+1
            if row-1 in range(len(board)) and board[row-1][col] == 'O':
                board[row-1][col] = 'D'
                neighbor(row-1, col)#递归检查
            if row+1 in range(len(board)) and board[row+1][col] == 'O':
                board[row+1][col] = 'D'
                neighbor(row+1, col)#递归检查
            if col-1 in range(len(board[0])) and board[row][col-1] == 'O':
                board[row][col-1] = 'D'
                neighbor(row, col-1)#递归检查
            if col+1 in range(len(board[0])) and board[row][col+1] == 'O':
                board[row][col+1] = 'D'
                neighbor(row, col+1)#递归检查
        row = len(board)
        if row == 0:
            return
        col = len(board[0])
        #遍历第一行和最后一行
        for i in range(col):
            # board[0][i] #第一行
            # board[row-1][i]#最后一行
            bfs(0, i)
            bfs(row-1, i)
            
        for j in range(row):
            # board[j][0]#第一列
            # board[j][col-1]#最后一列
            bfs(j, 0)
            bfs(j, col-1)
        #将剩余的O变为，将中介元素替换回O
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'D':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        return board


        

        
so = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","O","O","X"],["X","O","X","X"]]
board = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
"""
['X', 'O', 'X', 'O', 'X', 'O']
['O', 'X', 'O', 'X', 'O', 'X']
['X', 'O', 'X', 'O', 'X', 'O']
['O', 'X', 'O', 'X', 'O', 'X']
"""
res = so.solve(board)
# print(len(board))
# print(len(board[0]))
for i in range(len(res)):
    print(res[i])
    # for j in range(len(board[0])):
        # print(board[i][j])