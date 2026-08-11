class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for char in s:
            # Starter elements
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            # Popping closers
            elif char == ")" and len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            elif char == "]" and len(stack) > 0 and stack[-1] == "[":
                stack.pop()
            elif char == "}" and len(stack) > 0 and stack[-1] == "{":
                stack.pop()
            # Otherwise, just append.
            else:
                stack.append(char)
        
        return len(stack) == 0