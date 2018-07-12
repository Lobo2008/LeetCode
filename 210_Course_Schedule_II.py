"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .

Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .

"""

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        """
        还是bfs，画出图就容易理解得多了，以第二个题目来画：[[1,0],[2,0],[3,1],[3,2]]
        3->1->0
         \>2/>     其中3->2 , 2->0

         所以正确的选课方案就是，
            最右边一层[0]
            然后中间的一层[1,2]
            最左边的一层[3]
        同一层的多个节点，在同一层中可以以任意顺序出现，所以，所有的情况就是:
        [0]->[1,2]->[3]
            第二次的[1.2]可互换，则有[0]->[2,1]->[3]共三种

        注意注意，只需要返回一个正确的结果即可，无需返回所有情况
        """
        from collections import defaultdict
        levels = defaultdict(lambda: [], {})
        out_degree = {i:0 for i in range(numCourses)}
        for course, pre in prerequisites:
            out_degree[course] += 1
            levels[pre].append(course)
        #levels =  {0: [1, 2], 1: [3], 2: [3]}
        #out_degree= {0: 0, 1: 1, 2: 1, 3: 2}
        queue = [i for i in out_degree if out_degree[i]==0] #[0]
        # print(queue)
        rs = []
        while queue:
            q = queue.pop()
            rs.append(q)  #rs=[0]
            #找出与0相连的节点，把出度减一
            for node in levels[q]:#[1,2]
                out_degree[node] -= 1
                if out_degree[node] == 0:#出度减为零的时候，加入队列
                    queue.append(node)
        return rs if len(rs) == numCourses else []







    # from collections import *
    
    def findOrder_bfs(self, numCourses, prerequisites):  
        from collections import defaultdict,deque     
        dic = {i: set() for i in range(numCourses)}
        neigh = defaultdict(set)
        for course, prereq in prerequisites:
            dic[course].add(prereq)
            neigh[prereq].add(course)
        #dic = {0: set(), 1: {0}, 2: {0}, 3: {1, 2}} 0没有先决，3的先决是1和2
        #neigh= {0: {1, 2}, 1: {3}, 2: {3}}   0是1和2的先决
        # print(dic, neigh)
        queue = deque([i for i in dic if not dic[i]])#将没有先决的节点放入队列  queue=[0]
        count, res = 0, []
        while queue:
            node = queue.popleft()
            res.append(node)#res=[0]
            count += 1
            for i in neigh[node]:  #遍历neigh[0]=[1,2]
                dic[i].remove(node)#dic[1].remove(0) 遍历指向0的两个节点，并分别把这两个节点中指向0的节点数据删掉，删完以后，把节点放入队列，下次遍历
                if not dic[i]:
                    queue.append(i)
        return res if count == numCourses else []

    
so = Solution()
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# prerequisites = [[]]
# numCourses = 2
# prerequisites = [[0,1],[1,0]]
print(so.findOrder(numCourses, prerequisites))
print('+++++++')
# print(so.findOrder_bfs(numCourses, prerequisites))