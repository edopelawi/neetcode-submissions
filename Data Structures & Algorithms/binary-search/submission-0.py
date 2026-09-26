class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftIdx = 0
        rightIdx = len(nums) - 1

        while leftIdx <= rightIdx:
            midIdx = (leftIdx + rightIdx) // 2
            val = nums[midIdx]

            if val == target:
                return midIdx
            
            elif val < target:
                leftIdx = midIdx + 1
            
            elif val > target:
                rightIdx = midIdx - 1
        
        return -1
        