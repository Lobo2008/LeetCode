"""
 There are N students in a class. Some of them are friends, while some are not. 
 Their friendship is transitive in nature. 
 For example, 
 if A is a direct friend of B, and B is a direct friend of C, 
 then A is an indirect friend of C. And we defined a friend circle is a group of students 
 who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between
students in the class. If M[i][j] = 1, then the ith and jth students are direct 
friends with each other, otherwise not. 
And you have to output the total number of friend circles among all the students.

Example 1:

Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.

Example 2:

Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

Note:

    N is in range [1,200].
    M[i][i] = 1 for all students.
    If M[i][j] = 1, then M[j][i] = 1.
"""



# class UF(object):
#     def __init__(self, matrix):
#         self.n = len(matrix)
#         self.parent = [-1]*self.n #[-1,-1,-1]
#         for i in range(self.n):
#             self.parent[i] = i #[0,1,2]
#     def find(self, node):
#         if self.parent[node] == node:   return node # or parent[node] is also ok
#         self.parent[node] = self.find(self.parent[node])
#         return self.parent[node]

#     def union(self, x, y):
#         x_root = self.find(x)
#         y_root = self.find(y)
#         if x_root != y_root:
#             self.parent[x_root] = y_root
#     def get_rs(self):
#         return self.parent



class UF(object):
    def __init__(self, matrix):
        self.n = len(matrix)
        self.parent = [i for i in range(self.n)]
    def getRoot(self, node):
        if node == self.parent[node]:   return node
        self.parent[node] = self.getRoot(self.parent[node])
        return self.parent[node]
class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
      
        """
        if len(M) == 0 or len(M[0]) == 0:   return 0
        parent = [i for i in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[0])):
                if i != j and M[i][j] == 1:
                    root_i = self.getRoot(parent, i)
                    root_j = self.getRoot(parent, j)
                    if root_i != root_j:
                        parent[root_i] = root_j
                     
        return len([i for k,v in enumerate(parent) if k==v] )


    def getRoot(self, parent, node):
        if node == parent[node]:    return node
        parent[node] = self.getRoot(parent, parent[node])
        return parent[node]

















        # uf = UF(M)  
        # for i in range(len(M)):
        #     for j in range(len(M)):
        #         if i != j and M[i][j] == 1:
        #             uf.union(i,j)
        # rs = uf.get_rs()
        # return rs
        # return len([i for k,v in enumerate(rs) if k==v ])





so = Solution()
M = [[1,1,0],[1,1,0],[0,0,1]] # 2
# M = [[1,1,0],[1,1,1],[0,1,1]] # 1
print(so.findCircleNum(M))