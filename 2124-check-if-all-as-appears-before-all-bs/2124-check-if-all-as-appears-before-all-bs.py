class Solution:
    def checkString(self, s: str) -> bool:
        return all(map(le, s, islice(s, 1, None)))