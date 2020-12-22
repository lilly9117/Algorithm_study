# 유효한 팰린드롬

# 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

# 팰린드롬 : 앞뒤가 똑같은 문장 (뒤집어도 같은 말이 되는 단어 & 문장)

import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        
        s = re.sub('[^a-z0-9]', '', s)
        
        return s == s[::-1] #슬라이싱 이용 (뒤집어 버림)
            