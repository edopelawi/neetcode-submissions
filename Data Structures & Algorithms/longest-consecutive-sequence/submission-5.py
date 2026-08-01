class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in numset:
            
            # Sequence starter
            if num - 1 not in numset:
                length = 1

                while num + 1 in numset:
                    num += 1 # It's safe to mutate current variable in the for-loop
                    length += 1
                
                # End of the sequence
                longest = max(longest, length)

        return longest

    def longestConsecutiveV1(self, nums: List[int]) -> int:
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

        