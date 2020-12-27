class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 투 포인터가 중앙을 중심으로 확장하는 형태
        def expand(left, right):
            while (left >=0) and (right <= len(s)) and (s[left] == s[right-1]):
                left -=1
                right +=1
            return s[left+1:right-1]
            
        if len(s) < 2 or s == s[::-1]: # 예외 처리
            return s 
        
        result = ''
        for i in range(0, len(s)-1):
            result = max(result, expand(i,i+1), expand(i,i+2), key = len) #가장 긴거 뽑아내기
            
        return result
        