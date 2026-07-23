class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counters = self.createCharCount(s)
        t_counters = self.createCharCount(t)

        if len(s_counters) != len(t_counters):
            return False
        
        for key in s_counters:
            if key not in t_counters:
                return False                
            if s_counters[key] != t_counters[key]:
                return False

        return True

    def createCharCount(self, s: str) -> dict:
        counter = {}
        for c in s:
            if c in counter:
                count = counter[c]
                counter[c] = count + 1
            else:
                counter[c] = 1
        return counter