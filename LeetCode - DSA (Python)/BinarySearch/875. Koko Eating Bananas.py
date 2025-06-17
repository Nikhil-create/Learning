class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def findTotalHours(piles,numOfBananas):
            timeInHours = 0
            for bananas in piles:
                timeInHours += math.ceil(bananas/numOfBananas)
            return timeInHours

        minBananas = 1
        maxBananas = max(piles)

        while minBananas <= maxBananas:
            mid = (minBananas + maxBananas)//2

            totalHours = findTotalHours(piles,mid)

            if totalHours <= h:
                maxBananas = mid-1
            else:
                minBananas = mid+1

        return minBananas


        