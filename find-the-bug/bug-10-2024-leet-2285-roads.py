# FIND THE BUG (#10)
# https://leetcode.com/problems/maximum-total-importance-of-roads
from typing import List   # leetcode automatically does this



from queue import PriorityQueue

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degs = { i : 0 for i in range(n) }
        for edg in roads:
            (a, b) = edg
            degs[a] = degs[a] + 1
            degs[b] = degs[b] + 1

        pq = PriorityQueue()
        for n, deg in degs.items():
            pq.put( (deg, n) )
        
        vals = { i : 0 for i in range(n) }
        for val in range(1, n+1):
            _, city = pq.get()
            vals[city] = val

        sum = 0
        for edg in roads:
            (a, b) = edg
            sum += (vals[a] + vals[b])

        return sum



# print( Solution().maximumImportance(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]) )

