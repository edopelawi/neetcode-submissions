class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Early return
        if len(strs) == 1:
            return [strs]

        keyMaps = {}

        for s in strs:
            key = self.generateHashKey(s)
            keyMaps.setdefault(key, []).append(s)            
        
        return list(keyMaps.values())

    # The V1 approach fails on "duh" and "ill".
    def groupAnagramsV1(self, strs: List[str]) -> List[List[str]]:
        # Early return
        if len(strs) == 1:
            return [strs]
        
        # Order: length of str, ascii sum of str, the str itself.
        richStrs = [(len(s), self.asciiSum(s), s) for s in strs]

        # Structure: len as key, contains dict with ascii sum as key with [str] as content.
        resultMap = {}

        # Main grouping logic
        for s_len, s_sum, s in richStrs:
            if s_len not in resultMap:
                s_array = [s]
                sumMap = {s_sum: s_array}
                resultMap[s_len] = sumMap
                continue
            
            sumMap = resultMap[s_len]
            if s_sum not in sumMap:
                sumMap[s_sum] = [s]                
            else:
                s_array = sumMap[s_sum]
                s_array.append(s)
                sumMap[s_sum] = s_array
            
            resultMap[s_len] = sumMap

        # Map out the result to expected format
        
        grouped_by_len_result = [list(len_dict.values()) for len_dict in list(resultMap.values())]
        final_result = [result for group in grouped_by_len_result for result in group]
        
        return final_result

    def asciiSum(self, s: str) -> int:
        return sum(map(ord, s))

    def generateHashKey(self, s: str) -> str:
        counter = self.generateAlphabetCounter(s)
        str_values = map(str, counter.values())
        return "#".join(str_values)

    def generateAlphabetCounter(self, s: str) -> dict:        
        lowerBound = ord('a')
        upperBound = ord('z')
        counter = dict.fromkeys(range(lowerBound, upperBound + 1), 0)

        asciiNums = map(ord, s)
        for num in asciiNums:
            count = counter[num]
            counter[num] = count + 1
        
        return counter