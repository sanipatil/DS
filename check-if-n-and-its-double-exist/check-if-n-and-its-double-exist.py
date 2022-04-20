class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort(reverse=True)
        a = []
        for elem in arr:
            if elem*2 in a or elem/2 in a:
                return True
            a.append(elem)
        return False
        
            
        