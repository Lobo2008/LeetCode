"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.

"""

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        """
        pre_post_map={"1年级":{"2年级"，”3年级“，”4年级“}}
        key：1年级的课，val：修了1年级的课以后可以修的所有课（就是比1年级更高的课）

        post_pre_map={”五年级“:{“4年级”，“3年级”，“2年级”}}
        key：5年级的课，val：修5年级的课的时候需要先修1~4年级


        2，[[1,0]] 要上1年级的课，必须先上0年级的课，所以true
        2, [[1,0],[0,1]]：要上1年级的课，必须先上0年级的课，而先上0年级的课，必须线上1年级的课，所以False


        """
        if len(prerequisites) == 0:
            return True
        #初始化每个节点的入度为0
        in_degrees = {}
        for u,v in prerequisites:
            if u not in in_degrees:
                in_degrees[u] = 0
            if v not in prerequisites:
                in_degrees[v] = 0
        #计算每个节点的入度
        for u,v in prerequisites:
            in_degrees[v] += 1
        print(in_degrees)
        Q = []
        Seq = []
        #找一个入度为0的节点作为开始，将节点加入序列Seq
        for item in in_degrees:
            if in_degrees[item] == 0:
                Q.append(item)
                in_degrees.pop(item)
                break
        while Q:            
            u = Q.pop()
            Seq.append(u)
            for ux,vx in prerequisites:
                if u == ux:
                    in_degrees[vx] -= 1
            for k,v in in_degrees.items():
                if v == 0:
                    Q.append(k)
                    in_degrees.pop(k)
                    break
        if len(Seq) == numCourses:
            return True
        return False
                


so = Solution()

numCourses = 2
prerequisites =  [[1,0],[0,1]]

numCourses = 4
prerequisites = [[4,3],[4,2],[1,2],[1,3],[2,1]]
# prerequisites = [[4,3],[4,2],[1,2],[1,3]]
print(so.canFinish(numCourses, prerequisites))

# """
# ref：https://www.cnblogs.com/zhaojieyu/p/8543136.html
# 1）先计算所有节点的入度
# 2）然后将入度为0的加入队列，并将其从图里移去，再将移去的元素指向的元素的入读减一，入度为0的就是没有前提要求的项目
# 3）重复以上步骤，如果最终队列的长度等于图的边的数量，说明无环
# """

# def toposort(graph):
#     """
#     {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
#     """
#     in_degrees = dict((u,0) for u in graph)   #初始化所有顶点入度为0
#     vertex_num = len(in_degrees)#边的数量
#     """
#     G = {
#         'a':'bce',
#         'b':'d',
#         'c':'bd',
#         'd':'',
#         'e':'cd'
#     }
#     1)  u=a
#             v=b
#                  {'a': 0, 'b': 1, 'c': 0, 'd': 0, 'e': 0}
#             v=c
#                  {'a': 0, 'b': 1, 'c': 1, 'd': 0, 'e': 0}
#             v=e
#                  {'a': 0, 'b': 1, 'c': 1, 'd': 0, 'e': 1}
#     2) u=b
#             v=d
#                 {'a': 0, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
#     3) u=c
#             v=b
#                  {'a': 0, 'b': 2, 'c': 1, 'd': 1, 'e': 1}
#             v=d
#                {'a': 0, 'b': 2, 'c': 1, 'd': 2, 'e': 1}
#     4) u=d
#             no changes
#     5) u=e
#             v=c
#                  {'a': 0, 'b': 2, 'c': 2, 'd': 2, 'e': 1}
#             v=d
#                  {'a': 0, 'b': 2, 'c': 2, 'd': 3, 'e': 1}
#     """
#     for u in graph:
#         for v in graph[u]:
#             in_degrees[v] += 1       #计算每个顶点的入度
#     print(in_degrees)
#     Q = [u for u in in_degrees if in_degrees[u] == 0]   # 筛选入度为0的顶点
    
#     Seq = []
#     """
#     1) Q=[a],Seq=[] 
#        u=a,Seq=[a]
#        v=b
#             {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 1},   b!=0
#        v=c
#             {'a': 0, 'b': 1, 'c': 1, 'd': 3, 'e': 1}    c!=0
#        v=e 
#             {'a': 0, 'b': 1, 'c': 1, 'd': 3, 'e': 0}    e=0 -> Q=[e]
#     2） Q=[e],Seq=[a]
#         u=[e],Seq=[a,e]
#         v=c
#            {'a': 0, 'b': 1, 'c': 0, 'd': 3, 'e': 0}     c=0 -> Q=[c]
#         v=d
#             {'a': 0, 'b': 1, 'c': 0, 'd': 2, 'e': 0} d!=0
#     3) Q=[c],Seq=[a,e]
#         u=c,Seq=[a,e,c]
#         v=b
#             {'a': 0, 'b': 0, 'c': 0, 'd': 2, 'e': 0}   b=0-> Q=[b]
#         v=d
#             {'a': 0, 'b': 0, 'c': 0, 'd': 1, 'e': 0}   d!=0
#     4)Q=[b],Seq=[a,e,c]
#         u=d,Seq=[a,e,c,b]
#              {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0} d=0 -> Q=[d]
#     5)Q=[d],Seq=[a,e,c,d]
#         u='',Seq=[a,e,c,b,d]


#     """

#     while Q:
#         u = Q.pop()       #默认从最后一个删除
#         Seq.append(u)
#         for v in graph[u]:
#             in_degrees[v] -= 1       #移除其所有指向
#             if in_degrees[v] == 0:
#                 Q.append(v)          #再次筛选入度为0的顶点
#         print('u=',u,'->',in_degrees)
#     if len(Seq) == vertex_num:       #如果循环结束后存在非0入度的顶点说明图中有环，不存在拓扑排序
#         return Seq
#     else:
#         print("there's a circle.")
# G = {
#     'a':'bce',
#     'b':'d',
#     'c':'bd',
#     'd':'',
#     'e':'cd'
# }
#  print(toposort(G))