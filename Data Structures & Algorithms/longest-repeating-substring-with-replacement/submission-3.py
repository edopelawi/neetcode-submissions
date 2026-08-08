class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = Counter()
        leftIdx = 0
        maxLength = 0
        maxFrequency = 0

        for rightIdx in range(len(s)):
            rightChar = s[rightIdx]
            charCount[rightChar] += 1
            # print(f"[^^^] leftIdx: {leftIdx}, rightIndex: {rightIdx}, rightChar: {rightChar}")
            # print(f"[^^^] charCounter: {charCount}")

            maxFrequency = max(maxFrequency, charCount[rightChar])
            windowLength = rightIdx - leftIdx + 1
            replacements = windowLength - maxFrequency # assuming the non-max repeating chars needs to be replaced to get the max length

            # print(f"[^^^] maxFrequency: {maxFrequency}")
            # print(f"[^^^] windowLength: {windowLength}, replacements: {replacements}")

            if replacements > k: # need to move window
                leftChar = s[leftIdx]
                charCount[leftChar] -= 1 # reduce stored frequency
                leftIdx += 1 # move window forward
                
                # print(f"[^^^^^] Replacement goes over chance.")
                # print(f"[^^^^^] Moved leftIdx to {leftIdx}")
                # print(f"[^^^^^] Current charCount: {charCount}")
            
            maxLength = max(maxLength, rightIdx - leftIdx + 1)
            # print(f"[^^^^^^] updated maxLength: {maxLength}")

        return maxLength

    def characterReplacementV2(self, s: str, k: int) -> int: # First sliding window version, fails on "ABBB"
        if len(s) == 1: # Early return
            return 1

        leftIdx = 0
        rightIdx = 1
        leftChar = s[0]
        
        repCounter = 0
        currentLength = 1
        maxLength = 1

        while rightIdx < len(s):
            rightChar = s[rightIdx]
            # print(f"[^^^] rightIdx: {rightIdx}, leftChar: {leftChar}, rightChar: {rightChar}")

            while leftChar == rightChar: # Scan until repeat stops
                rightIdx += 1
                currentLength += 1
                if rightIdx < len(s): # As long not out of bounds
                    rightChar = s[rightIdx]
                else:
                    break

            if rightIdx >= len(s): # Edge stopper
                # print(f"[^^^] rightIdx goes out of bounds at {rightIdx}, stopping.")
                break

            # print(f"[^^^] Chain stops, rightIdx: {rightIdx}, currentLength: {currentLength}")
            if repCounter < k: # Continue as long it's allowed                
                repCounter += 1
                currentLength += 1
                # print(f"[^^^^^] Counter available, moving forward. repCounter: {repCounter}, currentLength: {currentLength}")
            else: # Out of chances
                # print(f"[^^^^^] Counter maxed out, resets window.")
                maxLength = max(maxLength, currentLength)
                # Move the window up
                leftIdx = rightIdx
                leftChar = rightChar
                currentLength = 1
            
            # Prep for next round
            rightIdx += 1

        return max(maxLength, currentLength)

    def characterReplacementV1(self, s: str, k: int) -> int: # Doesn't cover the "Longest Repeating" part
        charCount = Counter(s)
        maxLength = len(s)

        if len(charCount) == 1 or k == 0: # Early return
            return maxLength

        idealDelta = maxLength - k
        # print(f"[^^^] idealDelta: {idealDelta}")
        sortedChars = sorted(charCount, key=charCount.get, reverse=True)
        # print(f"[^^^] sortedChars: {sortedChars}")
        for char in sortedChars:
            count = charCount[char]
            # print(f"[^^^] Evaluating char: {char}, count: {count}")
            if count <= idealDelta:
                return count + k

        return 0
        