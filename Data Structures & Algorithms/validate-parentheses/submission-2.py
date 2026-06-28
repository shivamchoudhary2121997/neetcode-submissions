class Solution:
    def isValid(self, s: str) -> bool:
        close_map = {"(":")", "{":"}", "[":"]"}
        openbraces = "({["
        closebraces = ")}]"
        stack = []
        for i in s:
            if i in openbraces:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                c = stack.pop()
                cb = close_map[c]
                if i!=cb:
                    return False
        if len(stack)!=0:
            return False
        return True