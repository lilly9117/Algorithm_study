class Solution(object):
    # 브루트 포스로 계산 -> 타임아웃 ㅠㅠ
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_p = 0
        
        for i , price in enumerate(prices):
            for j in range(i, len(prices)):
                max_p = max(prices[j] - price, max_p)
        
        return max_p

    def maxProfit2(self, prices): #  저점과 현재 값과의 차이 계산
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min_p = sys.maxsize # 시스템이 즈정할 수 있는 가장 높은 값 - 에러방지
        
        # 최솟값 & 최댓값 update
        for p in prices:
            min_p = min(min_p, p)
            profit = max(profit, p - min_p)
            
        return profit 
        