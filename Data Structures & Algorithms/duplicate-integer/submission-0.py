class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for number in nums:
            if number in counter:
                return True
            else:
                counter[number] = 1

        return False