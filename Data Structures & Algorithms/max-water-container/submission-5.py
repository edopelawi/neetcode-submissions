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
            # This time: skip the volume computation on smaller bar
            if leftHeight > rightHeight:                
                rightIdx -= 1
                while (rightHeight > heights[rightIdx]) and (leftIdx < rightIdx):
                    rightIdx -= 1
            else:
                leftIdx += 1
                while (leftHeight > heights[leftIdx]) and (leftIdx < rightIdx):
                    leftIdx += 1

        return result

    def maxAreaV1(self, heights: List[int]) -> int:
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