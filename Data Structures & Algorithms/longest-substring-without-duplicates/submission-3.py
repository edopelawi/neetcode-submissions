class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int: # Proper sliding window version
        leftIdx = 0
        rightIdx = 0
        maxLength = 0
        seen = set()

        while rightIdx < len(s):
            char = s[rightIdx]
            if char not in seen: # Extend window
                seen.add(char)
                maxLength = max(maxLength, rightIdx - leftIdx + 1)
            
            else: # Shrink window until duplicates removed
                # Move the left index for scanning
                while s[leftIdx] != char:
                    seen.remove(s[leftIdx])
                    leftIdx += 1

                # Out of the loop, keep the current char in seen
                # since it's on the duplicate case
                leftIdx += 1
            # Continue to next char                        
            rightIdx += 1

        return maxLength


    def lengthOfLongestSubstringV2(self, s: str) -> int: # Works, but it creates a new String everytime it finds repeated chars
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


    def lengthOfLongestSubstringV1(self, s: str) -> int: # Doesn't cover all cases
        
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

