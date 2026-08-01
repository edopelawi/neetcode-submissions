class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        # Alphanumeric filtering + lowercasing
        alnumString = "".join([c.lower() for c in s if c.isalnum()])

        maxIdx = len(alnumString) // 2
        print("[^^^] Alphanumeric String: ", alnumString)
        print("[^^^] Max Idx: ", maxIdx)
        for i in range(maxIdx):
            left = alnumString[i]
            right = alnumString[-i-1]
            if left != right:
                print(f"[^^^] Invalid matches, char on {i}: {left}, char on {len(alnumString) - i} (or -{i}): {right}")
                return False
        
        return True
        