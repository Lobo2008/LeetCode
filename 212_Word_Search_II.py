"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input: 
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

Output: ["eat","oath"]

Note:
You may assume that all inputs are consist of lowercase letters a-z.

"""

class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        """
        第一代的变体，遍历每个word，把符合要求的word存下即可

        to be continue: 
         still TLE, pls ref this https://leetcode.com/problems/word-search-ii/discuss/59864/Python-code-use-trie-and-dfs-380ms


        """
        rs = []
        words = list(set(words))
        for word in words:
            if self.wordSearch(board, word):
                rs.append(word)
        return rs
    """
    查找board中是否存在word  ，也就是lc79的源代码
    """
    def wordSearch(self, board, word):
        if len(word) == 0:  return True
        if len(board) == 0 or len(board[0]) == 0:   return False
        if not self._hasEnoughChar(board, word):   return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(i,j, board, word):
                    return True
    """
    dfs搜索
    """
    def dfs(self, i, j, board, word):
        if len(word) == 0:  return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
            return False
        visited = board[i][j]
        board[i][j] = ' '
        # rs =(self.dfs(i-1,j,board,word[1:]) or \
        #          self.dfs(i+1,j,board,word[1:]) or \
        #          self.dfs(i,j-1,board,word[1:]) or\
        #          self.dfs(i,j+1,board,word[1:]))
        # board[i][j] = visited
        # return rs

        if self.dfs(i-1,j,board,word[1:]):
            board[i][j] = visited
            return True
        if self.dfs(i+1,j,board,word[1:]):
            board[i][j] = visited
            return True
        if self.dfs(i,j-1,board,word[1:]):
            board[i][j] = visited
            return True
        if self.dfs(i,j+1,board,word[1:]):
            board[i][j] = visited
            return True
        return False
    """
    判断word里的元素的个数是否少于board里面的对应元素的个数，对提升速度有很大的影响
    """
    def _hasEnoughChar(self, board, word):
        from collections import Counter
        c_w = Counter(word)
        c_board = Counter([c for row in board for c in row])
        for k,v in c_w.items():
            if c_board[k] < v:
                return False
        return True

so = Solution()

board =\
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

print(so.findWords(board,words))
