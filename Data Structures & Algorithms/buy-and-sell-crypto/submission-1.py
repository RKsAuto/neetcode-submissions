class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        profit = 0
        for i in prices:
            if len(stack)==0 or stack[-1]<i:
                stack.append(i)
            else:
                profit = max(profit,stack[-1] - stack[0])
                while stack and stack[-1]>i:
                    stack.pop()
                stack.append(i)
        if stack:
            profit = max(profit,stack[-1] - stack[0])
        return profit
            

        