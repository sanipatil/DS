class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)
        stack = []
        numsdict = {}
        for i in range(len(nums1)):
            numsdict[nums1[i]] = i
        for i in range(len(nums2)):
            temp = nums2[i]
            while stack and temp > stack[-1]:
                result[numsdict[stack[-1]]] = temp
                stack.pop()
            if temp in numsdict:
                stack.append(temp)
        return result