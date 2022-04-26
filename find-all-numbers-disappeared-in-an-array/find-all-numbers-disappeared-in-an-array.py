class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        count_dict = {}
        result = []
        for i in range(len(nums)):
            if nums[i] in count_dict:
                count_dict[nums[i]] += 1
            else:
                count_dict[nums[i]] = 1
            
        for j in range(1, len(nums)+1):
            if j not in count_dict:
                result.append(j)
                
        return result