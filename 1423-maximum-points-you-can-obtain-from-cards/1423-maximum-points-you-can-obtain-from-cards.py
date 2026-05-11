class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
   

        n = len(cardPoints)

        # if taking all cards
        if k == n:
            return sum(cardPoints)

        total = sum(cardPoints)

        window_size = n - k

        # first window sum
        window_sum = sum(cardPoints[:window_size])

        min_sum = window_sum

        left = 0

        # slide the window
        for right in range(window_size, n):

            window_sum += cardPoints[right]
            window_sum -= cardPoints[left]

            left += 1

            min_sum = min(min_sum, window_sum)

        return total - min_sum
        