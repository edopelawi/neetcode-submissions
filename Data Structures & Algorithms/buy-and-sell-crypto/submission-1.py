class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0

        for price in prices[1:]:
            maxProfit = max(maxProfit, price - minPrice)
            minPrice = min(price, minPrice)

        return maxProfit

    def maxProfitLessPythonic(self, prices: List[int]) -> int:
        minPrice = None
        maxProfit = 0

        for idx in range(len(prices)):
            price = prices[idx]

            if minPrice is None:                
                minPrice = price
                continue
            
            profit = price - minPrice
            # print(f"[^^^] idx: {idx}, current minPrice: {minPrice}, current maxProfit: {maxProfit}, new price: {price}")
            if profit > maxProfit:
                # print("[^^^^^] new maxProfit unlocked: ", profit)
                maxProfit = profit

            if minPrice > price:
                # print("[^^^^^] new minPrice unlocked: ", price)
                minPrice = price

        
        return maxProfit
        