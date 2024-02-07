class Solution(object):
    def countTestedDevices(self, batteryPercentages):
        """
        :type batteryPercentages: List[int]
        :rtype: int
        """
        tested = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] > 0:
                tested += 1
                for j in range(i + 1, len(batteryPercentages)):
                    batteryPercentages[j] = max(0, batteryPercentages[j] - 1)
        return tested
        