class Solution:
    # def checkInclusion(self, s1: str, s2: str) -> bool:

    def checkInclusion(self, s1: str, s2: str) -> bool: #Failing on Test Case no. 41. Crazy, lol

        targetLength = len(s1)
        targetCounter = Counter(s1)
        currentCounter = Counter()

        leftIdx = 0

        for rightIdx in range(len(s2)):
            rightChar = s2[rightIdx]
            print(f"[^^^] leftIdx: {leftIdx}, rightIdx: {rightIdx}, rightChar: {rightChar}")            
            if rightChar in targetCounter.keys():
                currentCounter[rightChar] += 1
                print(f"[^^^^^] Matching rightChar found, currentCounter: {currentCounter}")
            elif len(currentCounter) > 0 : # Combo broken
                print(f"[^^^^^] Non-matching rightChar, currentCounter exists")
                print(f"[^^^^^] Resetting currentCounter")                
                currentCounter = Counter()                

            if len(currentCounter) == 0 or (len(currentCounter) == 1 and list(currentCounter.values()) == [1]):
                print(f"[^^^^^] New combo found.")
                print(f"[^^^^^] Moving leftIdx to follow rightIdx, currentCounter: {currentCounter}")
                leftIdx = rightIdx

            if (rightIdx - leftIdx + 1) == targetLength:
                print(f"[^^^^^^] Window meets target length!")
                if targetCounter == currentCounter:
                    return True
                else:
                    print(f"[^^^^^^^^] Non matching counter, moving window forward")
                    # Move the sliding window forward                    
                    leftChar = s2[leftIdx]
                    # Move while the same char still found in currentCounter
                    while currentCounter[leftChar] > targetCounter[leftChar]:
                        leftIdx += 1
                        currentCounter[leftChar] -= 1

                    print(f"[^^^^^^^^] Window moved, leftIdx: {leftIdx}, currentCounter: {currentCounter}")

        return targetCounter == currentCounter