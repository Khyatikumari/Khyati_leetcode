class Solution:
    def removeCoveredIntervals(self, I: List[List[int]]) -> int:
        I.sort()
        a, b, cnt=-1, -1, 0
        for c, d in I:
            if c>a and d>b:
                a=c
                cnt+=1
            b=max(b, d)
        return cnt
        