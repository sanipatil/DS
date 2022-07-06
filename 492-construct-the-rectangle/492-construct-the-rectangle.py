class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        possiblePairs={}
        for i in range(1,area+1):
            if area % i == 0:
                j = area // i
                possiblePairs[i] = j
                
        prevDiff = float("inf")
        for key in possiblePairs:
            if key >= possiblePairs[key]:
                currentDiff = key - possiblePairs[key]
                if currentDiff < prevDiff:
                    prevDiff = currentDiff
                    res = [key,possiblePairs[key]]
        
        return res