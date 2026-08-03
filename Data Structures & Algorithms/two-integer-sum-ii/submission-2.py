class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Early return
        numLength = len(numbers)

        if numLength == 2:
            return [1,2] # Output request: 1-indexed array
        
        leftIdx = 0
        rightIdx = numLength - 1

        while leftIdx < rightIdx:

            numSum = numbers[leftIdx] + numbers[rightIdx]

            if (numSum == target):
                # Output request: 1-indexed array
                return [leftIdx + 1, rightIdx + 1]
            elif (numSum > target):
                rightIdx -= 1
            else:
                leftIdx += 1
        
        # This line shouldn't run, since the numbers should have solutions.
        return [leftIdx + 1, rightIdx + 1] 

