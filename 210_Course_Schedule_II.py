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
            第二次的[1.2]可互换，则有[0]->[2,1]->[3]工三种

        """
        from collections import defaultdict
        graph = defaultdict(lambda: [], {})
        levels = defaultdict(lambda: [], {})
        in_degree = {node:0 for node in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)
            in_degree[prereq] += 1
        # print(graph)
        # print(in_degree)
        #in_degree={0: 2, 1: 1, 2: 1, 3: 0}
        """
        将入度相等的分为一组
        """
        max_ind = 0
        for k in in_degree:
            if in_degree[k] > max_ind:
                max_ind = in_degree[k]
            levels[in_degree[k]].append(k)
        # levels[2].append(4)
        # levels[1].append(5)
        #levels={2: [0], 1: [1, 2], 0: [3]}
        # levels={2:[1,2],1:[4,5],0:[7,8]}
        # thislevel = self.permute(levels[max_ind])#[[0,4],[4,0]]
        # max_ind -= 1
        
        thislevel = levels.pop(len(levels)-1)
        thislevel = self.permute(thislevel)
        if levels:
            while levels:
                rslevel = []
                nextlevel = levels.pop(len(levels)-1)
                nextlevel = self.permute(nextlevel)
                for i in thislevel:
                    for j in nextlevel:
                        rslevel.append(i+j)
            
                thislevel = rslevel
            return rslevel
        else:
            return thislevel     
           
    def permute(self, num):
        if len(num) == 0: return []
        if len(num) == 1: return [num]
        res = []
        for i in range(len(num)):
            for j in self.permute(num[:i] + num[i+1:]):
                res.append([num[i]] + j)
        return res


            


    
so = Solution()
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(so.findOrder(numCourses, prerequisites))