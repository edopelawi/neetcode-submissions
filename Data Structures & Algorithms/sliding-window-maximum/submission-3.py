class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]: # Non-heap version.

        currentMax = max(nums[0:k]) # Picking the maximum of first window
        result = [currentMax]        
        leftIdx = 0
        
        for rightIdx in range(k, len(nums)):

            if nums[rightIdx] > currentMax: # New number is higher? Pick it up
                currentMax = nums[rightIdx] 
            
            if nums[leftIdx] == currentMax: # Previous windows' element was max? Recalculate
                currentMax = max(nums[leftIdx + 1: rightIdx + 1]) 
            
            leftIdx += 1 
            result.append(currentMax) # Append whatever the max number is. Who cares the number in-between?
        
        return result

    def maxSlidingWindowV4(self, nums: List[int], k: int) -> List[int]: # Proper heap usage, deleting stale values.
        numLength = len(nums)

        # Early returns
        if numLength == 1:
            return nums
        elif numLength == k:
            return [max(nums)]

        # max heap using negative values
        # Each entry = (-value, index)
        maxHeap = []
        result = []

        # First window
        for rightIdx in range(k):
            heapq.heappush(maxHeap, (-nums[rightIdx], rightIdx))

        # First result
        result.append(-maxHeap[0][0])     

        # Further windows
        leftIdx = 1

        for rightIdx in range(k, numLength):
            # Add new right-side number
            heapq.heappush(maxHeap, (-nums[rightIdx], rightIdx))

            # Remove obsolete numbers
            # what maxHeap[0][1] means: for the top item, get index #1 (the original element index)
            while maxHeap[0][1] < leftIdx:
                heapq.heappop(maxHeap)

            # Heap top value is now guaranteed to belong to current window
            result.append(-maxHeap[0][0])
            leftIdx += 1

        return result

    def maxSlidingWindowV3(self, nums: List[int], k: int) -> List[int]: # Failed on test case 40.
        numLength = len(nums)
        
        # Early returns
        if numLength == 1:
            return nums
        elif numLength == k: # the window is just the whole array
            return [max(nums)]

        leftIdx = 0
        rightIdx = k - 1
        
        # First window processing and initial values
        negVisitedNums = [-num for num in nums[leftIdx:rightIdx + 1]]
        heapq.heapify(negVisitedNums)

        maxNum = -negVisitedNums[0]        
        result = [maxNum]
        pendingPoppedNums = []

        # Move right window first
        rightIdx += 1

        print(f"[^^^] Initial value of result: {result}")
        print(f"[^^^] Initial value of negVisitedNums: {negVisitedNums}")

        while rightIdx < numLength:
            # Old window number
            leftNum = nums[leftIdx]

            print(f"[^^^] leftNum from obsolete window: {leftNum}")

            if leftNum == -negVisitedNums[0]: # If leftNum was maximum, pop it out
                print(f"[^^^^^] Popping negVisitedNums since leftNum was maximum")
                heapq.heappop(negVisitedNums)
                oldNumPopped = True
            else:
                print(f"[^^^^^] Pushing obsolete leftNum to pendingPoppedNums, since it's not maximum")
                heapq.heappush(pendingPoppedNums, -leftNum)

            # Check pending popped nums
            if len(pendingPoppedNums) > 0 and \
                pendingPoppedNums[0] == negVisitedNums[0]: # If the maximum was pending sometime ago, pop it out
                print(f"[^^^^^] Popping negVisitedNums since pendingPoppedNums' max was the maximum")
                heapq.heappop(negVisitedNums)

            # Further windows
            rightNum = nums[rightIdx]
            currentMaxNum = None if len(negVisitedNums) == 0 else -negVisitedNums[0]
            
            if currentMaxNum is None or rightNum >= currentMaxNum: # Case 1: new value is the new maximum
                result.append(rightNum)                
            else: # Case 2: new value is not the maximum, append the current maximum instead
                result.append(currentMaxNum)

            # Remember to push the value as negatives
            heapq.heappush(negVisitedNums, -rightNum)
            
            rightIdx += 1
            leftIdx += 1

        return result

    def maxSlidingWindowV2(self, nums: List[int], k: int) -> List[int]: # Failed on test case 41
        numLength = len(nums)
        
        # Early returns
        if numLength == 1:
            return nums
        elif numLength == k: # the window is just the whole array
            return [max(nums)]

        leftIdx = 0
        rightIdx = k - 1
        
        # First window processing and initial values
        negVisitedNums = [-num for num in nums[leftIdx:rightIdx + 1]]
        heapq.heapify(negVisitedNums)

        maxNum = -negVisitedNums[0]        
        result = [maxNum]

        # Move right window first
        rightIdx += 1

        while rightIdx < numLength:
            # Old window number
            leftNum = nums[leftIdx]

            if leftNum == -negVisitedNums[0]: # If leftNum was maximum, pop it out
                heapq.heappop(negVisitedNums)

            # Further windows
            rightNum = nums[rightIdx]
            currentMaxNum = None if len(negVisitedNums) == 0 else -negVisitedNums[0]
            
            if currentMaxNum is None or rightNum >= currentMaxNum: # Case 1: new value is the new maximum
                result.append(rightNum)                
            else: # Case 2: new value is not the maximum, append the current maximum instead
                result.append(currentMaxNum)

            # Remember to push the value as negatives
            heapq.heappush(negVisitedNums, -rightNum)
            
            rightIdx += 1
            leftIdx += 1

        return result


    def maxSlidingWindowV1(self, nums: List[int], k: int) -> List[int]: # This case got issue: "Time Limit Exceeded" on case 38.
           
        numLength = len(nums)
        
        # Early returns
        if numLength == 1:
            return nums
        elif numLength == k: # the window is just the whole array
            return [max(nums)]


        leftIdx = 0
        rightIdx = k - 1

        leftNum = nums[leftIdx]
        previousMaxNum = 0

        result = []

        while rightIdx < numLength: # TODO: Revisit how to make better space complexitiy
            if len(result) == 0: # First window
                # print("[^^^] First window!")
                maxNum = max(nums[leftIdx:rightIdx + 1])
                result.append(maxNum)
                previousMaxNum = maxNum
                rightIdx += 1
                # print(f"[^^^^^] maxNum: {maxNum}, result: {result}")
                # print(f"[^^^^^] moving to rightIdx: {rightIdx}")
                continue
            
            # Further windows
            rightNum = nums[rightIdx]
            # print(f"[^^^] rightIdx: {rightIdx}, rightNum: {rightNum}")

            # Case 1: rightNum is greater or equal than previousMaxNum
            if rightNum >= previousMaxNum:
                # print(f"[^^^^^] rightNum: {rightNum} is greater or equal than previousMaxNum: {previousMaxNum}")
                result.append(rightNum)
                previousMaxNum = rightNum           
            else:
                # Fallback case: recalculate everything
                # print(f"[^^^^^] Recalculate maximum! of the current window")
                subarray = nums[leftIdx + 1: rightIdx + 1]
                maxNum = max(subarray)
                result.append(maxNum)
                previousMaxNum = maxNum
            
            # print("[^^^^^^^] Updated result from the step: {result}")

            rightIdx += 1
            leftIdx += 1

        return result