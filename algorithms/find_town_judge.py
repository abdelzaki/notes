"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise."""


from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ingoing = defaultdict(int)
        outgoing = defaultdict(int)
        for Out, IN in trust:
            ingoing[IN]+= 1
            outgoing[Out]+= 1 

        for person in range(1,n+1):
            if outgoing[person] == 0 and ingoing[person] == n-1 :
                return person 

        return -1 

        print(ingoing) 
        print(outgoing) 

solution = Solution()
n = 3 
trust = [[1,3],[2,3],[3,1]] 

print(solution.findJudge(n,trust))