class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c in ['(', '[', '{']:
                stk.append(c)
            else:
                if not stk:
                    return False
                key = stk.pop()
                if c == ')' and key != '(': return False
                if c == ']' and key != '[': return False
                if c == '}' and key != '{': return False
        return len(stk) == 0