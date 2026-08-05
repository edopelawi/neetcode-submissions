class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftIdx = 0
        rightIdx = len(heights) - 1
        result = 0

        while leftIdx < rightIdx:        

            leftBuffer = heights[leftIdx]
            rightBuffer = heights[rightIdx]
            width = rightIdx - leftIdx

            result = max(result, self.calculateWater(leftBuffer, rightBuffer, width))

            if leftBuffer > rightBuffer:
                rightIdx -= 1
            elif rightBuffer >= leftBuffer:
                leftIdx += 1

        return result
    
    def calculateWater(self, firstBar: int, secondBar: int, width: int) -> int:
        maxHeight = min(firstBar, secondBar)
        return width * maxHeight
