class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while numbers[left] + numbers[right] != target:
            if numbers[right] > target - numbers[left]:
                right -= 1
            elif numbers[right] < target - numbers[left]:
                left += 1
        return [left + 1, right + 1]


            
