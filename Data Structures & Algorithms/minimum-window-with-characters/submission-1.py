class Solution:
    def minWindow(self, s: str, t: str) -> str:        
        targetCounter = Counter(t)
        targetLength = len(t)
        
        if len(s) <= targetLength: # Early return
            windowCounter = Counter(s)
            return s if windowCounter == targetCounter else ""
        
        windowCounter = Counter()
        targetKeyLength = len(targetCounter)
        formedKeyLength = 0

        leftIndex = 0        
        bestStart = 0
        bestLength = None 
        substrings = []

        for rightIndex, rightChar in enumerate(s):
            windowCounter[rightChar] += 1

            # Did this char just satisfy a requirement?
            if rightChar in targetCounter and \
                windowCounter[rightChar] == targetCounter[rightChar]:
                formedKeyLength += 1

            # If the window is valid, then try making it smaller.
            while formedKeyLength == targetKeyLength:
                windowLength = rightIndex - leftIndex + 1
                
                if bestLength == None or windowLength < bestLength:
                    bestStart = leftIndex
                    bestLength = windowLength
                
                leftChar = s[leftIndex]
                windowCounter[leftChar] -= 1

                # Removing this character broke a requirement.
                if (
                    leftChar in targetCounter
                    and windowCounter[leftChar] < targetCounter[leftChar]
                ):
                    formedKeyLength -= 1

                leftIndex += 1
 

        return "" if bestLength == None else s[bestStart:bestStart + bestLength]



    def minWindowV2(self, s: str, t: str) -> str: # Failed on s="OUZODYXAZV", t="XYZ"
        windowCounter = Counter(s)
        targetCounter = Counter(t)
        targetLength = len(t)
        
        if len(s) <= targetLength: # Early return            
            return s if windowCounter == targetCounter else ""

        print(f"[^] targetCounter: {targetCounter}")
        leftIndex = 0
        rightIndex = 0 
        substrings = []

        while rightIndex < len(s):
            rightChar = s[rightIndex]            
            # print(f"[^^^] rightIndex: {rightIndex}, rightChar: {rightChar}, windowCounter: {windowCounter}")

            # We can ignore chars that is not in the targetCounter.
            if rightChar not in targetCounter:
                rightIndex += 1
                continue

            # Invariant: LEADING char count in the window should not exceed the targetCounter
            # Slide the window to remove excess chars until the invariant is satisfied.            
            while windowCounter[rightChar] > targetCounter[rightChar]:
                # print(f"[^^^^^] Sliding windowCounter to fit targetCounter's rightChar ({rightChar}) occurrence")
                # print(f"[^^^^^] windowCounter[{rightChar}]: {windowCounter[rightChar]}, targetCounter[{rightChar}]: {targetCounter[rightChar]}")
                leftChar = s[leftIndex]

                if windowCounter[leftChar] <= targetCounter[leftChar]:
                    # print(f"[^^^^^] Sliding windowCounter cancelled due to prefix of targetCounter, leftChar: {leftChar}")
                    break

                # print(f"[^^^^^] Removing char from leftIndex: {leftIndex}, leftChar: {leftChar}")
                windowCounter[leftChar] -= 1
                leftIndex += 1
                # print(f"[^^^^^] Updated windowCounter: {windowCounter}, leftIndex: {leftIndex}")
            
            # Make sure rightIndex follows leftIndex if it goes faster.
            rightIndex = max(rightIndex, leftIndex)

            # Invariant: Substring is found when all targetCounter occurrences are covered by current windowCounter.
            validSubstring = True
            for char in targetCounter.keys():
                if char not in windowCounter or targetCounter[char] > windowCounter[char]:
                    validSubstring = False
                else:
                    continue
            
            if validSubstring:
                # Throw excess prefixes
                while s[leftIndex] not in targetCounter:
                    windowCounter[leftIndex] -= 1
                    leftIndex += 1

                # The substring is from leftIndex until end of String                                       
                result = s[leftIndex:]
                # print(f"[^^^] Valid substring found, leftIndex: {leftIndex}, rightIndex: {rightIndex}, result (leftIndex until end): {result}")
                substrings.append(result)

            rightIndex += 1           

        print(f"[^^^] Final substring options: {substrings}")

        return "" if len(substrings) == 0 else sorted(substrings, key=len)[0]

    def minWindowV1(self, s: str, t: str) -> str: # This version fails on Test Case 24
        targetCounter = Counter(t)
        targetLength = len(t)
        
        if len(s) <= targetLength: # Early return
            inputCounter = Counter(s)
            return s if inputCounter == targetCounter else ""

        leftIndex = 0
        windowCounter = Counter()
        substrings = []

        for rightIndex in range(len(s)):            
            rightChar = s[rightIndex]
            windowCounter[rightChar] += 1
            print(f"[^^^] rightIndex: {rightIndex}, rightChar: {rightChar}, windowCounter: {windowCounter}")

            # We can ignore chars that is not in the targetCounter.
            if rightChar not in targetCounter:
                continue

            # Invariant: char count in the window should not exceed the targetCounter
            # Slide the window to remove excess chars until the invariant is satisfied.            
            while windowCounter[rightChar] > targetCounter[rightChar]:
                print(f"[^^^^^] Sliding windowCounter to fit targetCounter's rightChar ({rightChar}) occurrence")
                print(f"[^^^^^] windowCounter[{rightChar}]: {windowCounter[rightChar]}, targetCounter[{rightChar}]: {targetCounter[rightChar]}")
                leftChar = s[leftIndex]
                print(f"[^^^^^] Removing char from leftIndex: {leftIndex}, leftChar: {leftChar}")
                windowCounter[leftChar] -= 1
                leftIndex += 1
                print(f"[^^^^^] Updated windowCounter: {windowCounter}, leftIndex: {leftIndex}")
                

            # Invariant: the shortest substring is found when the targetCounter is a proper subset of windowCounter.
            if windowCounter.items() >= targetCounter.items():
                # Throw excess prefixes
                while s[leftIndex] not in targetCounter:
                    windowCounter[s[leftIndex]] -= 1
                    leftIndex += 1
                       
                result = s[leftIndex:rightIndex+1]
                print(f"[^^^] Valid shortest substring found, result: {result}")
                substrings.append(result)   

        print(f"[^^^] Final substring options: {substrings}")

        return "" if len(substrings) == 0 else sorted(substrings, key=len)[0]