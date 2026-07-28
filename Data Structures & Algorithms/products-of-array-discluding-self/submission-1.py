class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # print(f"[^^^] Input list: {nums}")

        numLength = len(nums)
        result = [1] * numLength

        # print(f"[%%%] Prefix array processing!")
        prefix = 1
        for index in range(numLength):
            # print(f"[%%%] Index: {index}, initial prefix value: {prefix}")
            result[index] = prefix
            multiplier = nums[index]
            prefix *= multiplier
            # print(f"[%%%] Multiplier: {multiplier}")
            # print(f"[%%%] Prefix after multiply: {prefix}")
            # print(f"[%%%] Result array in-mid prefix processing: {result}")

        # print(f"[$$$] Result array after prefix processing: {result}")

        # print(f"[###] Suffix array processing!")
        suffix = 1
        backwardIterator = range(numLength-1, -1, -1)
        for index in backwardIterator:
            # print(f"[###] Index: {index}, initial suffix value: {suffix}")
            result[index] *= suffix
            multiplier = nums[index]
            suffix *= multiplier
        #     print(f"[###] Multiplier: {multiplier}")
        #     print(f"[###] Suffix after multiply: {suffix}")
        #     print(f"[$$$] Result array in-mid suffix processing: {result}")

        # print(f"[$$$] Result array after suffix processing: {result}")
        return result

        


        