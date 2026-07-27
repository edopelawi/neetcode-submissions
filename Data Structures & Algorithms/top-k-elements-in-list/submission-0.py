class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0: # Early return
            return []

        # Zero by default for first-timer numbers
        counter = defaultdict(int)       

        # Count the occurrences
        for num in nums:            
            counter[num] += 1

        # Sort the numbers by occurrence counter
        sorted_nums = sorted(counter, key=lambda num: counter[num], reverse=True)
        
        # result
        if len(sorted_nums) <= k:
            return sorted_nums
        else:
            return sorted_nums[0:k]

            
                        


