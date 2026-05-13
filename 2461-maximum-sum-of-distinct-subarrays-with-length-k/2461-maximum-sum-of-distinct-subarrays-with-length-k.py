class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        i = 0
        curr_sum = 0
        max_sum = 0

        s = set()

        for j in range(len(nums)):

            # Remove duplicates
            while nums[j] in s:
                s.remove(nums[i])
                curr_sum -= nums[i]
                i += 1

            # Add current element
            s.add(nums[j])
            curr_sum += nums[j]

            # Maintain window size k
            if j - i + 1 > k:
                s.remove(nums[i])
                curr_sum -= nums[i]
                i += 1

            # Check valid window
            if j - i + 1 == k:
                max_sum = max(max_sum, curr_sum)

        return max_sum