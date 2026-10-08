class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        op = ''
        depth = 0
        for i in s:
            if i == '(' and depth > 0:
                depth += 1
                op += '('
            elif i == '(':
                depth += 1
            else:
                depth -= 1
                if depth == 0:
                    continue
                else:
                    op += ')'
        return op