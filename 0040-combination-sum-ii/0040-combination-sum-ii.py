class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        result = []

        def backtrack(start, current, remaining):

            # Found valid combination
            if remaining == 0:
                result.append(current[:])
                return

            # Invalid path
            if remaining < 0:
                return

            for i in range(start, len(candidates)):

                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Pruning
                if candidates[i] > remaining:
                    break

                current.append(candidates[i])

                # Move to next index (use once only)
                backtrack(
                    i + 1,
                    current,
                    remaining - candidates[i]
                )

                # Backtrack
                current.pop()

        backtrack(0, [], target)

        return result