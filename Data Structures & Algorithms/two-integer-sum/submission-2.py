class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 2:
            return [0, 1]

        idmap = self.indexMap(nums)
        
        for first_idx, num in enumerate(nums):
            diff = target - num
            if diff in idmap:
                second_idx = idmap[diff]
                if first_idx != second_idx:
                    return [first_idx, second_idx]
        
        # This shouldn't go here.
        return [0, len(nums)]


    def indexMap(self, nums: List[int]) -> dict[int]:
        idmap = {}
        for index, num in enumerate(nums):
            idmap[num] = index
        return idmap