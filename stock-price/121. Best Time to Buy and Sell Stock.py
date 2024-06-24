class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Max profit = highest price that occurs AFTER global lowest price
        Iterate through array, keep track of lowest price so far,
        and update max profit with curPrice - lowest
        """
        res = 0

        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res
