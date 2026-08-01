class Solution:

    def isPalindrome(self, s: str) -> bool:
        # Two pointers version, less memory allocation.
        leftIdx = 0
        rightIdx = len(s) - 1

        while leftIdx < rightIdx:
            # Traverse left until alphanumeric char is found
            while leftIdx < rightIdx and not s[leftIdx].isalnum():
                leftIdx += 1
            # Traverse right until alphanumeric char is found
            while leftIdx < rightIdx and not s[rightIdx].isalnum():
                rightIdx -= 1
            
            # Not palindrome
            if s[leftIdx].lower() != s[rightIdx].lower():
                return False
            
            leftIdx += 1
            rightIdx -= 1
                
        return True

    def isPalindromeV1(self, s: str) -> bool:
        if len(s) == 1:
            return True

        # Alphanumeric filtering + lowercasing
        alnumString = "".join([c.lower() for c in s if c.isalnum()])

        maxIdx = len(alnumString) // 2
        # print("[^^^] Alphanumeric String: ", alnumString)
        # print("[^^^] Max Idx: ", maxIdx)
        for i in range(maxIdx):
            left = alnumString[i]
            right = alnumString[-i-1]
            if left != right:
                # print(f"[^^^] Invalid matches, char on {i}: {left}, char on {len(alnumString) - i} (or -{i}): {right}")
                return False
        
        return True
        