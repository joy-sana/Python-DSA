
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        min_price = float('inf')  
        max_profit = 0
#               [7, 1, 5, 3, 6, 4]
        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        
        return max_profit

def run_test_cases():
    solution = Solution()

    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5), 
        ([7, 6, 4, 3, 1], 0),      
        ([2, 4, 1], 2),          
    ]

    for i, (prices, expected) in enumerate(test_cases, 1):
        result = solution.maxProfit(prices)
        print(f"Test Case {i}: Prices = {prices}")
        print(f"Expected Profit = {expected}, Calculated Profit = {result}")
        print("Pass" if result == expected else "Fail")
        print("-" * 50)


if __name__ == "__main__":
    run_test_cases()