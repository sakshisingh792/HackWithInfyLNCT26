class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
            last1 = -1
            last2 = -1
            minm = float("inf")

            for i in range(len(nums)):
                if nums[i] == 1:
                    last1 = i
                    if last2 != -1:
                        minm = min(minm, abs(last1 - last2))

                elif nums[i] == 2:
                    last2 = i
                    if last1 != -1:
                        minm = min(minm, abs(last1 - last2))

            return -1 if minm == float("inf") else minm
                