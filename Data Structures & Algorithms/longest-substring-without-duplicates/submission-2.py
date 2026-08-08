class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        currentLength = 0
        window = ""

        for char in s:
            # print("[^^^] Current char: ", char)
            if char in window: # Repetition found                
                maxLength = max(maxLength, currentLength)
                repeatCharIndex = window.find(char)
                # print("[^^^^^] Repeat char found in index: ", repeatCharIndex)
                window = window[repeatCharIndex + 1:] + char
                currentLength = len(window)
                # print(f"[^^^^^] New window: {window}, length: {currentLength}")                 
                
            else:                
                currentLength += 1
                window += char
                # print(f"[#####] New char found: {char}, updated window: {window}")
        
        return max(maxLength, currentLength)


    def lengthOfLongestSubstringV1(self, s: str) -> int:
        
        maxLength = 0
        currentLength = 0
        stringSet = set()

        for char in s:

            if char in stringSet: # Repetition found
                maxLength = max(maxLength, currentLength)
                currentLength = 1
                stringSet = set(char)
            else:
                currentLength += 1
                stringSet.add(char)
        
        return max(maxLength, currentLength)

