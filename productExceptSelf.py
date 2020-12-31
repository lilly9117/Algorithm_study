# 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #나눗셈 하지 않고 O(n)!!
        
        out = []
        p =1
        
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i] # 왼쪽부터 곱해서 result에 추가
        
        p =1
        
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums)-1, 0-1, -1): #1씩 줄어들게 range
            out[i] = out[i] *p # 여기서 기존 리스트 out 그대로 사용! (공간복잡도)
            p = p * nums[i]
            
            # p : 1 4 12 24
            # out : 24 12 8 6
        return out
        