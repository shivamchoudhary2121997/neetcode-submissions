class Solution:
    def isValid(self, s: str) -> bool:
        close_map = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for ch in s:
            if ch in close_map:
                stack.append(ch)
            else:
                if not stack:
                    return False
                if close_map[stack.pop()] != ch:
                    return False
        return len(stack) == 0