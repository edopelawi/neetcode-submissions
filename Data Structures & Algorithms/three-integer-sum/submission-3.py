class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numLength = len(nums)
        # Early return
        if numLength == 3:
            return [nums] if sum(nums) == 0 else []
        
        nums.sort()
        # print(f"Sorted input: {nums}")

        idx_1 = 0
        result = set()

        while idx_1 < numLength - 3:
            idx_2 = idx_1 + 1
            idx_3 = numLength - 1
            
            num_1 = nums[idx_1]
            # print(f"[###] idx_1: {idx_1}, num_1: {num_1}")

            while idx_2 > idx_1 and idx_2 < idx_3: # Scan the right side to prevent duplicates
                num_2 = nums[idx_2]
                num_3 = nums[idx_3]
                
                # print(f"[####] idx_2: {idx_2}, num_2: {num_2}")
                # print(f"[####] idx_3: {idx_3}, num_3: {num_3}")
                current_sum = num_1 + num_2 + num_3
                # print(f"[####] current_sum: {current_sum}")

                if current_sum == 0:
                    # print(f"[#####] Targeted sum found!")
                    result.add((num_1, num_2, num_3))
                    # Checking next combo
                    idx_2 += 1
                elif current_sum > 0:
                    # print(f"[#####] Sum bigger than 0, reducing idx_3")
                    idx_3 -= 1
                elif current_sum < 0:
                    # print(f"[#####] Sum less than 0, increasing idx_2")
                    idx_2 += 1
                else:
                    # print(f"[#####] Unexpected condition, sum: {current_sum}, breaking loop")                    
                    break
            
            # Moving to the next idx_1
            # print(f"[####] End of inner loop, increasing idx_1")
            idx_1 += 1
        
        # Turning it back to array of arrays
        return [list(item) for item in result]


        