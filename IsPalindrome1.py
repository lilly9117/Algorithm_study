#유효한 팰린드롬

#주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

#팰린드롬 : 앞뒤가 똑같은 문장 (뒤집어도 같은 말이 되는 단어 & 문장)

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        strs = []
        for char in s:
            if char.isalnum(): #영문자, 숫자 여부 판별
                strs.append(char.lower())
                
        while len(strs) > 1:
            #pop으로 index 지정 
            if strs.pop(0) != strs.pop(): # 맨마지막이랑 맨 첫번째거 비교!!!
                return False
        
        return True
            