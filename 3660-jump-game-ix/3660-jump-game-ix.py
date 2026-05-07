from typing import List

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        
        # prefix maximums
        pref_max = [0] * n
        pref_max[0] = nums[0]
        for i in range(1, n):
            pref_max[i] = max(pref_max[i-1], nums[i])
        
        # suffix minimums
        suff_min = [0] * n
        suff_min[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suff_min[i] = min(suff_min[i+1], nums[i])
        
        ans = [0] * n
        start = 0
        for i in range(n-1):
            if pref_max[i] <= suff_min[i+1]:
                # segment [start, i]
                seg_max = max(nums[start:i+1])
                for j in range(start, i+1):
                    ans[j] = seg_max
                start = i + 1
        
        # last segment
        seg_max = max(nums[start:])
        for j in range(start, n):
            ans[j] = seg_max
        
        return ans