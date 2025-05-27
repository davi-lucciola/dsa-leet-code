# Time Complexity: O(n) 
# Space Complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = []

        for char in s:
            if char == '(' or char == '[' or char == '{':
                parenthesis.append(char)
                continue
            
            if char == ')' or char == ']' or char == '}':
                if len(parenthesis) == 0:
                    return False

                if char == ')' and parenthesis[-1] != '(':
                    return False

                if char == ']' and parenthesis[-1] != '[':
                    return False

                if char == '}' and parenthesis[-1] != '{':
                    return False

                parenthesis.pop()

        return len(parenthesis) == 0
