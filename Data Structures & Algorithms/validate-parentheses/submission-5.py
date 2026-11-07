class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False

        has_open_brackets = False
        close_brackets = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        # Only contains open brackets.
        stack = []
        for c in s:
            if c not in close_brackets:
                stack.append(c)
            else:
                if stack and close_brackets[c] == stack[-1]:
                    stack.pop()
                else:
                    return False      

        return len(stack) == 0
        