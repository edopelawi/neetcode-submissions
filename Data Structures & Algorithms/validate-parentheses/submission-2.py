class Solution:
    def isValid(self, s: str) -> bool: # Cleaner with dict
        stack = deque()
        matches = {
            "]": "[",
            ")": "(",
            "}": "{"        
        }

        for char in s:
            if char not in matches.keys():
                stack.append(char)
                continue
            
            opener = matches[char]
            if len(stack) > 0 and stack[-1] == opener:
                stack.pop()
            else:
                stack.append(char)
        
        return len(stack) == 0


    def isValidV1(self, s: str) -> bool: # Regular
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