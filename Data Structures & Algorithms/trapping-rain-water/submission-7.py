class Solution:
    def trap(self, height: List[int]) -> int: # Two-pointer version. No need for array, just maxes.
        leftIdx = 0
        rightIdx = len(height) - 1
        leftMax = height[leftIdx]
        rightMax = height[rightIdx]

        trappedWater = 0
        
        while leftIdx < rightIdx:
            leftMax = max(leftMax, height[leftIdx])
            rightMax = max(rightMax, height[rightIdx])

            if leftMax <= rightMax: 
                # calculate and move based on the left pointer (local minima)
                trappedWater += leftMax - height[leftIdx]
                leftIdx += 1
            else:
                # calculate and move based on the right pointer (local minima)
                trappedWater += rightMax - height[rightIdx]
                rightIdx -= 1

        return trappedWater




    def trapV1(self, height: List[int]) -> int: # Prefix and Suffix Array version
        tallestLeft = []
        tallestRight = [0] * len(height)

        maxHeight = 0
        for forwardIdx in range(len(height)):
            maxHeight = max(maxHeight, height[forwardIdx])
            tallestLeft.append(maxHeight)           
        
        maxHeight = 0
        for backwardIdx in range(len(height)-1, -1, -1):
            maxHeight = max(maxHeight, height[backwardIdx])
            tallestRight[backwardIdx] = maxHeight

        trappedWater = 0
        # print("[^^^] tallestLeft: ", tallestLeft)
        # print("[^^^] tallestRight: ", tallestRight)
        # print("[^^^] Computing Water level!")
        for idx in range(len(height)):
            # Compute difference, since water spills over
            waterLevel = min(tallestLeft[idx], tallestRight[idx])
            # Trapped water means water level minus current height            
            wallHeight = height[idx]
            # print(f"[^^^^^] idx: {idx}, waterLevel: {waterLevel}, wallHeight: {wallHeight}")
            trappedWater += waterLevel - height[idx]
        
        return trappedWater

        


    def trapNotWorking(self, height: List[int]) -> int:
        trappedWater = []
        startIndex = 0        
        maxIndex = len(height) - 1

        while startIndex < maxIndex:
            # Search non-zero bars
            startHeight = height[startIndex]
            print(f"[^^^] startIndex: {startIndex}, startHeight: {startHeight}")
            while startHeight == 0:
                startIndex += 1
                startHeight = height[startIndex]
                continue
            
            # After we have one, then two-pointers
            nextIndex = startIndex + 1
            nextHeight = height[nextIndex]
            maxPossibleWater = 0
            currentDiffWater = {}


            # Traverse until we have limiting bar
            while nextHeight < startHeight and nextIndex < maxIndex:                
                maxPossibleWater += startHeight - nextHeight        

                nextIndex += 1
                if nextIndex >= maxIndex: # out of bounds
                    continue
                
                currentHeight = nextHeight                
                nextHeight = height[nextIndex]

                currentDiff = currentHeight - nextHeight
                if currentDiff > 0 :
                    currentDiffWater[nextIndex] = currentDiff
                
            
            print(f"[^^^^^] Finished inner loop. nextIndex: {nextIndex}, maxPossibleWater: {maxPossibleWater}, currentDiffWater: {currentDiffWater}")
            print(f"[^^^^^] startHeight: {startHeight}, nextHeight: {nextHeight}")

            if nextIndex < maxIndex: # not out of bounds
                trappedWater.append(maxPossibleWater)
            elif height[maxIndex] >= startHeight: # the last wall could contain all of the water
                trappedWater.append(maxPossibleWater)            
            else: # out of bounds, just sum what's possible
                trappedWater.append(sum(currentDiffWater.values()))

            # Cut the top of trapped water based on the limiting bar
            # TBA
            startIndex = nextIndex

        result = sum(trappedWater)
        print("[###] Result: ", result)
        return result
        