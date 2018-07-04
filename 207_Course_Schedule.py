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

        pre_post_map ={} # key is one course, value is a set of all courses need this course as prerequisite
        post_pre_map = {} # key is one course, value is a set of all courses need to learn before learning this course
        for post, pre in prerequisites:#post是key，pre是val，即p=[[高数下,高数下],[大三,大2]]的话，第一次：高数上->高数下,第二次：大3->大2
            if post not in post_pre_map:
                post_pre_map[post] = set()
            post_pre_map[post].add(pre)#po={"高数下":”高数上“},要选高数下，必须先选高数上
            if pre not in pre_post_map:#
                pre_post_map[pre] = set()
            pre_post_map[pre].add(post) #po={”高数上“：”高数下“}，选了高数上以后，可以选高数下           
        
        """
        set({"lzh":1992})={"lzh"}取的是key

        set({大1，大2，大3，大4}) ^ set({大4，大2})  =>  {大1，大3}
        """

        next_to_learn = set(range(numCourses)) ^ set(post_pre_map) # learn the ones that do not have any prerequiste course first (base courses)
        learned_courses = set() # courses already learned so far
        while next_to_learn: # still have courses to learn
            course = next_to_learn.pop() # learn this course
            learned_courses.add(course) # this course now learned
            if course in pre_post_map: # if this course is a prerequiste for other course(s)
                for post_course in pre_post_map[course]:
                    post_pre_map[post_course].remove(course) # this prerequiste course for this post_course is learned
                    if post_pre_map[post_course] == set(): # all prerequiste course(s) for this post_course are learned
                        next_to_learn.add(post_course) # now we can learn this higher level course
        return len(learned_courses) == numCourses