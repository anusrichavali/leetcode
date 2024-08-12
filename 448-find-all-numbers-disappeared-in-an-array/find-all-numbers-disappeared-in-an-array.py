class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash = {i: 0 for i in range(1, len(nums) + 1)}
        for i in nums:
            hash[i] += 1
        
        res = []
        for num in hash:
            if hash[num] == 0:
                res.append(num)

        return res
        