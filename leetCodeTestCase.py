
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        len_arr = len(prices)
        minI = prices[0]
        for i in range(0,len_arr):
            if prices[i] < minI:
                minI = prices[i]
        if minI == len_arr-1:
            return 0

        maxI = prices[minI]
        for i in range(minI,len_arr):
            if prices[i] > maxI:
                maxI = prices[i]
        
        profit = prices[maxI] - prices[minI]
        return profit
            


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