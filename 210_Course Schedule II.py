class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        result = []
        next_course_list = [[] for i in range(numCourses)]
        in_degree = [0]*numCourses
        for edge in prerequisites:
            in_degree[edge[0]] += 1
            next_course_list[edge[1]].append(edge[0])

        candidates = [i for i in range(numCourses) if in_degree[i] == 0]

        for i in range(numCourses):
            if len(candidates) == 0:
                return []
            course = candidates.pop()
            result.append(course)
            for next_course in next_course_list[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    candidates.append(next_course)

        return result

print Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]])