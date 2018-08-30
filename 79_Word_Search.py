"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

"""
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        """
        应该用回溯法

        遍历每一行，当找到第一个跟word里的第一个字母相同的数字的时候，遍历其上下左右
        ref:    https://leetcode.com/problems/word-search/discuss/27665/Python-simple-dfs-solution
        """


        if len(word) == 0:  return True
        if len(board) == 0 or len(board[0]) == 0: return False
        #加了这句话，速度有本质的提升，因为如果word中出现的字符在board中不够的话，可以直接省略这个testcase
        if not self._hasEnoughChar(board, word):    return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(i,j,board,word):
                    return True
        return False
        
    def dfs(self,i,j,board,word):
            if len(word) == 0: return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
                return False
            #能到这里说明board[i][j]==word[0] 
            visited = board[i][j]
            board[i][j]=' '
            #这么多dfs中，只要有一个是true，说明能找到路径，继续下去就可以
            rs =(self.dfs(i-1,j,board,word[1:]) or \
                 self.dfs(i+1,j,board,word[1:]) or \
                 self.dfs(i,j-1,board,word[1:]) or\
                 self.dfs(i,j+1,board,word[1:]))
            board[i][j] = visited
            return rs
    def _hasEnoughChar(self, board, word):
        from collections import Counter
        c_w = Counter(word) #SEE  ->  Counter({'E': 2, 'S': 1})
        c_board = Counter([c for row in board for c in row])#Counter({'E': 3, 'A': 2, 'C': 2, 'S': 2, 'B': 1, 'F': 1, 'D': 1})
        for w,c in c_w.items():
            if c_board[w]<c:
                return False
        return True
        
so = Solution()

board =\
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
board=[['A']]
word = "ABCCED"
word = "ABCB"

"""
board只有一行、只有一列的情况
只有一个元素的情况
空的情况
"""

print(board)
print(so.exist(board, word))