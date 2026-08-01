class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        currentNum = None
        currentLen = 0
        longestLen = 0
        
        for num in numset:
            currentNum = num

            if currentNum - 1 not in numset:
                currentNum = num
                currentLen = 1
                # Iterate forward
                while currentNum + 1 in numset:
                    currentNum += 1
                    currentLen += 1
            
                longestLen = max(currentLen, longestLen)
        
        return longestLen

        