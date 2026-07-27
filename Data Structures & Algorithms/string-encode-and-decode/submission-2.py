class Solution:

    # Expected Format
    # Encoding format: "#(length of string)#(String content)"
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        # print(f"[!!!] Encoding for string: {strs}")
        return "".join(f"#{len(item)}#{item}" for item in strs)


    def decode(self, s: str) -> List[str]:
        # print(f"[!!!] Decoding for string: {s}")
        endIndex = len(s)
        # Edge case
        if endIndex <= 1:
            return []

        separator = "#"
        result = []
        
        index = 0
        lengthStartPointer = 0
        waitForLength = False

        while index < endIndex:
            char = s[index]
            if waitForLength == False and char == separator:                
                waitForLength = True
                lengthStartPointer = index
                # print(f"[%%%] Start waiting for length, start pointer: {lengthStartPointer}")
            elif char == separator:
                # Build the pointers
                lengthText = s[lengthStartPointer+1:index]
                # print(f"[^^^] lengthText: {lengthText}, startPointer: {lengthStartPointer}, index: {index}")
                length = int(lengthText)
                textStartPointer = index + 1            
                textEndPointer = textStartPointer + length

                # Get the result
                substring = s[textStartPointer:textEndPointer]
                # print(f"[###] substring: {substring}, textStartPointer: {textStartPointer}, textEndPointer: {textEndPointer}")
                result.append(substring)

                # Jump to next pointer
                index = textEndPointer - 1
                waitForLength = False
            
            index += 1
        
        # print(f"[***] Final state, index: {index}, maxLength: {endIndex}")
        return result

        