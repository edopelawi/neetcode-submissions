class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftIdx = 0
        rightIdx = len(heights) - 1
        result = 0

        while leftIdx < rightIdx:        

            leftHeight = heights[leftIdx]
            rightHeight = heights[rightIdx]
            width = rightIdx - leftIdx

            currentVolume = width * min(leftHeight, rightHeight)
            result = max(result, currentVolume)

            # Move the index of the smaller height
            if leftHeight > rightHeight:
                rightIdx -= 1
            elif rightHeight >= leftHeight:
                leftIdx += 1

        return result