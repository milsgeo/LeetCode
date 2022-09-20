class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={")":"(", "}":"{", "]":"["}
        
        for char in s:
            if char in mapping:
                top_el=stack.pop() if stack else '#'
                if mapping[char]!=top_el:
                    return False
            else:
                stack.append(char)
        return not stack
        