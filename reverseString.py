# 문자열 뒤집는 함수 

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) -1
        while left < right:
            s[left],s[right] = s[right], s[left] #투포인터 이용한 스왑
            left +=1
            right -=1
        
        # 파이썬 기본 기능 사용
        # s.reverse() 

        # s = s[::-1] # (X) 이 문제는 공간 복잡도 O(1)로 제한, 변수할당 처리하는데 제약 o