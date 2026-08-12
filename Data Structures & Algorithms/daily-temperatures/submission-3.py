class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        count = len(temperatures)

        # Edge case
        if (count == 1):
            return [0]
        
        monotonicStack = deque() # Smallest element on the last.
        result = [0] * count # Default: no warmer days. Winter is coming.

        for index, temp in enumerate(temperatures):
            # print(f"[^^^] Evaluating temp: {temp}, index: {index}")
            
            # Case 1: current temp is warmer than the the stack contents
            
            while len(monotonicStack) > 0:
                pendingIndex, pendingTemp = monotonicStack[-1]
                # print(f"[^^^^^] Popping stack. pendingTemp: {pendingTemp}, pendingIndex: {pendingIndex}")
                if pendingTemp < temp:
                    result[pendingIndex] = index - pendingIndex # Update the day
                    monotonicStack.pop()
                else:
                    break

            # Case 2: curent temp is colder than the rest of stack, put it on the stack
            # print(f"[^^^^^] Colder days are done, adding temp and index to current stack")
            monotonicStack.append((index, temp))            
        
        return result

    def dailyTemperaturesV2(self, temperatures: List[int]) -> List[int]:
        
        count = len(temperatures)

        # Edge case
        if (count == 1):
            return [0]

        tempStack = deque() # Stack structure: tuple of (temp, idx)
        tempStack.append((temperatures[0], 0)) 
        result = [0] * count # First assumption: it never gets warmer by default

        # print(f"[^] Inital tempStack: {tempStack}")
        for idx in range(1, count):
            temp = temperatures[idx]
            missingResult = deque()

                
            # print(f"[^^^] idx: {idx}, temp: {temp}")

            while len(tempStack) > 0: # Check pending calculations

                pendingTemp, pendingIdx = tempStack.pop()

                if pendingTemp < temp:
                    idxDiff = idx - pendingIdx
                    result[pendingIdx] = idxDiff
                    # print(f"[^^^^^] Warmer days found for pendingTemp: {pendingTemp}, pendingIdx: {pendingIdx}, idxDiff: {idxDiff}")
                else:
                    missingResult.appendleft((pendingTemp, pendingIdx))
                    # print(f"[^^^^^] Not warmer day, putting back to stack for pendingTemp: {pendingTemp}, pendingIdx: {pendingIdx}")
                    # print(f"[^^^^^] missingResult: {missingResult}")
            
            # print(f"[^^^^] Missing result: {missingResult}")
            tempStack.extend(missingResult)
            tempStack.append((temp, idx)) # Since we haven't calculated curent day
            # print(f"[^^^^] tempStack: {tempStack}")

        return result


    def dailyTemperaturesV1(self, temperatures: List[int]) -> List[int]: # O(n^2), inefficient. Time limit exceeded on case 23

        maxIndex = len(temperatures)
        result = [0] * maxIndex # First assumption: it never gets better by default
        result[-1] = 0 # Last day won't get better

        for index in range(maxIndex - 1, -1, -1):
            temp = temperatures[index]
            
            for backIndex in range(index - 1, -1, -1):
                backTemp = temperatures[backIndex]
                if backTemp < temp: # If it's cooler in the past
                    result[backIndex] = index - backIndex # Put the diff

        return result
            

