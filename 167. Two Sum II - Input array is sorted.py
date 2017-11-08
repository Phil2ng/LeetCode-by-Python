class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        j = len(numbers) - 1
        for i in range(0, len(numbers)):
            while(True):
                if numbers[i] + numbers[j] < target:
                    break
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
                if numbers[i] + numbers[j] > target:
                    j -= 1
