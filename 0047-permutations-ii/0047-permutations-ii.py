class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        counter = {}

        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1


        def solve(temp):
            if len(temp) == n:
                result.append(temp[:])
                return None

            for num in counter:
                if counter[num] > 0:
                    temp.append(num)
                    counter[num] -= 1
                    solve(temp)
                    temp.pop()
                    counter[num] += 1

        solve([])

        return result