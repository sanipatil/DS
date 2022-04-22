class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp_max = arr[len(arr)-1]
        arr[len(arr)-1] = -1
        i = len(arr)-2
        while i >= 0:
            j = arr[i]
            arr[i] = temp_max
            temp_max = max(temp_max,j)
            i -= 1
        return arr
            
            
            
        
        